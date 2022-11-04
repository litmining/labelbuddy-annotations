labelbuddy_databases := $(shell find -type f -name '*.labelbuddy')
annotation_files := $(patsubst %.labelbuddy, %.jsonl, $(labelbuddy_databases))

.PHONY: all annotations database

all: annotations

annotations: $(annotation_files)

database:
	./scripts/database.py

$(annotation_files): %.jsonl: %.labelbuddy
	labelbuddy $< --export-docs $@ --no-text --labelled-only
