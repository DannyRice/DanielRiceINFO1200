#!/usr/bin/env python3
print("Daniel Rice's Rectangle App")  # shows my name


print("The Area and Perimeter Program")  # display a welcome message
print()  # makes a space

# get input from the user
length = float(input("Please enter the length: "))# user inputs the length variable
width = float(input("Please enter the width:\t"))# user inputs the width variable

# calculations
area = length * width  # calculate area
perimeter = (length*2) + (width * 2)  # calculate perimeter

# format and display the result
print()  # makes a space
print("Area = \t" + str(area))  # shows the output of the area calculation
# shows the output of the perimeter calculation
print("Perimeter = " + str(perimeter))
print()  # makes a space
print("Thanks for using this program!")  # prints goodbye message
