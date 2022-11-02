-- Task 9: Cities by States
-- Return a list of ordered cities and included state name
SELECT
	cities.id,
	cities.name,
	states.name
from cities
LEFT JOIN states ON states.id = cities.state_id;
