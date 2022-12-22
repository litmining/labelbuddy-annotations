"""Downloading full datasets from which documents were extracted."""

import json
import os
import pathlib
import re
import shutil
import tempfile
import time
from typing import List
from urllib import request

from labelrepo import repo


_BUFFER_SIZE = 1024 * 1024


def _convert_osf_url_to_download(url: str) -> str:
    if "download" in url:
        return url
    match = re.match(r"^https://osf.io/([0-9a-zA-Z]+)/?$", url)
    if match is None:
        return url
    osf_id = match.group(1)
    return f"https://osf.io/download/{osf_id}/"


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
                eta_msg = f"eta {eta}s"
                print(
                    f"\r{proportion: <4.0%} {dl_msg: <10} {eta_msg: >10}",
                    end="",
                    flush=True,
                )
                output_stream.write(buffer)
            print()


def _extract_archive(
    archive_file: pathlib.Path, target_dir: pathlib.Path, name: str
) -> None:
    with tempfile.TemporaryDirectory(
        dir=target_dir, ignore_cleanup_errors=True
    ) as tmp_dir:
        print("Extracting archive contents...")
        shutil.unpack_archive(archive_file, tmp_dir)
        contents = list(pathlib.Path(tmp_dir).glob("*"))
        assert len(contents) == 1
        extracted = contents[0]
        assert extracted.name == name
        extracted.rename(target_dir / extracted.name)


def _download_archive(url: str, target_dir: pathlib.Path, name: str) -> None:
    print(f"Downloading {url}")
    fd, tmp_file_name = tempfile.mkstemp(suffix=".tar.gz", dir=target_dir)
    os.close(fd)
    tmp_file = pathlib.Path(tmp_file_name)
    try:
        _download_url(url, tmp_file)
        _extract_archive(tmp_file, target_dir, name)
    finally:
        try:
            tmp_file.unlink()
        except Exception:
            pass


def _get_archive(
    url: str, target_dir: str | pathlib.Path, target_name: str
) -> pathlib.Path:
    target_dir = pathlib.Path(target_dir)
    target = target_dir / target_name
    if target.exists():
        return target
    url = _convert_osf_url_to_download(url)
    _download_archive(url, target_dir, target_name)
    assert target.exists()
    return target


def get_documents_source_dir(url: str, name: str) -> pathlib.Path:
    sources_dir = repo.data_dir() / "document_sources"
    sources_dir.mkdir(exist_ok=True)
    return _get_archive(url, sources_dir, name)


def get_project_document_sources(project_name: str) -> List[pathlib.Path]:
    project_dir = repo.repo_root() / "projects" / project_name
    sources_json = project_dir / "documents" / "doc_sources.json"
    if not sources_json.is_file():
        return []
    sources_info = json.loads(sources_json.read_text("UTF-8"))
    result = []
    for source in sources_info:
        result.append(get_documents_source_dir(source["url"], source["name"]))
    return result
