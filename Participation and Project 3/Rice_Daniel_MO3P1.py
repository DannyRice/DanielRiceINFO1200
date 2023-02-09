#!/usr/bin/env python3
print("Daniel Rice's MPG App")  # print my name and my app


print("The Miles Per Gallon program")  # display a welcome message
print()  # makes a space

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t")
                     )  # user inputs amount of miles
gallons_used = float(input("Enter gallons of gas used:\t")
                     )  # user inputs amount of gallons used
# user inputs cost of a gallon of gas
gallon_cost = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon and costs
# miles per gallon = miles driven divided by the gallons used
mpg = miles_driven / gallons_used
# total miles per gallon rounded to the first decimal place
mpg = round(mpg, 1)
# calculates gallons used multiplied by the cost of a gallon
tgc = gallons_used * gallon_cost
# calculate and round the gallons used divided by the total gas cost
cpm = round(gallons_used / tgc, 1)

# format and display the result
print()  # makes a space
print("Miles Per Gallon:\t" + str(mpg))  # shows the result of miles per gallon
# shows the result of total gallon cost
print("Total Gas Cost:\t\t" + str(tgc))
print("Cost Per Mile:\t\t" + str(cpm))  # shows the result of cost per miles
print()  # makes a space
print("Bye")  # shows bye on the screen
