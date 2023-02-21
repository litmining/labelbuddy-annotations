#! /bin/bash

export LABELREPO_CSS_AVAILABLE=1
export LABELREPO_PROJECTS_BASE_URL="./projects/"
export LABELREPO_PROJECTS_HTML_EXTENSION=1
export LABELREPO_PROJECTS_URL_ESCAPE_DOT=1

jupyter-book build -W analysis/book
