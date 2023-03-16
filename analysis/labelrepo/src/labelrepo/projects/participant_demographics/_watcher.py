from __future__ import annotations

import asyncio
import json
import pathlib
import sqlite3
import sys
from typing import Optional, Set, Union

import pandas as pd
import websockets

from labelrepo.projects.participant_demographics import (
    _participant_demographics, _interpreter
)


def get_live_report_path(
    labelbuddy_file: Union[pathlib.Path, str], port
) -> pathlib.Path:
    lb_file = pathlib.Path(labelbuddy_file)
    return lb_file.with_name(
        f"{lb_file.stem}_participants_live_report_{port}.html"
    ).resolve()


class _Watcher:
    def __init__(
        self, labelbuddy_file: Union[pathlib.Path, str], port: int
    ) -> None:
        self.socket_connections: Set = set()
        self.labelbuddy_file = pathlib.Path(labelbuddy_file)
        self.target_file = get_live_report_path(self.labelbuddy_file, port)
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
        self.connection: Optional[sqlite3.Connection] = None
        self.data_version = None

    def __enter__(self) -> _Watcher:
        self.labelbuddy_file.stat()
        try:
            self.connection = sqlite3.connect(
                f"{self.labelbuddy_file.resolve().as_uri()}?mode=ro"
            )
        except sqlite3.OperationalError:
            self.connection = sqlite3.connect(self.labelbuddy_file.resolve())
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
            if self.connection is not None:
                self.connection.close()
        except Exception:
            pass

    def _need_update(self) -> bool:
        old_data_version = self.data_version
        assert self.connection is not None
        self.data_version = self.connection.execute(
            "pragma data_version"
        ).fetchone()[0]
        if old_data_version is None:
            return True
        return self.data_version != old_data_version

    async def start(self) -> None:
        assert (
            self.connection is not None
        ), f"Use {self.__class__.__name__} as a context manager."
        self.target_file.write_text(self.page)
        print(
            "\nTo see the live participant demographics report, "
            "visit this address in your web browser:\n\n"
            f"{self.target_file.as_uri()}\n"
        )
        while True:
            if self._need_update():
                try:
                    self._update_content()
                except Exception:
                    self.content = """<div>
                    There was an error while generating the report
                    </div>"""
                for connection in self.socket_connections:
                    await connection.send(self.content)
            await asyncio.sleep(self.delay)

    def _update_content(self) -> None:
        assert self.connection is not None
        doc_result = self.connection.execute(
            """
        select id, lower(hex(content_md5)) as md5, metadata,
        coalesce(list_title, substr(content, 1, 150)) as title
        from document
        where id = coalesce( (select last_visited_doc from app_state),
            (select id from document limit 1) )
        """
        ).fetchone()
        metadata = json.loads(doc_result["metadata"])

        demo_labels = ", ".join(
            map("'{}'".format, _interpreter.demographics_labels())
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
        substr(content, start_char + 1, end_char - start_char)
        as selected_text,
        substr(content, context_start_char + 1,
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
        anno_df = pd.DataFrame({**doc_info, **anno} for anno in annotations)
        if not anno_df.shape[0]:
            summaries = [dict(doc_info, participants=None)]
        else:
            summaries = _participant_demographics._get_document_summaries(
                anno_df
            )
            summaries[0]["doc_uid"] = doc_result["id"]
        template_params = {
            "documents": summaries,
            "standalone": False,
            "no_doc_positions": True,
            "noscript": True,
        }
        template_params.update(
            _participant_demographics._get_template_data(self.labelbuddy_file)
        )
        self.content = self.template.render(template_params)

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
