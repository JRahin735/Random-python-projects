# Student Name: Rahin Jain
# UIN: 665219123
# Class: CS 341 for fall '24
# Project 1: CTA Database App
# Description: The CTA Database App is an interactive tool that analyzes Chicago Transit Authority data using SQLite.
#              Users can explore station details, ridership statistics, and stop information. It supports querying by
#              station, date, and line color, comparing stations, and visualizing trends through graphs, offering
#              insights into Chicago’s public transit system.

import sqlite3
import matplotlib.pyplot as plt


# Stat function: This function retrieves and displays general statistics from the CTA database, including station
#                count, stops, ridership entries, and totals.
def stat(dbConn, dbCursor):
    dbCursor.execute("select count(*) from stations;")
    row = dbCursor.fetchone();
    print("  # of stations:", f"{row[0]:,}")

    dbCursor = dbConn.cursor()

    dbCursor.execute("select count(*) from stops;")
    row = dbCursor.fetchone();
    print("  # of stops:", f"{row[0]:,}")

    DbCursor = dbConn.cursor()
    DbCursor.execute("select count(*) from Ridership;")
    row = DbCursor.fetchone();
    print("  # of ride entries:", f"{row[0]:,}")

    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select strftime('%Y-%m-%d', Min(Ride_Date)), strftime('%Y-%m-%d', Max(Ride_Date)) from Ridership;")
    row = DbCursor.fetchone();
    print("  date range:", f"{row[0]} - {row[1]}")

    DbCursor = dbConn.cursor()
    DbCursor.execute("select sum(Num_riders) from Ridership;")
    row = DbCursor.fetchone();
    print("  Total ridership:", f"{row[0]:,}")


# Command functions:

# This function, Command1, prompts the user to input a partial station name (with wildcards).
# It queries the database for matching station names, retrieves their IDs, and prints them in alphabetical order.
# If no stations are found, it displays an appropriate message.
def Command1(dbConn):
    station = input("\nEnter partial station name (wildcards _ and %): ")
    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select station_id, station_name from stations "
        "where station_name like ? "
        "group by Station_id "
        "order by station_name asc;", [station]
    )

    row = DbCursor.fetchall();
    if (len(row) == 0):
        print("**No stations found...")
    for a in row:
        print(f"{a[0]} : {a[1]}")

# This function analyzes ridership for a selected station, displaying weekday, Saturday, Sunday/holiday totals,
# and percentages of overall ridership.
def Command2(dbConn):
    station = input("\nEnter the name of the station you would like to analyze: ")
    DbCursor = dbConn.cursor()

    DbCursor.execute(
        "select sum(num_riders) from ridership "
        "join Stations on stations.station_id = ridership.station_id "
        "where station_name == ? and Type_of_Day == 'W';", [station]
    )

    weekday = DbCursor.fetchone();
    DbCursor.execute(
        "select sum(num_riders) from ridership "
        "join stations on stations.station_id = ridership.station_id "
        "where station_name == ? and type_of_day == 'A';", [station]
    )

    saturday = DbCursor.fetchone();
    DbCursor.execute(
        "select sum(num_riders) from ridership "
        "join stations on stations.station_id = ridership.station_id "
        "where station_name == ? and type_of_day == 'U';", [station]
    )

    sunday = DbCursor.fetchone();
    DbCursor.execute(
        "select sum(num_riders) from ridership "
        "join stations on stations.station_id = ridership.station_id "
        "where station_name == ?;", [station]
    )

    total = DbCursor.fetchone();

    if (weekday[0] == None):
        print("**No data found...")
    else:

        weekper = (int(weekday[0]) / int(total[0])) * 100
        satper = (int(saturday[0]) / int(total[0])) * 100
        sunper = (int(sunday[0]) / int(total[0])) * 100

        print("Percentage of ridership for the", station, "station: ")
        print("  Weekday ridership:", f"{weekday[0]:,}", f"({weekper:.2f}%)")
        print("  Saturday ridership:", f"{saturday[0]:,}", f"({satper:.2f}%)")
        print("  Sunday/holiday ridership:", f"{sunday[0]:,}", f"({sunper:.2f}%)")
        print("  Total ridership:", f"{total[0]:,}")

