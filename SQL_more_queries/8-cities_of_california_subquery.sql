-- Task 8: Cities of California
-- Select all cities form the state of California
SELECT
	id,
	name
FROM cities
WHERE state_id = 1
ORDER BY id ASC;
