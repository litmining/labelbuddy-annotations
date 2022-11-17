labelbuddy_databases := $(shell find . -type f -name '*.labelbuddy')
annotation_files := $(patsubst %.labelbuddy, %.jsonl, $(labelbuddy_databases))

.PHONY: all annotations database csv book

all: annotations

annotations: $(annotation_files)

database:
	python3 ./scripts/make_database.py

csv: analysis/data/detailed_annotation.csv

analysis/data/detailed_annotation.csv: analysis/data/database.sqlite3
	sqlite3 -header -csv $< "select * from detailed_annotation;" > $@

$(annotation_files): %.jsonl: %.labelbuddy
	labelbuddy $< --export-docs $@ --no-text --labelled-only

book:
	jupyter-book build -W analysis/book