# This function, **Command3**, retrieves and displays weekday ridership for each station in descending order.
# It calculates the percentage of total weekday riders for each station and prints the station name,
# total riders, and percentage.
def Command3(dbConn):
    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select station_name, sum(num_riders) from Stations "
        "join ridership on stations.station_id == ridership.station_id "
        "where type_of_day == 'W' "
        "group by ridership.station_id "
        "order by sum(num_riders) desc; "
    )

    rows = DbCursor.fetchall();
    DbCursor.execute(
        "select sum(num_riders) from stations "
        "join ridership on stations.station_id == ridership.station_id "
        "where type_of_day == 'W'; "
    )

    total = DbCursor.fetchone();
    print(" Ridership on Weekdays for Each Station")

    for row in rows:
        percentage = (row[1] / total[0]) * 100
        print(f"{row[0]} : {row[1]:,} ({percentage:.2f}%)")

# This function, **Command4**, prompts the user to input a train line color and a direction (N/S/W/E).
# It retrieves and displays all stops along that line in the specified direction. For each stop, it indicates
# whether it is handicap accessible. If no stops or directions are found, it displays appropriate messages.
def Command4(dbConn):
    line = input("\nEnter a line color (e.g. Red or Yellow): ")
    line = line[0].upper() + line[1:].lower()

    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select stop_name from lines "
        "join stopdetails on stopdetails.line_id == lines.line_id "
        "join stops on stopdetails.stop_id == stops.stop_id "
        "where color like ? "
        "order by stop_name asc;", [line]
    )

    rows = DbCursor.fetchall();

    if len(rows) == 0:
        print("**No such line...")

    else:
        direction = input("Enter a direction (N/S/W/E): ").upper()
        DbCursor = dbConn.cursor()

        DbCursor.execute(
            "select stop_name, direction, ada from lines "
            "join stopdetails on stopdetails.line_id == lines.line_id "
            "join stops on stopdetails.stop_id == stops.stop_id "
            "where color like ? and direction == ? "
            "order by stop_name asc;", [line, direction]
        )

        stop_names = DbCursor.fetchall();
        if (len(stop_names) == 0):
            print("**That line does not run in the direction chosen...")

        for stop_name in stop_names:
            if stop_name[2] == 1:
                print(f"{stop_name[0]} : direction = {stop_name[1]} (handicap accessible)")
            else:
                print(f"{stop_name[0]} : direction = {stop_name[1]} (not handicap accessible)")

#This function displays stop counts and percentages for each line color and direction, showing total
# stops for the CTA system.
def Command5(dbConn):
    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select color, direction, count(*) from stopdetails "
        "join lines on stopdetails.line_id == lines.line_id "
        "join stops on stopdetails.stop_id == stops.stop_id "
        "group by color, direction "
        "order by color asc, direction asc;"
    )

    stop_names = DbCursor.fetchall();
    DbCursor.execute(
        "select count(stop_id) from stops;"
    )

    total = DbCursor.fetchone();
    print(" Number of Stops For Each Color By Direction")

    for stop_name in stop_names:
        percentage = (stop_name[2] / total[0]) * 100
        print(f"{stop_name[0]} going {stop_name[1]} : {stop_name[2]} ({percentage:.2f}%)")

# This function retrieves and displays yearly ridership for a station, offering an option to plot the data visually.
def Command6(dbConn):
    station = input("\nEnter a station name (wildcards _ and %): ")
    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select station_name from stations "
        "where station_name like ?;", [station]
    )
    stations = DbCursor.fetchall();

    if len(stations) == 0:
        print("**No station found...")

    elif len(stations) > 1:
        print("**Multiple stations found...")

    else:
        DbCursor = dbConn.cursor()
        DbCursor.execute(
            "select strftime('%Y', ride_date), sum(num_riders) from ridership "
            "join stations on stations.station_id == ridership.station_id "
            "where station_name like ? "
            "group by strftime('%Y', ride_date);", [station]
        )

        passengers = DbCursor.fetchall();
        print("Yearly Ridership at", stations[0][0])

        for passenger in passengers:
            print(f"{passenger[0]} : {passenger[1]:,}")

        plotter = input("Plot? (y/n) \n")

        if plotter == "y":
            x_axis = [];
            y_axis = [];
            for i in range(len(passengers)):
                x_axis.append(passengers[i][0])
                y_axis.append(passengers[i][1])

            plt.plot(x_axis, y_axis)
            plt.xlabel("Year");
            plt.ylabel("Numbers of Riders");
            plt.xticks(fontsize=6)
            plt.yticks(fontsize=6)
            plt.title("Yearly Ridership at UIC-Halsted Station")
            plt.show()

