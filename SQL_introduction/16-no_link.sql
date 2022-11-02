-- Task 16: Say my name.
-- Returns rows that contain a name value. Ordered by score DESC
SELECT
	score,
	name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
