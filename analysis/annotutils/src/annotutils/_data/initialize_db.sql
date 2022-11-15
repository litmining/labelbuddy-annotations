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
  name text unique not null
);

create table annotator(
  id integer primary key,
  name text unique not null
);

create table annotation(
  id integer primary key,
  doc_id not null references document(id) on delete cascade,
  label_id not null references label(id) on delete cascade,
  annotator_id not null references annotator(id) on delete cascade,
  start_char integer not null,
  end_char integer not null,
  extra_data text,
  project text not null
);

create table db_info(
  key text unique not null,
  value
);

create view detailed_annotation as
  select
    pmcid, pmid, publication_year, journal, title,
    label.name as label_name,
    annotator.name as annotator_name,
    start_char, end_char, extra_data, project,
    substring(
      document.text, start_char + 1, end_char - start_char) as selected_text
    from annotation
         inner join label on annotation.label_id = label.id
         inner join document on annotation.doc_id = document.id
         inner join annotator on annotation.annotator_id = annotator.id
   order by document.id, start_char, end_char,
            label_name, annotator_name, annotation.id;
