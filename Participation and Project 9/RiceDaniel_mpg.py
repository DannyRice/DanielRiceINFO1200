#!/usr/bin/env python3

# import the csv module
import csv

# creates file name for the csv file
FILE_NAME = "trips.csv"


def write_trips(trips):
    """Opens the csv file and writes in the input to a list

    Args:
        trips (list): User inputs a list
    """
    with open(FILE_NAME, "w", newline="") as output_file:  # open the csv file with write mode
        # creates a variable to write to the csv file by calling the csv module
        writer = csv.writer(output_file)
        writer.writerows(trips)  # write the input trips into the csv file


def read_trips():
    """Opens the csv file and reads the content

    Returns:
        list: User input list
    """
    trips = []  # sets trips variable as a list
    with open(FILE_NAME, "r", newline="") as input_file:  # open the csv file with read mode
        # creates a variable to read from the csv file by calling the csv module
        reader = csv.reader(input_file)
        for row in reader:  # for each row read
            trips.append(row)  # add trips to the row
    return trips  # return the list


def list_trips(trips):
    """lists out the trips all together
    """
    print("Distance\tGallon\tMPG")  # Display sections
    for i in range(0, len(trips)):  # go through the 2d list
        trip = trips[i]  # put each trip in the list
        # display the trip values
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
    print()  # display a space


def get_miles_driven():
    """Has the user input the number of miles driven

    Returns:
        variable: User input
    """
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:  # while loop that has the user input the miles driven on the trip
        # displays error message
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven  # returns the variable


def get_gallons_used():
    """Has the user input the number of gallons used

    Returns:
        variable: User input
    """
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:  # while loop that has the user input the gallons used on the trip
        # displays error message
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used  # returns the variable


def main():
    """Main trip program
    """
    # display a welcome message
    print("The Miles Per Gallon program")
    print()  # displays a space

    trips = read_trips()  # 2d list for the input trips by using the read_trips function
    list_trips(trips)  # uses the list_trips funciton to list out the trips

    more = "y"  # sets y in more variable
    while more.lower() == "y":  # while more is a y input by the user
        # sets miles_driven as the get_miles_driven function
        miles_driven = get_miles_driven()
        # sets gallons_used as the get_gallons_used function
        gallons_used = get_gallons_used()

        # calculation for the miles per gallon rounded by 2 decimal points
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")  # display the calculation results
        print()  # display a space

        # variable that makes one trip
        single_trip = [miles_driven, gallons_used, mpg]
        trips.append(single_trip)  # adds the trip to the list
        # uses the write_trips funciton to write the trip to the csv file
        write_trips(trips)
        list_trips(trips)  # uses the list_trips function to list out the trips

        # User inputs if they want to restart the program
        more = input("More entries? (y or n): ")

    print("Bye!")  # display goodbye message


# gives top level scope to main
if __name__ == "__main__":
    main()
