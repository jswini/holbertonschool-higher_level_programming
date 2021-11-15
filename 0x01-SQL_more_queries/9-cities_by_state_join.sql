-- This script uses join to output results from 2 tables
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON states.id = cities.state_id;
