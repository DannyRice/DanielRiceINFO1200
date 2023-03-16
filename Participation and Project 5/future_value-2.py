#!/usr/bin/env python3
# imports the functions from the validate.py file and can be used by putting v. in front of the function
import validate as v
print("Daniel Rice's Validated Future Value App")  # Displays welcome message


def calculate_future_value(monthly_investment, yearly_interest, years):
    '''
    Calculates the yearly interest base off of the monthly investment and amount of years
    param: monthly investment is user input, yearly investment is user input, yeras is user input
    '''
    # convert yearly values to monthly values
    # set monthly interest rate variable to divide yearly_interest  by 12 and then by 100
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12  # set months variable to multiply years by 12

    # calculate future value
    future_value = 0.0  # sets future value variable
    for i in range(0, months):  # sets a range for i in terms of the value of months
        # adds the monthly investment variable into the future value
        future_value += monthly_investment
        # sets monthly interest to be the future value muliplied by the monthly interest rate
        monthly_interest = future_value * monthly_interest_rate
        # adds the monthly interest value to the future value variable
        future_value += monthly_interest

    return future_value  # send future value variable back to it's caller


def main():
    '''
    User inputs the monthly investment, yearly interest rate, and amount of years. It then displays the calculated value
    '''
    choice = "y"  # sets choice variable to "y"
    while choice.lower() == "y":  # starts a while loop for as long as choice is equal to "y"
        # user input a number from 0-1000 for variable monthly investment
        monthly_investment = v.get_float(
            "Enter monthly investment:\t", 0, 1000)
        # user input a number from 0-15 for variable yearly interest rate
        yearly_interest_rate = v.get_float(
            "Enter yearly interest rate:\t", 0, 15)
        # user input a number from 0-50 for variable years
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        # get function to calculate the future value and put as a variable
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        # display the calculated future value rounded by 2 decimal places
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()  # makes a space

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()  # makes a space

    print("Bye!")  # display good bye message


# allows code to be executed as a script with top level scope
if __name__ == "__main__":
    main()
