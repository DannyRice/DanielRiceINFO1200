#!/usr/bin/env python3
# Name: Daniel Rice
# Class: INFO 1200
# Section: 001
# Professor: Dr. Crandall
# Date: 2/16/2023
# Project #: MO4_P1
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
print("Daniel Rice's Letter Grade Converter")  # display welcome message
print()  # makes a space

choice = "y"  # set choice variable to y
while choice.lower() == "y":  # while the choice variable is set to y, run the code below
    # User inputs a letter grade
    number = int(input("Enter numerical grade: "))
    if number >= 94 and number < 100:  # if the number is between 94 and 100
        letter = "A"  # then set letter varible to A
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 90 and number <= 93:  # if the number is between 90 and 93
        letter = "A-"  # then set letter varible to A-
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 87 and number <= 89:  # if the number is between 87 and 89
        letter = "B+"  # then set letter varible to B+
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 83 and number <= 86:  # if the number is between 83 and 86
        letter = "B"  # then set letter varible to B
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 80 and number <= 82:  # if the number is between 80 and 82
        letter = "B-"  # then set letter varible to B-
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 77 and number <= 79:  # if the number is between 77 and 79
        letter = "C+"  # then set letter varible to C+
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 73 and number <= 76:  # if the number is between 73 and 76
        letter = "C"  # then set letter varible to C
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 70 and number <= 72:  # if the number is between 70 and 72
        letter = "C-"  # then set letter varible to C-
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 67 and number <= 69:  # if the number is between 67 and 69
        letter = "D+"  # then set letter varible to D+
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 63 and number <= 66:  # if the number is between 63 and 66
        letter = "D"  # then set letter varible to D
        print("Letter Grade: ", letter)  # and display the letter grade
    elif number >= 60 and number <= 62:  # if the number is between 60 and 62
        letter = "D-"  # then set letter varible to D-
        print("Letter Grade: ", letter)  # and display the letter grade
    else:  # once all the if and elif are done, come to this section of code
        letter = "E"  # then set letter varible to E
        print("Letter Grade: ", letter)  # and display the letter grade
    print()  # makes a space
    # ask for user input again to restart the program
    choice = input("Continue? (y/n): ")
    print()  # makes a space
print("Bye!")  # displays goodbye message
