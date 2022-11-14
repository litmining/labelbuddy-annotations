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
