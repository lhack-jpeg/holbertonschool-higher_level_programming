-- TASK 19: Temperatures #1
-- Return the top 3 rows during the motnhs of July and August, ordered by temperature decs
SELECT
	city,
	avg(value) as 'avg_temp'
FROM temperatures
WHERE `month` BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
