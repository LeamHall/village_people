-- name:    build_plots.sql
-- version: 0.0.1
-- date:    20201121
-- author:  Leam Hall
-- desc:    Create a sample plots table.

.headers    on
.nullvalue  [NULL]
.echo       on

-- Schema
DROP TABLE IF EXISTS plots;

CREATE TABLE plots (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);

-- Data
BEGIN DEFERRED;
INSERT INTO plots (item) VALUES ( 'Supplication' );
INSERT INTO plots (item) VALUES ( 'Deliverance' );
INSERT INTO plots (item) VALUES ( 'Crime pursued by vengeance' );
INSERT INTO plots (item) VALUES ( 'Vengeance taken for kin upon kin' );
INSERT INTO plots (item) VALUES ( 'Pursuit' );
INSERT INTO plots (item) VALUES ( 'Disaster' );
INSERT INTO plots (item) VALUES ( 'Falling prey to cruelty/misfortune' );
INSERT INTO plots (item) VALUES ( 'Revolt' );
INSERT INTO plots (item) VALUES ( 'Daring enterprise' );
INSERT INTO plots (item) VALUES ( 'Abduction' );
INSERT INTO plots (item) VALUES ( 'The enigma' );
INSERT INTO plots (item) VALUES ( 'Obtaining' );
INSERT INTO plots (item) VALUES ( 'Enmity of kin' );
INSERT INTO plots (item) VALUES ( 'Rivalry of kin' );
INSERT INTO plots (item) VALUES ( 'Murderous adultery' );
INSERT INTO plots (item) VALUES ( 'Madness' );
INSERT INTO plots (item) VALUES ( 'Fatal imprudence' );
INSERT INTO plots (item) VALUES ( 'Involuntary crimes of love' );
INSERT INTO plots (item) VALUES ( 'Slaying of kin unrecognized' );
INSERT INTO plots (item) VALUES ( 'Self-sacrifice for an ideal' );
INSERT INTO plots (item) VALUES ( 'Self-sacrifice for kin' );
INSERT INTO plots (item) VALUES ( 'All sacrificed for passion' );
INSERT INTO plots (item) VALUES ( 'Necessity of sacrificing loved ones' );
INSERT INTO plots (item) VALUES ( 'Rivalry of superior vs. inferior' );
INSERT INTO plots (item) VALUES ( 'Adultery' );
INSERT INTO plots (item) VALUES ( 'Crimes of love' );
INSERT INTO plots (item) VALUES ( 'Discovery of the dishonour of a loved one' );
INSERT INTO plots (item) VALUES ( 'Obstacles to love' );
INSERT INTO plots (item) VALUES ( 'An enemy loved' );
INSERT INTO plots (item) VALUES ( 'Ambition' );
INSERT INTO plots (item) VALUES ( 'Conflict with a god' );
INSERT INTO plots (item) VALUES ( 'Mistaken jealousy' );
INSERT INTO plots (item) VALUES ( 'Erroneous judgment' );
INSERT INTO plots (item) VALUES ( 'Remorse' );
INSERT INTO plots (item) VALUES ( 'Recovery of a lost one' );
INSERT INTO plots (item) VALUES ( 'Loss of loved ones' );
INSERT INTO plots (item) VALUES ( 'Overcoming the Monster' );
INSERT INTO plots (item) VALUES ( 'Rags to Riches' );
INSERT INTO plots (item) VALUES ( 'The Quest' );
INSERT INTO plots (item) VALUES ( 'Voyage and Return' );
INSERT INTO plots (item) VALUES ( 'Comedy' );
INSERT INTO plots (item) VALUES ( 'Tragedy' );
INSERT INTO plots (item) VALUES ( 'Rebirth' );
INSERT INTO plots (item) VALUES ( 'Precursors' );
END;
