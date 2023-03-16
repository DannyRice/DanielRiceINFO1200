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
print("Daniel Rice's Tip Calculator")  # Displays welcome message
print()  # makes a space

# User inputs the cost of their meal
meal_cost = float(input("Cost of meal: "))
print()  # makes a space

for i in range(15, 30, 5):  # sets the range for i to start at 15, end at but not include 30, and go up by 5 at a time
    print(i, "%")  # displays i and a % sign after it
    tip_percent = i / 100  # sets tip_percent variable to i divided by 100
    # sets tip_amount to the meal cost multiplied by the tip percent, rounded up to the 2nd decimal point
    tip_amount = round(meal_cost * tip_percent, 2)
    print("Tip amount: ", tip_amount)  # displays the tip amount
    # sets the total variable to the meal cost added to the tip amount, rounded to the 2nd decimal point
    total = round(meal_cost + tip_amount, 2)
    print("Total amount: ", total)  # displays the total amount
    print()  # makes a space
