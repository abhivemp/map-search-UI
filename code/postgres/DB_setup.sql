
-- Setting Up DB
-- Code by Yash Dhayal

-- Creating DB
CREATE DATABASE Project;

-- Tables
-- Creating Content table
CREATE TABLE CONTENT (
Content_id	SERIAL		PRIMARY KEY,
Author		VARCHAR(20)	NOT NULL,	-- Author last name
Title		TEXT			NOT NULL,	-- Title of content
Posting_date	DATE			NOT NULL,	-- Date content is posted
Location	VARCHAR(20)	NOT NULL,	-- County relevant to content
Category	VARCHAR(20)	NOT NULL,	-- Category of the content
Data		TEXT			NOT NULL	-- Link to the content
);

-- Creating Multimedia table
CREATE TABLE MM(
	Playtime	TIME
) INHERITS (CONTENT);

-- Creating Article table. Will only go into this if inserted data is considered article
CREATE TABLE ARTICLE( 	) INHERITS (CONTENT);


-- Filling tables
-- Transferring data from a CSV file to Article Table
COPY ARTICLE(Content_id, Author, Title, Posting_date, Location, Category, Data) 
FROM '/home/osc/Desktop/Project/article.csv' DELIMITER ',' CSV HEADER;

-- Transferring data from a CSV file to MM Table
COPY MM(Content_id, Author, Title, Posting_date, Location, Category, Data, playtime) 
FROM '/home/osc/Desktop/Project/multimedia.csv' DELIMITER ',' CSV HEADER;


-- Views
-- PieTags view contains categories and the count of each category
CREATE VIEW PieTags AS
SELECT category, COUNT(category)
FROM CONTENT
GROUP BY category;
