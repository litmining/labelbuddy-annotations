from __future__ import annotations

import asyncio
import json
import pathlib
import sqlite3
import time
import sys
from typing import Optional, Set, Union

import pandas as pd
import websockets

from labelrepo.projects.participant_demographics import (
    _participant_demographics,
)


class _Watcher:
    def __init__(
        self, labelbuddy_file: Union[pathlib.Path, str], port: int
    ) -> None:
        self.socket_connections: Set = set()
        self.labelbuddy_file = pathlib.Path(labelbuddy_file)
        self.target_file = self.labelbuddy_file.with_name(
            f"{self.labelbuddy_file.stem}_participants_live_report_{port}.html"
        ).resolve()
        self.last_wake_up_time: Optional[float] = None
        self.delay = 0.25
        self.project_name = self.labelbuddy_file.parents[1].name
        self.annotator_name = self.labelbuddy_file.stem
        jinja_env = _participant_demographics._get_jinja_env()
        self.page = jinja_env.get_template("live_report.html").render(
            {"port": port}
        )
        self.template = jinja_env.get_template("report.html")
        print(f"Watching file: {self.labelbuddy_file}")
        self.content = ""
        self.connection = None

    def __enter__(self) -> _Watcher:
        self.labelbuddy_file.stat()
        self.connection = sqlite3.connect(
            f"file:{self.labelbuddy_file}?mode=ro"
        )
        self.connection.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type, exc_val, tb):
        del exc_type, exc_val, tb
        if self.target_file.is_file():
            try:
                self.target_file.unlink()
            except Exception:
                pass
        try:
            self.connection.close()
        except Exception:
            pass

    async def start(self) -> None:
        assert (
            self.connection is not None
        ), f"Use {self.__class__.__name__} as a context manager."
        self.target_file.write_text(self.page)
        print(
            "\nTo see the live participant demographics report, "
            "visit this file in your web browser:\n\n"
            f"{self.target_file}\n"
        )
        while True:
            previous_wake_up_time = self.last_wake_up_time
            self.last_wake_up_time = time.time()
            if previous_wake_up_time is None or (
                self.labelbuddy_file.stat().st_mtime > previous_wake_up_time
            ):
                try:
                    self._update_content()
                except Exception:
                    self.content = """<div>
                    There was an error while generating the report
                    </div>"""
                websockets.broadcast(self.socket_connections, self.content)
            await asyncio.sleep(self.delay)

    def _update_content(self) -> None:
        doc_result = self.connection.execute(
            """
        select id, lower(hex(content_md5)) as md5, metadata,
        coalesce(list_title, substring(content, 1, 150)) as title
        from document
        where id = coalesce( (select last_visited_doc from app_state),
            (select id from document limit 1) )
        """
        ).fetchone()
        metadata = json.loads(doc_result["metadata"])

        demo_labels = ", ".join(
            map("'{}'".format, _participant_demographics._DEMOGRAPHICS_LABELS)
        )
        annotations = self.connection.execute(
            f"""with annot as
        (select document.content,
        annotation.*, max(0, start_char - 200) as context_start_char,
        min(length(content), end_char + 200) as context_end_char
        from annotation, document
        where annotation.doc_id = :doc and document.id = :doc)
        select label.name as label_name, label.color as label_color,
        start_char, end_char, extra_data,
        context_start_char, context_end_char,
        length(content) as doc_length,
        substring(content, start_char + 1, end_char - start_char)
        as selected_text,
        substring(content, context_start_char + 1,
        context_end_char - context_start_char) as context
        from annot
        inner join label on annot.label_id = label.id
        and label_name in ({demo_labels})
        """,
            {"doc": doc_result["id"]},
        )
        doc_info = {
            "pmcid": metadata["pmcid"],
            "title": doc_result["title"],
            "doc_md5": doc_result["md5"],
            "project_name": self.project_name,
            "annotator_name": self.annotator_name,
        }
        anno_df = pd.DataFrame(doc_info | dict(anno) for anno in annotations)
        if not anno_df.shape[0]:
            summaries = [doc_info | {"participants": None}]
        else:
            summaries = _participant_demographics._get_document_summaries(
                anno_df
            )
            summaries[0]["doc_uid"] = doc_result["id"]
        self.content = self.template.render(
            {
                "documents": summaries,
                "standalone": False,
                "no_doc_positions": True,
                "noscript": True,
            }
            | _participant_demographics._get_template_data(
                self.labelbuddy_file
            )
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
    try:
        async with websockets.serve(watcher.register, "localhost", port):
            with watcher:
                await watcher.start()
    except OSError as error:
        print(f"\nServing the live report failed due to:\n\n    {error}\n")
        sys.exit(1)
