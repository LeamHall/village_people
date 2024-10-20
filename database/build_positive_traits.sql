-- name:    build_positive_traits.sql
-- version: 0.0.1
-- date:    20241020
-- author:  Leam Hall
-- desc:    Create a positive traits table.

.headers    on
.nullvalue  [NULL]
.echo       on

-- Schema
DROP TABLE IF EXISTS positive_traits;

CREATE TABLE positive_traits (
  idx   INTEGER NOT NULL PRIMARY KEY,
  item  TEXT
);

-- Data
BEGIN DEFERRED;
INSERT INTO positive_traits (item) VALUES ( 'Adaptable' );
INSERT INTO positive_traits (item) VALUES ( 'Adventurous' );
INSERT INTO positive_traits (item) VALUES ( 'Affectionate' );
INSERT INTO positive_traits (item) VALUES ( 'Alert' );
INSERT INTO positive_traits (item) VALUES ( 'Ambitious' );
INSERT INTO positive_traits (item) VALUES ( 'Analytical' );
INSERT INTO positive_traits (item) VALUES ( 'Appreciative' );
INSERT INTO positive_traits (item) VALUES ( 'Bold' );
INSERT INTO positive_traits (item) VALUES ( 'Calm' );
INSERT INTO positive_traits (item) VALUES ( 'Cautious' );
INSERT INTO positive_traits (item) VALUES ( 'Centered' );
INSERT INTO positive_traits (item) VALUES ( 'Charming' );
INSERT INTO positive_traits (item) VALUES ( 'Confident' );
INSERT INTO positive_traits (item) VALUES ( 'Cooperative' );
INSERT INTO positive_traits (item) VALUES ( 'Courageous' );
INSERT INTO positive_traits (item) VALUES ( 'Courteous' );
INSERT INTO positive_traits (item) VALUES ( 'Creative' );
INSERT INTO positive_traits (item) VALUES ( 'Curious' );
INSERT INTO positive_traits (item) VALUES ( 'Decisive' );
INSERT INTO positive_traits (item) VALUES ( 'Diplomatic' );
INSERT INTO positive_traits (item) VALUES ( 'Disciplined' );
INSERT INTO positive_traits (item) VALUES ( 'Discreet' );
INSERT INTO positive_traits (item) VALUES ( 'Easygoing' );
INSERT INTO positive_traits (item) VALUES ( 'Efficient' );
INSERT INTO positive_traits (item) VALUES ( 'Empathetic' );
INSERT INTO positive_traits (item) VALUES ( 'Enthusiastic' );
INSERT INTO positive_traits (item) VALUES ( 'Extroverted' );
INSERT INTO positive_traits (item) VALUES ( 'Flamboyant' );
INSERT INTO positive_traits (item) VALUES ( 'Flirtatious' );
INSERT INTO positive_traits (item) VALUES ( 'Focused' );
INSERT INTO positive_traits (item) VALUES ( 'Friendly' );
INSERT INTO positive_traits (item) VALUES ( 'Funny' );
INSERT INTO positive_traits (item) VALUES ( 'Generous' );
INSERT INTO positive_traits (item) VALUES ( 'Gentle' );
INSERT INTO positive_traits (item) VALUES ( 'Happy' );
INSERT INTO positive_traits (item) VALUES ( 'Honest' );
INSERT INTO positive_traits (item) VALUES ( 'Honorable' );
INSERT INTO positive_traits (item) VALUES ( 'Hospitable' );
INSERT INTO positive_traits (item) VALUES ( 'Humble' );
INSERT INTO positive_traits (item) VALUES ( 'Idealistic' );
INSERT INTO positive_traits (item) VALUES ( 'Imaginative' );
INSERT INTO positive_traits (item) VALUES ( 'Independent' );
INSERT INTO positive_traits (item) VALUES ( 'Industrious' );
INSERT INTO positive_traits (item) VALUES ( 'Innocent' );
INSERT INTO positive_traits (item) VALUES ( 'Inspirational' );
INSERT INTO positive_traits (item) VALUES ( 'Intelligent' );
INSERT INTO positive_traits (item) VALUES ( 'Introverted' );
INSERT INTO positive_traits (item) VALUES ( 'Just' );
INSERT INTO positive_traits (item) VALUES ( 'Kind' );
INSERT INTO positive_traits (item) VALUES ( 'Loyal' );
INSERT INTO positive_traits (item) VALUES ( 'Mature' );
INSERT INTO positive_traits (item) VALUES ( 'Merciful' );
INSERT INTO positive_traits (item) VALUES ( 'Meticulous' );
INSERT INTO positive_traits (item) VALUES ( 'Nature-focused' );
INSERT INTO positive_traits (item) VALUES ( 'Nurturing' );
INSERT INTO positive_traits (item) VALUES ( 'Obedient' );
INSERT INTO positive_traits (item) VALUES ( 'Objective' );
INSERT INTO positive_traits (item) VALUES ( 'Observant' );
INSERT INTO positive_traits (item) VALUES ( 'Optimistic' );
INSERT INTO positive_traits (item) VALUES ( 'Organized' );
INSERT INTO positive_traits (item) VALUES ( 'Passionate' );
INSERT INTO positive_traits (item) VALUES ( 'Patient' );
INSERT INTO positive_traits (item) VALUES ( 'Patriotic' );
INSERT INTO positive_traits (item) VALUES ( 'Pensive' );
INSERT INTO positive_traits (item) VALUES ( 'Perceptive' );
INSERT INTO positive_traits (item) VALUES ( 'Persuasive' );
INSERT INTO positive_traits (item) VALUES ( 'Philosophical' );
INSERT INTO positive_traits (item) VALUES ( 'Playful' );
INSERT INTO positive_traits (item) VALUES ( 'Private' );
INSERT INTO positive_traits (item) VALUES ( 'Proactive' );
INSERT INTO positive_traits (item) VALUES ( 'Professional' );
INSERT INTO positive_traits (item) VALUES ( 'Proper' );
INSERT INTO positive_traits (item) VALUES ( 'Protective' );
INSERT INTO positive_traits (item) VALUES ( 'Quirky' );
INSERT INTO positive_traits (item) VALUES ( 'Resourceful' );
INSERT INTO positive_traits (item) VALUES ( 'Responsible' );
INSERT INTO positive_traits (item) VALUES ( 'Sensible' );
INSERT INTO positive_traits (item) VALUES ( 'Sensual' );
INSERT INTO positive_traits (item) VALUES ( 'Sentimental' );
INSERT INTO positive_traits (item) VALUES ( 'Simple' );
INSERT INTO positive_traits (item) VALUES ( 'Socially Aware' );
INSERT INTO positive_traits (item) VALUES ( 'Aware' );
INSERT INTO positive_traits (item) VALUES ( 'Sophisticated' );
INSERT INTO positive_traits (item) VALUES ( 'Spiritual' );
INSERT INTO positive_traits (item) VALUES ( 'Spontaneous' );
INSERT INTO positive_traits (item) VALUES ( 'Spunky' );
INSERT INTO positive_traits (item) VALUES ( 'Studious' );
INSERT INTO positive_traits (item) VALUES ( 'Supportive' );
INSERT INTO positive_traits (item) VALUES ( 'Talented' );
INSERT INTO positive_traits (item) VALUES ( 'Thrifty' );
INSERT INTO positive_traits (item) VALUES ( 'Tolerant' );
INSERT INTO positive_traits (item) VALUES ( 'Traditional' );
INSERT INTO positive_traits (item) VALUES ( 'Trusting' );
INSERT INTO positive_traits (item) VALUES ( 'Uninhibited' );
INSERT INTO positive_traits (item) VALUES ( 'Unselfish' );
INSERT INTO positive_traits (item) VALUES ( 'Whimsical' );
INSERT INTO positive_traits (item) VALUES ( 'Wholesome' );
INSERT INTO positive_traits (item) VALUES ( 'Wise' );
INSERT INTO positive_traits (item) VALUES ( 'Witty' );
END;

