-- Task 9: Cities by States
-- Return a list of ordered cities and included state name
SELECT
	cities.id AS id,
	name,
	states.name AS name
from cities
JOIN states;
