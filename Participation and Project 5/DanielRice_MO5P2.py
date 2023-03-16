#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 2/22/2023
# Project #: MO5_P2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
import drconverter as c
print("Daniel Rice's Feet / Meters Converter")  # display title
print()  # makes a space


def fm_welcome():
    ''' 
    Displays Welcome message 
    '''
    print("Daniel's Feet and Meters Converter")  # print welcome message
    print()  # makes a space


def fm_menu():
    '''
    Displays the menu options
    '''
    print("Conversions Menu: ")  # print menu title
    print()  # makes a space
    print("a. Feet to Meters")  # print option a
    print("b. Meters to Feet")  # print option b


def main():
    """The main program that displays the welcome message and the menu
    """

    fm_welcome()  # calls welcome message function
    while True:  # infinite while loop
        fm_menu()  # calls menu function
        # sets choice variable to user input of either a or b
        choice = input("Select a conversion (a/b): ")
        print()  # makes a space
        if choice == "a":  # if the choice was a
            # Allow user to input feet value
            feet = float(input("Enter Feet: "))
            meters = c.to_meters(feet)  # conversion to meters
            # print outcome rounded by 2 decimal places
            print(round(meters, 2), " meters")
        elif choice == "b":  # if the choice was not a but b
            # Allow user to input meters value
            meters = float(input("Enter Meters: "))
            feet = c.to_feet(meters)  # conversion to feet
            # print outcome rounded by 2 decimal places
            print(round(feet, 2), " feet")
        else:  # if neither a or b was chosen
            print("You did not enter a valid selection")  # print error message

        # set more variable to allow user a choice to continue
        print()  # makes a space
        more = input("Would you like to perform another conversion? (y/n): ")
        print()  # makes a space
        if more != "y":  # if more does not equal "y"
            True  # set value to true
            print("Thanks, bye!")  # print goodbye message
            break  # terminate loop


# allows code to be executed as a script with top level scope
if __name__ == "__main__":
    main()
