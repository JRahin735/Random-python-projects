SELECT DATE(ride_date) AS dates, SUM(num_riders) AS everyone
FROM ridership
GROUP BY dates
ORDER BY everyone ASC
LIMIT 1;