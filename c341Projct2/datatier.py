# Rahin Jain - rjain56@uic.edu - 665219123
#
# datatier.py
#
# This module contains functions for executing SQL queries
# against a given SQLite database.
#
# Original author: Prof. Joe Hummel, Ellen Kidane
#
import sqlite3  # Importing SQLite to interact with the SQLite database


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL SELECT query, this function
# executes the query and returns the first row retrieved.
# If no row is retrieved, it returns an empty tuple ().
#
# The function supports parameterized queries, and the parameters
# can be passed as a list (this is optional).
#
# Returns: the first row of data retrieved, or an empty tuple ()
# if no data was retrieved. In case of an error, a message is
# printed and None is returned.
#
def select_one_row(dbConn, sql, parameters=None):
    if parameters == None:
        parameters = []  # Initialize parameters to an empty list if none are provided
    DbCursor = dbConn.cursor()  # Create a cursor to execute the SQL query

    try:
        DbCursor.execute(sql, parameters)  # Execute the SQL query with the provided parameters
        data = DbCursor.fetchone()  # Fetch the first row of the result

        if data != None:
            return data  # Return the retrieved row if not None
        else:
            return ()  # Return an empty tuple if no data was retrieved

    except Exception as error:
        # Catch any exceptions and print an error message
        print("select_one_row func failed:", error)
        return None  # Return None if an error occurred

    finally:
        # Always close the cursor after executing the query
        DbCursor.close()


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL SELECT query, this function
# executes the query and returns a list of rows retrieved. If no
# rows are retrieved, an empty list [] is returned.
#
# The function supports parameterized queries, and the parameters
# can be passed as a list (this is optional).
#
# Returns: a list of rows retrieved by the query. If an error occurs,
# a message is printed and None is returned.
#
def select_n_rows(dbConn, sql, parameters=None):
    if parameters == None:
        parameters = []  # Initialize parameters to an empty list if none are provided

    DbCursor = dbConn.cursor()  # Create a cursor to execute the SQL query

    try:
        DbCursor.execute(sql, parameters)  # Execute the SQL query with the provided parameters
        data_listed = DbCursor.fetchall()  # Fetch all rows of the result
        return data_listed  # Return the list of rows

    except Exception as error:
        # Catch any exceptions and print an error message
        print("select_n_rows failed:", error)
        return None  # Return None if an error occurred

    finally:
        # Always close the cursor after executing the query
        DbCursor.close()


##################################################################
#
# perform_action:
#
# Given a database connection and a SQL action query (e.g., INSERT,
# UPDATE, DELETE), this function executes the query and returns the
# number of rows modified. A return value of 0 means no rows were
# affected (which is not considered an error).
#
# The function supports parameterized queries, and the parameters
# can be passed as a list (this is optional).
#
# Returns: the number of rows modified by the query. If an error
# occurs, a message is printed and -1 is returned. A return value
# of 0 is not considered an error and indicates that no rows were
# updated (e.g., if the WHERE condition in the query was false).
#
def perform_action(dbConn, sql, parameters=None):
    if parameters == None:
        parameters = []  # Initialize parameters to an empty list if none are provided
    DbCursor = dbConn.cursor()  # Create a cursor to execute the SQL query

    try:
        DbCursor.execute(sql, parameters)  # Execute the SQL query with the provided parameters
        dbConn.commit()  # Commit the transaction to save changes in the database
        return DbCursor.rowcount  # Return the number of rows modified

    except Exception as error:
        # Catch any exceptions and print an error message
        print("perform_action failed:", error)
        return -1  # Return -1 if an error occurred

    finally:
        # Always close the cursor after executing the query
        DbCursor.close()
