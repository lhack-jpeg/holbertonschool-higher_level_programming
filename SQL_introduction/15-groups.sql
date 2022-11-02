-- Task 15: Number by score
-- Returns the score and count of scores
SELECT
	score,
	COUNT(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY 'number' DESC;
