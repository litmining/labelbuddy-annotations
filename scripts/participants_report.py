#! /usr/bin/env python3

from labelrepo import database
from labelrepo.projects import participant_demographics

database.make_database()
participant_demographics.report_command()
