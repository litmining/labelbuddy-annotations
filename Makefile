labelbuddy_databases := $(shell find . -type f -name '*.labelbuddy')
annotation_files := $(patsubst %.labelbuddy, %.jsonl, $(labelbuddy_databases))
repo_stats_fig := analysis/book/assets/generated/repo_stats.svg
projects_tag_file := analysis/book/projects/DONT_EDIT_THIS_DIRECTORY_IT_IS_AUTOMATICALLY_GENERATED

.PHONY: all annotations database csv book book-full clean

all: annotations

annotations: $(annotation_files)

database: analysis/data/database.sqlite3

csv: analysis/data/detailed_annotation.csv

analysis/data/database.sqlite3:
	python3 ./scripts/make_database.py

analysis/data/detailed_annotation.csv: analysis/data/database.sqlite3
	sqlite3 -header -csv $< "select * from detailed_annotation;" > $@

$(annotation_files): %.jsonl: %.labelbuddy
	labelbuddy $< --export-docs $@ --no-text --labelled-only

$(repo_stats_fig):
	python3 scripts/make_repo_stats_figure.py

$(projects_tag_file):
	python3 analysis/book_helpers/add_project_pages.py

book: $(repo_stats_fig) $(projects_tag_file)
	# the prerequisites make sure the files exist so jupyter-book doesn't crash,
	# but they don't enforce that they are up to date -- for that use book-full
	./scripts/make_book.sh

book-full: database csv
	rm -rf analysis/book/_build/
	rm -rf analysis/book/projects/
	python3 scripts/make_repo_stats_figure.py
	python3 scripts/make_participants_csv.py
	python3 analysis/book_helpers/add_project_pages.py
	./scripts/make_book.sh

clean:
	rm -rf analysis/data/database.sqlite3 analysis/data/detailed_annotation.csv analysis/book/_build analysis/book/projects
