#
# objecttier
#
# Builds objects from data retrieved through the data tier.
#
# Original author: Prof. Joe Hummel
#
import datatier
#
# do not import other modules
# Code by Rahin Jain (665219123) rjain56

########################################################
#
# Station:
#
# Constructor(...)
# Properties:
#   Station_ID: int
#   Station_Name: string
#   Ridership: int
#   Percent_Ridership: float
#
class Station:

   def __init__(self, Station_ID, Station_Name, Ridership, Percent_Ridership):
      self._Station_ID = Station_ID
      self._Station_Name = Station_Name
      self._Ridership = Ridership
      self._Percent_Ridership = Percent_Ridership


   @property
   def Station_ID(self):
      return self._Station_ID

   @property
   def Station_Name(self):
      return self._Station_Name

   @property
   def Ridership(self):
      return self._Ridership

   @property
   def Percent_Ridership(self):
      return self._Percent_Ridership




########################################################
#
# Stop:
#
# Constructor(...)
# Properties:
#   Stop_ID: int
#   Stop_Name: string
#   Direction: string
#   Accessible: boolean (True/False)
#   Latitude: float
#   Longitude: float
#   Lines: list of strings
#
class Stop:

   def __init__(self, Stop_ID, Stop_Name, Accessible, Direction, Lines, Latitude, Longitude):
      self._Stop_ID = Stop_ID
      self._Stop_Name = Stop_Name
      self._Accessible = Accessible
      self._Direction = Direction
      self._Lines = Lines
      self._Latitude = Latitude
      self._Longitude = Longitude

   @property
   def Stop_ID(self):
      return self._Stop_ID

   @property
   def Stop_Name(self):
      return self._Stop_Name

   @property
   def Accessible(self):
      return self._Accessible

   @property
   def Direction(self):
      return self._Direction

   @property
   def Lines(self):
      return self._Lines

   @property
   def Latitude(self):
      return self._Latitude

   @property
   def Longitude(self):
      return self._Longitude

########################################################
#
# get_stations:
#
# gets and returns all stations whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of stations in ascending order by name;
#          returns None if an error occurs.
#
def get_stations(dbConn, pattern):

   sql = (
      "select stations.station_id, station_name, sum(num_riders) " 
      "from stations join ridership on ridership.station_id == stations.station_id "
      "where station_name like ? "
      "group by station_name "
      "order by station_name asc;"
   )

   datatier_stations = datatier.select_n_rows(dbConn, sql, [pattern])

   sql = (
      "select sum(num_riders) "
      "from ridership;"
   )

   total = (datatier.select_one_row(dbConn, sql, []))[0]
   list_stations = []

   if len(datatier_stations) == 0:
      return list_stations

   for row in datatier_stations:
      percent = (int(row[2])/int(total)) * 100
      obj = Station(row[0], row[1], row[2], percent)
      list_stations.append(obj)

   return list_stations


########################################################
#
# get_stops:
#
# gets and returns all stops at a given station; the 
# given station name must match exactly (no wildcards).
# If there is no match, an empty list is returned.
#
# Returns: a list of stops in ascending order by name,
#          then in ascending order by id if two stops
#          have the same name; returns None if an error
#          occurs.
#
def get_stops(dbConn, name):

   sql = (
      "select stops.stop_id, stop_name, ada, direction, group_concat(color), latitude, longitude "
      "from stops join stopdetails on stopdetails.stop_id == stops.stop_id "
      "join Stations on Stations.Station_ID == stops.Station_ID "
      "join lines on lines.line_ID == stopdetails.Line_ID "
      "where station_name == ? "
      "group by stops.stop_id "
      "order by stop_name ASC, stops.stop_id ASC;"
   )

   datatier_stops = datatier.select_n_rows(dbConn, sql, [name])
   list_of_stops= []

   for row in datatier_stops:
      obj = Stop(row[0], row[1], row[2], row[3], sorted(row[4].split(",")), row[5], row[6])
      list_of_stops.append(obj)

   return list_of_stops
