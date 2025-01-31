SELECT DATE(ride_date), SUM(num_riders) FROM ridership
WHERE (strftime('%m-%d', ride_date) = '12-25' AND strftime('%Y', ride_date) BETWEEN '2010' AND '2020')
GROUP BY ride_date
ORDER BY ride_date DESC;