# This function retrieves and displays monthly ridership for a station in a given year, with an option to plot data.
def Command7(dbConn):
    station = input("\nEnter a station name (wildcards _ and %): ")
    DbCursor = dbConn.cursor()

    DbCursor.execute(
        "select station_name from stations "
        "where station_name like ?;", [station]
    )

    stationname = DbCursor.fetchall();

    if len(stationname) == 0:
        print("**No station found...")

    elif len(stationname) > 1:
        print("**Multiple stations found...")

    else:
        date = input("Enter a year: ")
        DbCursor = dbConn.cursor()

        DbCursor.execute(
            "select strftime('%m/%Y', ride_date), sum(num_riders) from ridership "
            "join stations on ridership.station_id == stations.station_id "
            "where station_name like ? and strftime('%Y', ride_date) == ? "
            "group by strftime('%m', ride_date) "
            "order by strftime('%m', ride_date) asc;", [station, date]
        )

        rows = DbCursor.fetchall()
        print("Monthly Ridership at", stationname[0][0], "for", date)

        for row in rows:
            print(f"{row[0]} : {row[1]:,}")

        plotgraph = input("Plot? (y/n) \n")

        if plotgraph == "y":
            x_axis = [];
            y_axis = [];

            for i in range(len(rows)):
                x_axis.append(rows[i][0][0:2])
                y_axis.append(rows[i][1])

            plt.plot(x_axis, y_axis)
            plt.xlabel("Month");
            plt.ylabel("Numbers of Riders");
            plt.xticks(fontsize=6)
            plt.yticks(fontsize=6)
            plt.title("Monthly Ridership at UIC-Halsted Station (2004)")
            plt.show()

# This function compares daily ridership between two stations for a given year, displaying results and
# offering a plot option.
def Command8(dbConn):
    year_to_compare = input("\nYear to compare against? ")
    station = input("\nEnter station 1 (wildcards _ and %): ")

    DbCursor = dbConn.cursor()
    DbCursor.execute(
        "select station_name from stations "
        "where station_name like ?;", [station]
    )
    station_found = DbCursor.fetchall();

    if len(station_found) == 0:
        print("**No station found...")

    elif len(station_found) > 1:
        print("**Multiple stations found...")

    else:
        station2 = input("\nEnter station 2 (wildcards _ and %): ")
        DbCursor = dbConn.cursor()

        DbCursor.execute(
            "select station_name from stations "
            "where station_name like ?;", [station2]
        )
        other_station_found = DbCursor.fetchall();
        if len(other_station_found) == 0:
            print("**No station found...")

        elif len(other_station_found) > 1:
            print("**Multiple stations found...")

        else:
            DbCursor = dbConn.cursor()
            DbCursor.execute(
                "select strftime('%Y-%m-%d', ride_date), sum(num_riders) from ridership "
                "join stations on ridership.station_id == stations.station_id "
                "where station_name like ? and strftime('%Y', ride_date) == ? "
                "group by  strftime('%d', ride_date),strftime('%m', ride_date) "
                "order by strftime('%m', ride_date) asc;", [station, year_to_compare]
            )
            station_found_rows = DbCursor.fetchall();

            DbCursor = dbConn.cursor()
            DbCursor.execute(
                "select station_id from stations "
                "where station_name like ?;", [station]
            )
            total_station_found = DbCursor.fetchall();

            DbCursor = dbConn.cursor()
            DbCursor.execute(
                "select strftime('%Y-%m-%d', ride_date), sum(num_riders) from ridership "
                "join stations on ridership.station_id == stations.station_id "
                "where station_name like ? and strftime('%Y', ride_date) == ? "
                "group by  strftime('%d', ride_date),strftime('%m', ride_date) "
                "order by strftime('%m', ride_date) asc;", [station2, year_to_compare]
            )
            other_station_found_rows = DbCursor.fetchall();

            DbCursor = dbConn.cursor()
            DbCursor.execute(
                "select station_id from stations "
                "where station_name like ?;", [station2]
            )
            total_other_station_found = DbCursor.fetchall();

            print("Station 1:", total_station_found[0][0], station_found[0][0])

            for row in station_found_rows[:5]:
                print(f"{row[0]} {row[1]}")

            for row in station_found_rows[-5:]:
                print(f"{row[0]} {row[1]}")

            print("Station 2:", total_other_station_found[0][0], other_station_found[0][0])

            for row in other_station_found_rows[:5]:
                print(f"{row[0]} {row[1]}")

            for row in other_station_found_rows[-5:]:
                print(f"{row[0]} {row[1]}")

            ploter = input("Plot? (y/n) \n")

            if ploter == "y":
                x_axis1 = []
                y_axis1 = []
                x_axis2 = []
                y_axis2 = []
                day = 1

                for i in range(len(station_found_rows)):
                    x_axis1.append(day)
                    y_axis1.append(station_found_rows[i][1])
                    x_axis2.append(day)
                    y_axis2.append(other_station_found_rows[i][1])
                    day = day + 1

                plt.plot(x_axis1, y_axis1)
                plt.plot(x_axis2, y_axis2)
                plt.legend(['Midway Airport', "O'Hare Airport"], loc='upper right')
                plt.xlabel("Day");
                plt.ylabel("Numbers of Riders");
                plt.xticks(fontsize=6)
                plt.yticks(fontsize=6)
                plt.title("Ridership Each Day of " + str(year_to_compare))
                plt.show()

