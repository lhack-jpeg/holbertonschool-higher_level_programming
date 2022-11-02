-- Task 18: Temperatures #0
-- Return the rows of the avberage temperature of the cities order by temp DESC
SELECT
	city,
	avg(value) as 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
