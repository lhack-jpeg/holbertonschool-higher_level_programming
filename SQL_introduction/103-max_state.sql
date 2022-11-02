 -- Task 20: Temperatures #2
 -- Return the max temperature by state order alphabetically
 SELECT
	state,
	MAX(value) as 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state;
