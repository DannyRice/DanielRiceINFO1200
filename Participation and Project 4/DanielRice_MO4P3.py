#!/usr/bin/env python3
# Name: Daniel Rice
# Class: INFO 1200
# Section: 001
# Professor: Dr. Crandall
# Date: 2/16/2023
# Project #: MO4_P2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
print("Daniel Rice's Change App")  # display welcome message
print()  # makes a space

choice = "y"  # sets the choice variable to y
while choice.lower() == "y":  # while the choice variable is set to y (or Y)
    # User inputs the number of cents to the variable of cents
    cents = float(input("Enter the number of cents (0-99): "))
    print()  # makes a space

    # sets quarters to the amount of cents divided by 25 rounded to the next smallest whole number
    quarters = cents // 25
    cents = cents % 25  # resets cents value to cents modulo 25 to get the remainder

    # sets dimes to the amount of cents divided by 10 rounded to the next smallest whole number
    dimes = cents // 10
    cents = cents % 10  # resets cents value to cents modulo 10 to get the remainder

    # sets nickles to the amount of cents divided by 5 rounded to the next smallest whole number
    nickles = cents // 5
    cents = cents % 5  # resets cents value to cents modulo 5 to get the remainder

    # sets pennies to the amount of cents divided by 1 rounded to the next smallest whole number
    pennies = cents // 1
    cents = cents % 1  # resets cents value to cents modulo 1 to get the remainder

    print("Quarters: ", quarters)  # display the amount of quarters
    print("Dimes: ", dimes)  # dispaly the amount of dimes
    print("Nickles: ", nickles)  # displays the amount of nickles
    print("Pennies: ", pennies)  # displays the amount of pennies
    print()  # makes a space

    # User inputs if they would like to continue to use the program
    choice = input("Continue? (y/n): ")
    print()  # makes a space
print("Bye!")  # displays goodbye message
