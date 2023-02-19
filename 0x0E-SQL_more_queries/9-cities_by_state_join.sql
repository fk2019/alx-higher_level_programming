-- list all cities contained in db hbtn_0d_usa
-- display ctiies.id, cities.name, states.name
-- results sorted in ascending order
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states ON cities.id = states.id
ORDER BY id;
