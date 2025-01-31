"""
Name: Rahin Jain
UIN: 665219123
netid: rjain56
Project 2: Part 3
Fall '24 CS 341 - Prof. Jon Solworth
"""

# Import necessary libraries
import sqlite3
import objecttier

##################################################################
#
# main
#
# Entry point for the application, welcoming the user and connecting to the database.
print('** Welcome to the Chicago Lobbyist Database Application **')

# Establish a connection to the database.
dbConn = sqlite3.connect('Chicago_Lobbyists.db')


def Command0():
    """
    Function to display general statistics of the database including the number
    of lobbyists, employers, and clients.
    """
    lobbyist_obj = objecttier.num_lobbyists(dbConn)
    employers_obj = objecttier.num_employers(dbConn)
    clients_obj = objecttier.num_clients(dbConn)

    print("General Statistics:")
    print("  Number of Lobbyists: {:,}".format(lobbyist_obj))
    print("  Number of Employers: {:,}".format(employers_obj))
    print("  Number of Clients: {:,}".format(clients_obj))


def Command1(dbConn, name):
    """
    Function to retrieve and display lobbyists based on the provided name.
    Allows for wildcard searching.
    """
    lobbyist_data = objecttier.get_lobbyists(dbConn, name)
    print("\nNumber of lobbyists found:", len(lobbyist_data))

    if len(lobbyist_data) > 100:
        print("\nThere are too many lobbyists to display, please narrow your search and try again...")
    else:
        for d in lobbyist_data:
            print(d.Lobbyist_ID, ":", d.First_Name, d.Last_Name, "Phone:", d.Phone)


def Command2(dbConn, lobbyist_id):
    """
    Function to retrieve and display detailed information of a lobbyist based on the provided ID.
    """
    lobbyist_data = objecttier.get_lobbyist_details(dbConn, lobbyist_id)

    if lobbyist_data == None:
        print("\nNo lobbyist with that ID was found.")
    else:
        print(lobbyist_data.Lobbyist_ID, ":")
        print("  Full Name:", lobbyist_data.Salutation, lobbyist_data.First_Name, lobbyist_data.Middle_Initial,
              lobbyist_data.Last_Name, lobbyist_data.Suffix)
        print("  Address:", lobbyist_data.Address_1, lobbyist_data.Address_2, ",", lobbyist_data.City, ",",
              lobbyist_data.State_Initial, lobbyist_data.Zip_Code, lobbyist_data.Country)
        print("  Email:", lobbyist_data.Email)
        print("  Phone:", lobbyist_data.Phone)
        print("  Fax:", lobbyist_data.Fax)
        print("  Years Registered:", end=" ")
        for d in lobbyist_data.Years_Registered:
            print(d, end=", ")
        print()
        print("  Employers:", end=" ")
        for d in lobbyist_data.Employers:
            print(d, end=", ")
        print()
        print("  Total Compensation: ${:,.2f}".format(lobbyist_data.Total_Compensation))


def Command3(dbConn, N, year):
    """
    Function to retrieve and display the top N lobbyists for a given year based on compensation.
    """
    lobbyist_data = objecttier.get_top_N_lobbyists(dbConn, N, year)
    count = 1

    for d in lobbyist_data:
        print(count, ".", d.First_Name, d.Last_Name)
        print("  Phone: ", d.Phone)
        print("  Total Compensation: ${:,.2f}".format(d.Total_Compensation))
        print("  Clients:", end=" ")
        for c in d.Clients:
            print(c, end=", ")
        print()
        count += 1


def Command4(dbConn, lobbyist_id, year):
    """
    Function to add a registration year for a specific lobbyist.
    """
    id_found = objecttier.add_lobbyist_year(dbConn, lobbyist_id, year)

    if id_found == 0 or id_found == -1:
        print("\nNo lobbyist with that ID was found.")
    else:
        print("\nLobbyist successfully registered.")


def Command5(dbConn, lobbyist_ID, salutation):
    """
    Function to set or update the salutation for a specific lobbyist.
    """
    id_found = objecttier.set_salutation(dbConn, lobbyist_ID, salutation)

    if id_found == 0 or id_found == -1:
        print("\nNo lobbyist with that ID was found.")
    else:
        print("\nSalutation successfully set.")


# Display general statistics at the start of the application.
Command0()

# Command loop to keep the application running until the user decides to exit.
cmd = input("Please enter a command (1-5, x to exit): \n")

while cmd != "x":
    if cmd == "1":
        # Command to search lobbyists by name
        inp = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
        Command1(dbConn, inp)
    elif cmd == "2":
        # Command to display lobbyist details by ID
        inp = input("Enter Lobbyist ID: \n")
        Command2(dbConn, inp)
    elif cmd == "3":
        # Command to display top N lobbyists for a specific year
        inp = int(input("Enter the value of N: "))
        if inp <= 0:
            print("Please enter a positive value for N...")
        else:
            inp2 = input("Enter the year: \n")
            Command3(dbConn, inp, inp2)
    elif cmd == "4":
        # Command to add a registration year for a specific lobbyist
        inp = input("Enter year: ")
        inp2 = input("Enter the lobbyist ID: ")
        Command4(dbConn, inp2, inp)
    elif cmd == "5":
        # Command to set or update the salutation for a lobbyist
        inp = input("Enter the lobbyist ID: ")
        inp2 = input("Enter the salutation: ")
        Command5(dbConn, inp, inp2)
    else:
        # Handle unknown commands
        print("**Error, unknown command, try again...")

    # Prompt for the next command
    cmd = input("Please enter a command (1-5, x to exit): \n")

# End of the application
# Closing message or any necessary cleanup code can go here.