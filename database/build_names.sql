-- name:    build_names.sql
-- version: 0.0.1
-- date:    20241020
-- author:  Leam Hall
-- desc:    Create the names schemas for the database, then add data.

.headers    on  
.nullvalue  [NULL]
.echo       on


DROP TABLE IF EXISTS human_last;
CREATE TABLE human_last (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);
.read database/human_last_names.sql


DROP TABLE IF EXISTS human_female_first;
CREATE TABLE human_female_first (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);
.read database/human_female_first_names.sql


DROP TABLE IF EXISTS human_male_first;
CREATE TABLE human_male_first (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);
.read database/human_male_first_names.sql