# This function finds and displays stations within a one-mile radius of given latitude and longitude,
# with an option to plot.
def Command9(dbConn):
    lat = float(input("\nEnter a latitude: "))

    if lat < 40 or lat > 43:
        print("**Latitude entered is out of bounds...")

    else:
        lon = float(input("Enter a longitude: "))

        if lon < -88 or lon > -87:
            print("**Longitude entered is out of bounds...")

        else:
            upper_lat = lat + round(1 / 69, 3)
            lower_lat = lat - round(1 / 69, 3)
            upper_long = lon + round(1 / 51, 3)
            lower_long = lon - round(1 / 51, 3)

            DbCursor = dbConn.cursor()

            DbCursor.execute(
                "select distinct station_name, latitude, longitude from stations "
                "join stops on stations.station_id == stops.station_id "
                "where ? > latitude and latitude > ? and ? > longitude and longitude > ? "
                "order by station_name asc;", [upper_lat, lower_lat, upper_long, lower_long]
            )
            rows = DbCursor.fetchall();
            if len(rows) == 0:
                print("**No stations found...")

            else:
                print("\nList of Stations Within a Mile")
                for row in rows:
                    print(f"{row[0]} : ({row[1]}, {row[2]})")

                plotter = input("Plot? (y/n) \n")

                if plotter == 'y':
                    x_axis = []
                    y_axis = []
                    stations = []

                    length = len(rows)

                    for i in range(length):
                        y_axis.append(rows[i][1])
                        x_axis.append(rows[i][2])
                        stations.append(rows[i][0])

                    img = plt.imread("chicago.png")
                    dimensions = [-87.9277, -87.5569, 41.7012, 42.0868]
                    plt.imshow(img, extent=dimensions)
                    plt.title("Stations near you")
                    plt.plot(x_axis, y_axis)

                    for i in range(len(stations)):
                        plt.annotate(stations[i], (x_axis[i], y_axis[i]))

                    plt.xlim([-87.9277, -87.5569])
                    plt.ylim([41.7012, 42.0868])
                    plt.show()


# Interface function:
def interface(dbConn):
    answer = input("Please enter a command (1-9, x to exit):")

    while (answer != "x"):
        if answer == "1":
            Command1(dbConn)
        elif answer == "2":
            Command2(dbConn)
        elif answer == "3":
            Command3(dbConn)
        elif answer == "4":
            Command4(dbConn)
        elif answer == "5":
            Command5(dbConn)
        elif answer == "6":
            Command6(dbConn)
        elif answer == "7":
            Command7(dbConn)
        elif answer == "8":
            Command8(dbConn)
        elif answer == "9":
            Command9(dbConn)
        else:
            print(" **Error, unknown command, try again...")

        answer = input("Please enter a command (1-9, x to exit):")


# Main

# Connection
dbConn = sqlite3.connect('CTA2_L_daily_ridership.db')
dbCursor = dbConn.cursor()

# Statistics
print('** Welcome to CTA L analysis app **')
print("General Statistics:")
stat(dbConn, dbCursor)

# Application interface
interface(dbConn)