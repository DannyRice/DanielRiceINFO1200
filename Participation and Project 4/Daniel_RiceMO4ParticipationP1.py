#!/usr/bin/env python3


# display a welcome message
print("Daniel Rice's Miles Per Gallon application")
print()  # makes a space

another_trip = "y"  # assigns y to a variable

while another_trip == "y":  # starts a while loop for whenever another trip is equal to y
    # get input from the user
    # input the miles driven
    miles_driven = float(input("Enter miles driven:         "))
    # input the amount of gallons used
    gallons_used = float(input("Enter gallons of gas used:  "))
    # input the cost per gallon
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    print() # makes a space

    if miles_driven <= 0:  # if the input is 0 or less, print the message below
        # prints an error message
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:  # if the input is 0 or less, print the message below
        # prints an error message
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:  # if the input is 0 or less, print the message below
        # prints an error message
        print("Cost per gallon must be greater than zero. Please try again.")
    else:  # once all the if and elif are done, come to this section of code
        # calculate miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:          ", mpg)  # display miles per gallon
        # calculate miles per gallon
        total_gas_cost = round((gallons_used * cost_per_gallon), 1)
        # display total gas cost
        print("Total Gas Cost:            ", total_gas_cost)
        # calculate miles per gallon
        cost_per_mile = round((total_gas_cost / miles_driven), 1)
        # display cost per mile
        print("Cost Per Mile:             ", cost_per_mile)
        print() # makes a space
        # input y or n to restart the user input for the program or not
        another_trip = input("Get entries for another trip (y/n)?  ")
    print()  # makes a space
print("Bye")  # display good bye message
