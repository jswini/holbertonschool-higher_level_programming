-- this script displays score and number of times it appears in table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
