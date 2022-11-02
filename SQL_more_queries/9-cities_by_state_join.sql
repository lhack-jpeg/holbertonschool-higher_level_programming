-- Task 9: Cities by States
-- Return a list of ordered cities and included state name
SELECT
	cities.id as id,
	name,
	states.name as name
from cities
LEFT JOIN states on cities.state_id = states.id
ORDER BY cities.id;
