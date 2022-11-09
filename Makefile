labelbuddy_databases := $(shell find . -type f -name '*.labelbuddy')
annotation_files := $(patsubst %.labelbuddy, %.jsonl, $(labelbuddy_databases))

.PHONY: all annotations database book

all: annotations

annotations: $(annotation_files)

database:
	python3 ./scripts/make_database.py

$(annotation_files): %.jsonl: %.labelbuddy
	labelbuddy $< --export-docs $@ --no-text --labelled-only

book:
	jupyter-book build analysis/book
