import asyncio
import json
import pathlib
import sqlite3
import time
from typing import Union

import pandas as pd
import websockets

from labelrepo.projects.participant_demographics import (
    _participant_demographics,
)


class _Watcher:
    def __init__(
        self, labelbuddy_file: Union[pathlib.Path, str], port: int
    ) -> None:
        self.socket_connections = set()
        self.labelbuddy_file = pathlib.Path(labelbuddy_file)
        self.target_file = self.labelbuddy_file.with_name(
            f"{self.labelbuddy_file.stem}_participants_demographics_"
            "live_report.html"
        ).resolve()
        self.last_wake_up_time = None
        self.last_update_time = None
        self.period = 0.5
        self.connection = sqlite3.connect(
            f"file:{self.labelbuddy_file}?mode=ro"
        )
        self.connection.row_factory = sqlite3.Row
        self.project_name = self.labelbuddy_file.parents[1].name
        self.annotator_name = self.labelbuddy_file.stem
        jinja_env = _participant_demographics._get_jinja_env()
        self.page = jinja_env.get_template("live_report.html").render(
            {"port": port}
        )
        self.template = jinja_env.get_template("report.html")
        print(f"Watching file: {self.labelbuddy_file}")
        self.content = ""
        self._update_content()

    async def start(self) -> None:
        self.target_file.write_text(self.page)
        print(
            "To see the live participant demographics report, "
            "visit this file in your web browser:\n\n"
            f"{self.target_file}"
        )
        while True:
            previous_wake_up_time = self.last_wake_up_time
            self.last_wake_up_time = time.time()
            if (
                previous_wake_up_time is None
                or (
                    self.labelbuddy_file.stat().st_mtime
                    > previous_wake_up_time
                )
                or self.last_update_time is None
                or (time.time() - self.last_update_time > 5)
            ):
                try:
                    self._update_content()
                except Exception:
                    self.content = """<div>
                    There was an error while generating the report
                    </div>"""
                self.last_update_time = time.time()
                websockets.broadcast(self.socket_connections, self.content)
            to_wait = self.period - (time.time() - self.last_wake_up_time)
            if to_wait > 0:
                await asyncio.sleep(to_wait)

    def _update_content(self) -> None:
        doc_info = self.connection.execute(
            """
        select id, lower(hex(content_md5)) as md5, metadata,
        coalesce(list_title, substring(content, 1, 150)) as title
        from document
        where id = (select last_visited_doc from app_state)
        """
        ).fetchone()
        metadata = json.loads(doc_info["metadata"])

        demo_labels = ", ".join(
            map("'{}'".format, _participant_demographics._DEMOGRAPHICS_LABELS)
        )
        annotations = self.connection.execute(
            f"""
        with doc as (select content from document where id = :doc)
        select label.name as label_name, label.color as label_color,
        start_char, end_char, extra_data,
        substring(content, start_char + 1, end_char - start_char)
        as selected_text
        from annotation, doc
        inner join label on annotation.label_id = label.id
        where doc_id = :doc
        and label_name in ({demo_labels})
        """,
            {"doc": doc_info["id"]},
        )

        anno_df = pd.DataFrame(
            {
                "pmcid": metadata["pmcid"],
                "title": doc_info["title"],
                "doc_md5": doc_info["md5"],
                "project_name": self.project_name,
                "annotator_name": self.annotator_name,
            }
            | dict(anno)
            for anno in annotations
        )
        if not anno_df.shape[0]:
            self.content = f"""<div>
            <h2>PMC{metadata['pmcid']}</h2>
            <p>
            No participant group annotations for this document (yet!)
            </p>
            </div>
            """
            return
        summaries = _participant_demographics._get_document_summaries(anno_df)
        self.content = self.template.render(
            {
                "documents": summaries,
                "standalone": False,
                "no_doc_positions": True,
                "live_report": True,
            }
        )

    async def register(self, socket):
        self.socket_connections.add(socket)
        await socket.send(self.content)
        try:
            await socket.wait_closed()
        finally:
            self.socket_connections.remove(socket)


async def watch_participants(
    labelbuddy_file: Union[pathlib.Path, str], port: int = 8765
) -> None:
    watcher = _Watcher(labelbuddy_file, port)

    async with websockets.serve(watcher.register, "localhost", port):
        await watcher.start()
