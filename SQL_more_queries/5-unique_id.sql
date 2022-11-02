-- Task 5: Unique id
-- Create table unique_id with the id DEFAULT 1 and unique
CREATE TABLE IF NOT EXISTS `unique_id`
(
	id INT DEFAULT(1) UNIQUE,
	name VARCHAR(256)
);
