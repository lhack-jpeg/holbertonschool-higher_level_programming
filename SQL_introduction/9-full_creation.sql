-- Task 9: Full Creation
-- Script should create a new table in the database if it does not exist
CREATE TABLE IF NOT EXISTS second_table
(
	id INT,
	name VARCHAR(256),
	score INT

);

INSERT INTO second_table (id, name, score)
       VALUES
       (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);
