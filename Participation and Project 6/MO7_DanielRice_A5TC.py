#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 3/14/2023
# Project #: MO7_P1
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.


def sales_tax(price):
    '''
    """Sets the tax value and the calculation for the sales tax

    Param:
        sales_tax - variable set to multiplied input price by 6%
    """    
    '''
    tax = 0.06  # sets TAX variable value to 6%
    sales_tax = price * tax  # sets sales_tax variable to price multiplied by tax
    return sales_tax  # send sales_tax variable back


def main():
    '''Displays the Sales tax calculator and asks user for input of the total cost, and then calculates the added sales tax, and displays the result

    param:
        total - is set by user input
    '''
    print("Sales Tax Calculator\n")  # display message
    # sets total variable to a floated user input
    total = float(input("Enter total: "))
    # sets total_after_tax variable to total added by the called sales_tax function, rounded by 2
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)  # display calculation result


# allows code to be executed as a script with top level scope
if __name__ == "__main__":
    main()
