#
# Name: Rahin Jain
# UIN: 665219123
#
#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier  # Importing datatier to handle database interactions

##################################################################
#
# Lobbyist:
#
# This class represents a basic Lobbyist with identifying information
# such as ID, first and last names, and phone number.
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int        # Unique identifier for the lobbyist
#   First_Name: string      # Lobbyist's first name
#   Last_Name: string       # Lobbyist's last name
#   Phone: string           # Lobbyist's contact number
#
class Lobbyist:

   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      # Initializing the lobbyist's attributes
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   # Property to get the lobbyist ID
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   # Property to get the first name
   @property
   def First_Name(self):
      return self._First_Name

   # Property to get the last name
   @property
   def Last_Name(self):
      return self._Last_Name

   # Property to get the phone number
   @property
   def Phone(self):
      return self._Phone

##################################################################
#
# LobbyistDetails:
#
# This class represents a lobbyist in more detail, including full
# contact information, employment history, and compensation.
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int                  # Unique identifier for the lobbyist
#   Salutation: string                # Title or salutation (e.g., Mr., Ms.)
#   First_Name: string                # First name
#   Middle_Initial: string            # Middle initial (if any)
#   Last_Name: string                 # Last name
#   Suffix: string                    # Suffix (e.g., Jr., Sr.)
#   Address_1: string                 # Primary address line
#   Address_2: string                 # Secondary address line (if any)
#   City: string                      # City of residence
#   State_Initial: string             # State abbreviation (e.g., IL for Illinois)
#   Zip_Code: string                  # Postal code
#   Country: string                   # Country of residence
#   Email: string                     # Email address
#   Phone: string                     # Contact phone number
#   Fax: string                       # Fax number (if any)
#   Years_Registered: list of years   # List of years the lobbyist was registered
#   Employers: list of employer names # List of employers
#   Total_Compensation: float         # Total compensation received
#
class LobbyistDetails:

   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial,
                Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code,
                Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
      # Initializing all details related to a lobbyist
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = Years_Registered
      self._Employers = Employers
      self._Total_Compensation = Total_Compensation

   # Getters for all properties
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation


##################################################################
#
# LobbyistClients:
#
# This class represents a lobbyist along with their total
# compensation and associated clients.
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int                # Unique identifier for the lobbyist
#   First_Name: string              # First name
#   Last_Name: string               # Last name
#   Phone: string                   # Contact number
#   Total_Compensation: float       # Total compensation the lobbyist has earned
#   Clients: list of clients        # List of associated clients
#
class LobbyistClients:

   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
      # Initializing the lobbyist's details, including compensation and clients
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   # Getters for all properties
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients


##################################################################
#
# num_lobbyists:
#
# Returns the total number of lobbyists in the database.
# Returns -1 if an error occurs (e.g., if the db connection is None).
#
def num_lobbyists(dbConn):

   if dbConn == None:
      return -1  # Return -1 if database connection is None

   q = """select count(lobbyist_id) 
          from LobbyistInfo;"""

   data = datatier.select_one_row(dbConn, q)

   if data == None:
      return -1  # Return -1 if the query failed

   return data[0]  # Return the count of lobbyists


##################################################################
#
# num_employers:
#
# Returns the total number of employers in the database.
# Returns -1 if an error occurs.
#
def num_employers(dbConn):

   q = """select count(employer_id) 
          from EmployerInfo;"""

   data = datatier.select_one_row(dbConn, q)

   if data == None:
      return -1  # Return -1 if the query failed

   return data[0]  # Return the count of employers

##################################################################
#
# num_clients:
#
# Returns the total number of clients in the database.
# Returns -1 if an error occurs.
#
def num_clients(dbConn):

   q = """select count(client_id) 
          from ClientInfo;"""

   data = datatier.select_one_row(dbConn, q)

   if data == None:
      return -1  # Return -1 if the query failed

   return data[0]  # Return the count of clients


##################################################################
#
# get_lobbyists:
#
# Gets and returns all lobbyists whose first or last name are "like"
# the pattern provided. The pattern uses SQL wildcard characters:
# - _ matches a single character
# - % matches zero or more characters.
#
# Returns: a list of Lobbyist objects in ascending order by ID.
#          If no data is retrieved or an error occurs, an empty
#          list is returned.
#
def get_lobbyists(dbConn, pattern):
   listobj = []  # Initialize an empty list to store Lobbyist objects

   q = (
      "select lobbyist_ID, First_Name, Last_Name, Phone "
      "from LobbyistInfo "
      "where First_Name like ? or Last_name like ? "
      "order by Lobbyist_ID ASC;"
   )  # SQL query to search for lobbyists based on the pattern

   data = datatier.select_n_rows(dbConn, q, [pattern, pattern])  # Retrieve multiple rows from the database

   if data == None:
      return []  # Return an empty list if the query failed

   # Loop through each row in the data and create Lobbyist objects
   for rows in data:
      item = Lobbyist(rows[0], rows[1], rows[2], rows[3])  # Create a Lobbyist object from the row data
      listobj.append(item)  # Add the Lobbyist object to the list

   return listobj  # Return the list of lobbyists


