-- Task 10: List by the best
-- Script to display in DESC order score and name
SELECT
	score,
	name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
