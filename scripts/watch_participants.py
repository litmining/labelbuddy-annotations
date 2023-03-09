#! /usr/bin/env python3

import asyncio
import argparse
import sys
import threading
import time
import webbrowser

from labelrepo import repo
from labelrepo.projects.participant_demographics import (
    watch_participants,
    get_live_report_path,
)

parser = argparse.ArgumentParser()
parser.add_argument("labelbuddy_database", type=str, nargs="?", default=None)
parser.add_argument("-p", "--port", type=int, default=8765)
parser.add_argument("--no_browser", action="store_true")
args = parser.parse_args()

if args.labelbuddy_database is not None:
    labelbuddy_database = args.labelbuddy_database
else:
    labelbuddy_database = repo.last_modified_labelbuddy_file()
    if labelbuddy_database is None:
        print("Could not find a labelbuddy file to watch.")
        sys.exit(1)
    print(
        "Using the most recently modified labelbuddy file: "
        f"{labelbuddy_database}\n"
        "To watch a different file, pass its path on the command line.\n"
    )

port = args.port
report_path = get_live_report_path(labelbuddy_database, port)
start_time = time.time()


def start_browser():
    for _ in range(8):
        time.sleep(0.5)
        try:
            m_time = report_path.stat().st_mtime
        except FileNotFoundError:
            continue
        if m_time > start_time:
            try:
                webbrowser.open(report_path.as_uri())
            except Exception:
                pass
            return


if not args.no_browser:
    opener = threading.Thread(target=start_browser)
    opener.start()

try:
    asyncio.run(watch_participants(labelbuddy_database, port))
except KeyboardInterrupt:
    print()
    sys.exit(0)
