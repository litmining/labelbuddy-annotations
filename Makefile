databases := $(shell find -type f -name '*.labelbuddy')
annotation_files := $(patsubst %.labelbuddy, %.jsonl, $(databases))

.PHONY: all annotations

all: annotations

annotations: $(annotation_files)

$(annotation_files): %.jsonl: %.labelbuddy
	labelbuddy $< --export-docs $@ --no-text --labelled-only
