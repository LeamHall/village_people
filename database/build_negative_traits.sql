-- name:    build_negative_traits.sql
-- version: 0.0.1
-- date:    20241020
-- author:  Leam Hall
-- desc:    Create a negative traits table.

.headers    on
.nullvalue  [NULL]
.echo       on

-- Schema
DROP TABLE IF EXISTS negative_traits;

CREATE TABLE negative_traits (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);

-- Data
BEGIN DEFERRED;
INSERT INTO negative_traits (item) VALUES ( 'Abrasive' );
INSERT INTO negative_traits (item) VALUES ( 'Addictive' );
INSERT INTO negative_traits (item) VALUES ( 'Antisocial' );
INSERT INTO negative_traits (item) VALUES ( 'Apathetic' );
INSERT INTO negative_traits (item) VALUES ( 'Callous' );
INSERT INTO negative_traits (item) VALUES ( 'Catty' );
INSERT INTO negative_traits (item) VALUES ( 'Childish' );
INSERT INTO negative_traits (item) VALUES ( 'Cocky' );
INSERT INTO negative_traits (item) VALUES ( 'Compulsive' );
INSERT INTO negative_traits (item) VALUES ( 'Confrontational' );
INSERT INTO negative_traits (item) VALUES ( 'Controlling' );
INSERT INTO negative_traits (item) VALUES ( 'Cowardly' );
INSERT INTO negative_traits (item) VALUES ( 'Cruel' );
INSERT INTO negative_traits (item) VALUES ( 'Cynical' );
INSERT INTO negative_traits (item) VALUES ( 'Defensive' );
INSERT INTO negative_traits (item) VALUES ( 'Devious' );
INSERT INTO negative_traits (item) VALUES ( 'Dishonest' );
INSERT INTO negative_traits (item) VALUES ( 'Disloyal' );
INSERT INTO negative_traits (item) VALUES ( 'Disorganized' );
INSERT INTO negative_traits (item) VALUES ( 'Disrespectful' );
INSERT INTO negative_traits (item) VALUES ( 'Evasive' );
INSERT INTO negative_traits (item) VALUES ( 'Evil' );
INSERT INTO negative_traits (item) VALUES ( 'Extravagant' );
INSERT INTO negative_traits (item) VALUES ( 'Fanatical' );
INSERT INTO negative_traits (item) VALUES ( 'Flaky' );
INSERT INTO negative_traits (item) VALUES ( 'Foolish' );
INSERT INTO negative_traits (item) VALUES ( 'Forgetful' );
INSERT INTO negative_traits (item) VALUES ( 'Frivolous' );
INSERT INTO negative_traits (item) VALUES ( 'Fussy' );
INSERT INTO negative_traits (item) VALUES ( 'Gossipy' );
INSERT INTO negative_traits (item) VALUES ( 'Greedy' );
INSERT INTO negative_traits (item) VALUES ( 'Grumpy' );
INSERT INTO negative_traits (item) VALUES ( 'Gullible' );
INSERT INTO negative_traits (item) VALUES ( 'Haughty' );
INSERT INTO negative_traits (item) VALUES ( 'Hostile' );
INSERT INTO negative_traits (item) VALUES ( 'Humorless' );
INSERT INTO negative_traits (item) VALUES ( 'Hypocritical' );
INSERT INTO negative_traits (item) VALUES ( 'Ignorant' );
INSERT INTO negative_traits (item) VALUES ( 'Impatient' );
INSERT INTO negative_traits (item) VALUES ( 'Impulsive' );
INSERT INTO negative_traits (item) VALUES ( 'Inattentive' );
INSERT INTO negative_traits (item) VALUES ( 'Indecisive' );
INSERT INTO negative_traits (item) VALUES ( 'Inflexible' );
INSERT INTO negative_traits (item) VALUES ( 'Inhibited' );
INSERT INTO negative_traits (item) VALUES ( 'Insecure' );
INSERT INTO negative_traits (item) VALUES ( 'Irrational' );
INSERT INTO negative_traits (item) VALUES ( 'Irresponsible' );
INSERT INTO negative_traits (item) VALUES ( 'Jealous' );
INSERT INTO negative_traits (item) VALUES ( 'Judgmental' );
INSERT INTO negative_traits (item) VALUES ( 'Know It All' );
INSERT INTO negative_traits (item) VALUES ( 'It' );
INSERT INTO negative_traits (item) VALUES ( 'All' );
INSERT INTO negative_traits (item) VALUES ( 'Lazy' );
INSERT INTO negative_traits (item) VALUES ( 'Macho' );
INSERT INTO negative_traits (item) VALUES ( 'Manipulative' );
INSERT INTO negative_traits (item) VALUES ( 'Martyr' );
INSERT INTO negative_traits (item) VALUES ( 'Materialistic' );
INSERT INTO negative_traits (item) VALUES ( 'Melodramatic' );
INSERT INTO negative_traits (item) VALUES ( 'Mischievous' );
INSERT INTO negative_traits (item) VALUES ( 'Morbid' );
INSERT INTO negative_traits (item) VALUES ( 'Nagging' );
INSERT INTO negative_traits (item) VALUES ( 'Needy' );
INSERT INTO negative_traits (item) VALUES ( 'Nervous' );
INSERT INTO negative_traits (item) VALUES ( 'Nosy' );
INSERT INTO negative_traits (item) VALUES ( 'Obsessive' );
INSERT INTO negative_traits (item) VALUES ( 'Oversensitive' );
INSERT INTO negative_traits (item) VALUES ( 'Paranoid' );
INSERT INTO negative_traits (item) VALUES ( 'Perfectionist' );
INSERT INTO negative_traits (item) VALUES ( 'Pessimistic' );
INSERT INTO negative_traits (item) VALUES ( 'Possessive' );
INSERT INTO negative_traits (item) VALUES ( 'Prejudiced' );
INSERT INTO negative_traits (item) VALUES ( 'Pretentious' );
INSERT INTO negative_traits (item) VALUES ( 'Promiscuous' );
INSERT INTO negative_traits (item) VALUES ( 'Pushy' );
INSERT INTO negative_traits (item) VALUES ( 'Rebellious' );
INSERT INTO negative_traits (item) VALUES ( 'Reckless' );
INSERT INTO negative_traits (item) VALUES ( 'Resentful' );
INSERT INTO negative_traits (item) VALUES ( 'Rowdy' );
INSERT INTO negative_traits (item) VALUES ( 'Scatterbrained' );
INSERT INTO negative_traits (item) VALUES ( 'Self-destructive' );
INSERT INTO negative_traits (item) VALUES ( 'Self-indulgent' );
INSERT INTO negative_traits (item) VALUES ( 'Selfish' );
INSERT INTO negative_traits (item) VALUES ( 'Sleazy' );
INSERT INTO negative_traits (item) VALUES ( 'Spoiled' );
INSERT INTO negative_traits (item) VALUES ( 'Stingy' );
INSERT INTO negative_traits (item) VALUES ( 'Stubborn' );
INSERT INTO negative_traits (item) VALUES ( 'Subservient' );
INSERT INTO negative_traits (item) VALUES ( 'Superstitious' );
INSERT INTO negative_traits (item) VALUES ( 'Tactless' );
INSERT INTO negative_traits (item) VALUES ( 'Temperamental' );
INSERT INTO negative_traits (item) VALUES ( 'Timid' );
INSERT INTO negative_traits (item) VALUES ( 'Uncommunicative' );
INSERT INTO negative_traits (item) VALUES ( 'Uncouth' );
INSERT INTO negative_traits (item) VALUES ( 'Unethical' );
INSERT INTO negative_traits (item) VALUES ( 'Ungrateful' );
INSERT INTO negative_traits (item) VALUES ( 'Unintelligent' );
INSERT INTO negative_traits (item) VALUES ( 'Vain' );
INSERT INTO negative_traits (item) VALUES ( 'Verbose' );
INSERT INTO negative_traits (item) VALUES ( 'Vindictive' );
INSERT INTO negative_traits (item) VALUES ( 'Violent' );
INSERT INTO negative_traits (item) VALUES ( 'Volatile' );
INSERT INTO negative_traits (item) VALUES ( 'Weak-willed' );
INSERT INTO negative_traits (item) VALUES ( 'Whiny' );
INSERT INTO negative_traits (item) VALUES ( 'Withdrawn' );
INSERT INTO negative_traits (item) VALUES ( 'Workaholic' );
INSERT INTO negative_traits (item) VALUES ( 'Worrywart' );
END;

