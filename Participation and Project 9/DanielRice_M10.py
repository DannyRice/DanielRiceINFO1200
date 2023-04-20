#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: April 4th, 2023
# Project #: M10
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import csv  # import the csv module

FILENAME = "monthly_sales.csv"  # sets FILENAME to the csv file name


def display_title():
    """Displays the program title
    """
    print("Daniel Rice's Monthly Sales")  # displays the title
    print("")  # displays a space


def display_menu():
    """Displays the command menu
    """
    print("")  # displays a space
    print("")  # displays a space
    print("COMMAND MENU")  # displays the menu section title
    print("")  # displays a space
    print("monthly - View monthly sales")  # displays a command option
    print("yearly  - View yearly summary")  # displays a command option
    print("edit    - Edit sales for a month")  # displays a command option
    print("exit    - Exit program")  # displays a command option
    print("")  # displays a space


def read_sales():
    """Reads the csv file

    Returns:
        list: list of sales made
    """
    sales = []  # sets the sales list
    with open(FILENAME, "r", newline="") as file:  # open the csv file with read mode
        # creates a variabble to read from the csv file by calling the csv module
        reader = csv.reader(file)
        for row in reader:  # for each row read
            sales.append(row)  # add sales to the list
    return sales  # return the sales list


def view_monthly_sales(sales):
    """Displays the monthly sales list

    Args:
        sales (list): Holds all the information about the sales for each month
    """
    for row in sales:  # for each row in the sales list
        print(f"{row[0]} - {row[1]}")  # print the row
    print("")  # displays a space


def view_yearly_summary(sales):
    """Displays the yearly sales list

    Args:
        sales (list): Holds all the information about the sales for each year
    """
    total = 0  # sets total variable to 0
    for row in sales:  # for each row in the sales list
        amount = int(row[1])  # set amount to the integer in the row
        total += amount  # add the amount variable to the total variable

    count = len(sales)  # set count variable to the length of the sales list

    average = total / count  # calcualte average
    average = round(average, 2)  # round the average score

    print("Yearly total:    ", total)  # display the yearly total
    print("Monthly average: ", average)  # display the monthly average
    print("")  # display a space


def edit(sales):
    """Allows the user to edit the sales file

    Args:
        sales (_type_): _description_
    """
    names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # sets names to a list of containing each month
    # User input into the name variable
    name = input("Input three-letter Month: ")
    name = name.title()  # makes the input not case sensative

    # if the user input does not match an item in the names list
    if name not in names:
        print("Invalid three-letter Month")  # display error message
    else:  # otherwise
        index = names.index(name)  # set index to the first int value in name
        # sets amount to the input amount of sales
        amount = int(input("Sales Amount: "))
        month = []  # month list
        month.append(name)  # add user input name into the month list
        # add user input sales amount to the month list
        month.append(str(amount))
        sales[index] = month  # adds the month listing to the sales list
        # uses the write_sales function to add to the sales list
        write_sales(sales)
        # displays an update message
        print(f"Sales amount for {month[0]} was modified")
    print("")  # displays a space


def write_sales(sales):
    """Adds to the sales lsit

    Args:
        sales (list): lists the sales information
    """
    with open(FILENAME, "w", newline="") as file:  # opens the csv file in write mode
        # creates the writer variable to the csv file by calling the csv module
        writer = csv.writer(file)
        writer.writerows(sales)  # write the input sales into the csv file


def main():
    """Allows user to view and edit the sales information
    """
    display_title()  # call the display title function
    display_menu()  # call the display menu function
    sales = read_sales()  # read the sales list

    while True:  # infinite while loop
        command = input("Command: ")  # Allows user to input a command
        if command == "monthly":  # if the command input was monthly
            view_monthly_sales(sales)  # use the view_monthly_sales function
        elif command == "yearly":  # if the command input was yearly
            view_yearly_summary(sales)  # use the view_yearly_summary function
        elif command == "edit":  # if the command input was edit
            edit(sales)  # use the edit function
        elif command == "exit":  # if the command input was exit
            break  # stop the loop
        else:  # if anything else is out in
            # displays an error message
            print("Not a valid command. Please try again.\n")
    print("Bye!")  # displays a goodbye message


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
