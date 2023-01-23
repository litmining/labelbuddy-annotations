"""Downloading full datasets from which documents were extracted."""

import json
import os
import pathlib
import re
import shutil
import sqlite3
import tempfile
import time
from typing import List
from urllib import request

from labelrepo import repo


_BUFFER_SIZE = 1024 * 1024


def _init_db(connection: sqlite3.Connection):
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS
        downloads (
            url NOT NULL UNIQUE ON CONFLICT REPLACE,
            local_path NOT NULL UNIQUE ON CONFLICT REPLACE
        )
        """
    )


def _downloads_db_connection(
    downloads_dir: pathlib.Path,
) -> sqlite3.Connection:
    db_path = downloads_dir / ".downloads.sqlite3"
    with sqlite3.connect(db_path) as connection:
        _init_db(connection)
    return sqlite3.connect(db_path)


def _convert_osf_url_to_download(url: str) -> str:
    if "download" in url:
        return url
    match = re.match(r"^https://osf.io/([0-9a-zA-Z]+)/?$", url)
    if match is None:
        return url
    osf_id = match.group(1)
    return f"https://osf.io/download/{osf_id}/"


def _format_time(seconds: int) -> str:
    hours, rest = divmod(seconds, 3600)
    minutes, rest = divmod(rest, 60)
    hinfo = f"{hours}h " if hours else ""
    minfo = f"{minutes:>02}m " if minutes else ""
    sinfo = f"{rest:>02}s"
    return "".join((hinfo, minfo, sinfo))


def _download_url(url: str, target_file: pathlib.Path) -> None:
    with request.urlopen(url) as response:
        total_size = int(response.headers["Content-Length"].strip())
        print(f"total size: {total_size} ({total_size / 1e9:.1f} GB)")
        downloaded = 0
        print()
        start_time = time.time()
        with open(target_file, "wb") as output_stream:
            while True:
                buffer = response.read(_BUFFER_SIZE)
                if not buffer:
                    break
                downloaded += len(buffer)
                proportion = downloaded / total_size
                dl_msg = f"({downloaded / 1e6: <.0f} MB)"
                elapsed = time.time() - start_time
                speed = downloaded / (elapsed + 1e-9)
                remaining = total_size - downloaded
                eta = int(remaining / (speed + 1e-9))
                eta_msg = f"eta {_format_time(eta)}"
                print(
                    f"\r{proportion: <4.0%} {dl_msg: <10} {eta_msg: >10}",
                    end="",
                    flush=True,
                )
                output_stream.write(buffer)
            print()


def _extract_archive(
    archive_file: pathlib.Path, downloads_dir: pathlib.Path
) -> pathlib.Path:
    with tempfile.TemporaryDirectory(
        dir=downloads_dir, ignore_cleanup_errors=True
    ) as tmp_dir:
        print("Extracting archive contents...")
        shutil.unpack_archive(archive_file, tmp_dir)
        contents = list(pathlib.Path(tmp_dir).glob("*"))
        assert len(contents) == 1
        extracted = contents[0]
        result_path = downloads_dir / extracted.name
        if result_path.exists():
            shutil.rmtree(result_path)
        extracted.rename(result_path)
    return result_path


def _download_archive(url: str, downloads_dir: pathlib.Path) -> pathlib.Path:
    print(f"Downloading {url}")
    fd, tmp_file_name = tempfile.mkstemp(suffix=".tar.gz", dir=downloads_dir)
    os.close(fd)
    tmp_file = pathlib.Path(tmp_file_name)
    try:
        _download_url(url, tmp_file)
        extracted_path = _extract_archive(tmp_file, downloads_dir)
    finally:
        try:
            tmp_file.unlink()
        except Exception:
            pass
    with _downloads_db_connection(downloads_dir) as connection:
        connection.execute(
            "INSERT INTO downloads (url, local_path) VALUES (?, ?)",
            (url, str(extracted_path.relative_to(downloads_dir))),
        )
    return extracted_path


def _get_archive(url: str, downloads_dir: str | pathlib.Path) -> pathlib.Path:
    downloads_dir = pathlib.Path(downloads_dir)
    with _downloads_db_connection(downloads_dir) as connection:
        result = connection.execute(
            "SELECT local_path FROM downloads WHERE url=?", (url,)
        ).fetchone()
        if result is not None:
            return downloads_dir / result[0]
    url = _convert_osf_url_to_download(url)
    return _download_archive(url, downloads_dir)


def get_dataset(url: str) -> pathlib.Path:
    downloads_dir = repo.data_dir() / "datasets"
    downloads_dir.mkdir(exist_ok=True)
    return _get_archive(url, downloads_dir)


def get_project_datasets(project_name: str) -> List[pathlib.Path]:
    project_dir = repo.repo_root() / "projects" / project_name
    sources_json = project_dir / "documents" / "datasets.json"
    if not sources_json.is_file():
        return []
    sources_info = json.loads(sources_json.read_text("UTF-8"))
    result = []
    for source in sources_info:
        result.append(get_dataset(source["url"]))
    return result
