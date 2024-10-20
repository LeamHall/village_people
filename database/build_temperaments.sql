-- name:    build_temperaments.sql
-- version: 0.0.1
-- date:    20201121
-- author:  Leam Hall
-- desc:    Create a temperaments table.

.headers    on
.nullvalue  [NULL]
.echo       on

-- Schema
DROP TABLE IF EXISTS temperaments;

CREATE TABLE temperaments (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);

-- Data
BEGIN DEFERRED;
INSERT INTO temperaments (item) VALUES ( 'Crafter' );
INSERT INTO temperaments (item) VALUES ( 'Promoter' );
INSERT INTO temperaments (item) VALUES ( 'Composer' );
INSERT INTO temperaments (item) VALUES ( 'Performer' );
INSERT INTO temperaments (item) VALUES ( 'Inspector' );
INSERT INTO temperaments (item) VALUES ( 'Supervisor' );
INSERT INTO temperaments (item) VALUES ( 'Protector' );
INSERT INTO temperaments (item) VALUES ( 'Provider' );
INSERT INTO temperaments (item) VALUES ( 'Counselor' );
INSERT INTO temperaments (item) VALUES ( 'Teacher' );
INSERT INTO temperaments (item) VALUES ( 'Healer' );
INSERT INTO temperaments (item) VALUES ( 'Champion' );
INSERT INTO temperaments (item) VALUES ( 'Mastermind' );
INSERT INTO temperaments (item) VALUES ( 'Fieldmarshal' );
INSERT INTO temperaments (item) VALUES ( 'Architect' );
INSERT INTO temperaments (item) VALUES ( 'Inventor' );
END;
