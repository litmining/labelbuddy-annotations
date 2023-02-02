create table project (
  name text not null primary key
);

create table document(
  id integer primary key,
  utf8_text_md5_checksum blob unique not null,
  text text not null,
  pmcid integer,
  pmid integer,
  publication_year integer,
  journal text,
  title text
);

create table label(
  id integer primary key,
  name text unique not null,
  color text
);

create table project_label(
  project_name text not null references project(name) on delete cascade,
  label_id integer not null references label(id) on delete cascade,
  constraint unique_project_name_label_id unique (project_name, label_id)
  on conflict ignore
);

create table annotator(
  name text not null primary key
);

create table annotation(
  id integer primary key,
  doc_id not null references document(id) on delete cascade,
  label_id not null references label(id) on delete cascade,
  annotator_name not null references annotator(name) on delete cascade,
  start_char integer not null,
  end_char integer not null,
  extra_data text,
  project_name text not null references project(name) on delete cascade
);

create table db_info(
  key text unique not null,
  value
);

create view detailed_annotation as
  with annot as
  (select *,
          max(0, start_char - 200) as context_start_char,
          min(length(document.text), end_char + 200) as context_end_char,
          annotation.id as annotation_id
     from annotation inner join document on annotation.doc_id = document.id)
  select
    pmcid, pmid, publication_year, journal, title,
    label.name as label_name,
    label.color as label_color,
    annotator_name,
    start_char, end_char, extra_data, project_name,
    substr(
      text, start_char + 1, end_char - start_char) as selected_text,
    substr(
      text,
      context_start_char + 1,
      context_end_char - context_start_char
    ) as context,
    context_start_char, context_end_char,
    length(text) as doc_length
    from annot
         inner join label on annot.label_id = label.id
   order by doc_id, start_char, end_char,
            label_id, annotator_name, annot.id;
