SELECT SUM(Num_Riders) 
FROM ridership
WHERE Station_ID = (SELECT Station_ID FROM stations WHERE Station_Name = 'O''Hare Airport') AND strftime('%Y', Ride_Date) = '2019';

SELECT SUM(Num_Riders) 
FROM ridership
WHERE Station_ID = (SELECT Station_ID FROM stations WHERE Station_Name = 'O''Hare Airport') AND strftime('%Y', Ride_Date) = '2020';