##################################################################
#
# get_lobbyist_details:
#
# Gets and returns detailed information about the given lobbyist
# using the lobbyist ID.
#
# Returns: a LobbyistDetails object if the lobbyist is found. If
#          the search fails or an error occurs, None is returned.
#
def get_lobbyist_details(dbConn, lobbyist_id):
   # Query to get all information about the lobbyist from the LobbyistInfo table
   q = (
      "select * "
      "from LobbyistInfo "
      "where Lobbyist_ID == ?;"
   )

   lobbyist_info_from_db = datatier.select_one_row(dbConn, q, [lobbyist_id])  # Retrieve one row of data

   # If no data is found or an error occurs, return None
   if lobbyist_info_from_db == None or len(lobbyist_info_from_db) == 0:
      return None

   # Query to get the list of years the lobbyist was registered
   q = (
      "select year "
      "from LobbyistYears "
      "where Lobbyist_ID == ?;"
   )

   year_from_db = datatier.select_n_rows(dbConn, q, [lobbyist_id])  # Retrieve the years of registration

   # Query to get the list of employers the lobbyist worked with
   q = (
      "select distinct Employer_Name "
      "from EmployerInfo "
      "join LobbyistAndEmployer on EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID "
      "where Lobbyist_ID = ? "
      "order by Employer_Name;"
   )

   employer_name_from_db = datatier.select_n_rows(dbConn, q, [lobbyist_id])  # Retrieve employer names

   # Query to get the total compensation received by the lobbyist
   q = (
      "select Sum(Compensation_Amount) "
      "from Compensation "
      "where Lobbyist_ID == ?;"
   )

   total_compensation = datatier.select_one_row(dbConn, q, [lobbyist_id])  # Retrieve the sum of compensation

   # Convert the list of years to a simple list
   list_years = []
   for row in year_from_db:
      list_years.append(row[0])

   # Convert the list of employers to a simple list
   list_employers = []
   for row in employer_name_from_db:
      list_employers.append(row[0])

   # Set the total compensation, or set it to 0 if the value is None
   if total_compensation and total_compensation[0] is not None:
      total_compensation = total_compensation[0]
   else:
      total_compensation = 0

   # Create a LobbyistDetails object with the retrieved data
   obj = LobbyistDetails(*lobbyist_info_from_db, list_years, list_employers, total_compensation)

   return obj  # Return the LobbyistDetails object


##################################################################
#
# get_top_N_lobbyists:
#
# Gets and returns the top N lobbyists based on their total
# compensation for a given year.
#
# Returns: a list of 0 or more LobbyistClients objects. If the
#          year is invalid or an error occurs, an empty list is
#          returned.
#
def get_top_N_lobbyists(dbConn, N, year):
   # Query to get the top N lobbyists based on their total compensation in the given year
   q = """
         select LobbyistInfo.Lobbyist_ID, First_Name, Last_Name, Phone, Sum(Compensation_Amount)
         from LobbyistInfo
         join Compensation on compensation.Lobbyist_ID == LobbyistInfo.Lobbyist_ID
         where strftime("%Y", Period_End) = ?
         group by compensation.Lobbyist_ID
         order by Sum(Compensation_Amount) desc
         limit ?;
      """

   data = datatier.select_n_rows(dbConn, q, [year, N])  # Retrieve the top N lobbyists based on the query
   listobj = []  # Initialize an empty list to store LobbyistClients objects

   if data == None:
      return None  # Return None if the query failed

   # Loop through each lobbyist in the result
   for row in data:

      # Query to get the list of clients the lobbyist worked with during the specified year
      q = """
         select distinct (ClientInfo.Client_ID), Client_Name
         from ClientInfo
         join Compensation on compensation.Client_ID == ClientInfo.Client_ID
         where strftime("%Y", Period_End) = ? and Lobbyist_ID = ?
         order by Client_Name asc;
      """

      data_client = datatier.select_n_rows(dbConn, q, [year, row[0]])  # Retrieve client names for the lobbyist
      list_data_client = []  # Initialize an empty list to store client names

      # Loop through the client data and add client names to the list
      for d in data_client:
         list_data_client.append(d[1])

      # Create a LobbyistClients object with the lobbyist's info and associated clients
      obj = LobbyistClients(row[0], row[1], row[2], row[3], row[4], list_data_client)
      listobj.append(obj)  # Add the LobbyistClients object to the list

   return listobj  # Return the list of top N lobbyists


##################################################################
#
# add_lobbyist_year:
#
# Inserts a new year of registration into the database for a given
# lobbyist. It checks whether the lobbyist exists first before
# inserting the year.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g., if the lobbyist does not exist).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   # Query to check if the lobbyist exists in the database
   q = """
               select count() 
               from LobbyistInfo 
               where lobbyist_id=?;
            """

   data = datatier.select_one_row(dbConn, q, (lobbyist_id,))

   # If the lobbyist doesn't exist, return 0
   if data[0] <= 0:
      return 0

   else:
      # Insert the new year for the lobbyist into the LobbyistYears table
      q = f"insert into lobbyistyears(lobbyist_id,year) values (?,?);"
      datatier.perform_action(dbConn, q, (lobbyist_id, year))  # Perform the insert action
      return 1  # Return 1 indicating success


##################################################################
#
# set_salutation:
#
# Updates the salutation for a given lobbyist. If the lobbyist
# already has a salutation, it is replaced by the new value.
# Passing an empty string as a salutation will delete the current
# salutation. The function first checks if the lobbyist exists.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g., if the lobbyist does not exist).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   # SQL query to update the salutation for the specified lobbyist
   q = """
         update LobbyistInfo set Salutation = ?
         where Lobbyist_ID = ?;
      """

   data = datatier.perform_action(dbConn, q, [salutation, lobbyist_id])  # Execute the update action

   if data == -1 or data == 0:
      return 0  # Return 0 if an error occurred or the update failed

   return 1  # Return 1 indicating the salutation was successfully updated
