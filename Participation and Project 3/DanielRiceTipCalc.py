# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Crandall)
# Date: Feb 11, 2023
# Project #: MO3
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
print("Daniel Rice's Tip Calculator App")  # Program name
print()  # makes a space

# user inputs the cost of their meal
costOfMeal = float(input("Cost of meal: "))
# user inputs the tip percent they would like to pay
tipPercentage = float(input("Tip Percent: "))
print()  # makes a space

# multiplies the cost of the meal multiplied by the tip percentage divided by 100, and rounded to the second decimal place
tipAmount = round(costOfMeal * (tipPercentage / 100), 2)
print("Tip amount: " + str(tipAmount))  # displays the calculated tip amount
# adds the tip amount to the cost of the meal, rounded to the second decimal place
totalAmount = round(costOfMeal + tipAmount, 2)
# displays the total cost of the meal
print("Total amount: " + str(totalAmount))
