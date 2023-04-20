#!/usr/bin/env python3

def get_number(prompt, low, high):
    """Validates the users input

    Args:
        prompt (parameter): User inputs a number
        low (parameter): sets lower bound of number
        high (parameter): sets upper bound of number

    Returns:
        variable: float user input
    """
    while True:  # while True loop
        try:  # test code for errors
            # user inputs to the nubmer variable converted to a float
            number = float(input(prompt))

        except:  # catch exceptions if there are any
            # display error message
            print("You entered an invalid number. Please try again.")
            continue  # end the loop

        if number > low and number <= high:  # if the input number is greater than the lower bound and greater than or equal to the upper bound
            return number  # return the number variable
        else:  # if the if statement isn't valid
            print(f"Entry must be greater than {low} "
                  f"and less than or equal to {high}.")  # display error message


def get_integer(prompt, low, high):
    """Validates the users input

    Args:
        prompt (parameter): User inputs a number
        low (parameter): sets lower bound of number
        high (parameter): sets upper bound of number

    Returns:
        variable: float user input
    """
    while True:  # while True loop
        try:
            # user inputs to the nubmer variable converted to an integer
            number = int(input(prompt))

        except:  # catch exceptions if there are any
            # display error message
            print("You entered an invalid number. Please try again.")
            continue  # end the loop

        if number > low and number <= high:  # if the input number is greater than the lower bound and greater than or equal to the upper bound
            return number  # return the number variable
        else:  # if the if statement isn't valid
            print(f"Entry must be greater than {low} "
                  f"and less than or equal to {high}.")  # display error message


def calculate_future_value(monthly_investment, yearly_interest, years):
    """Does the calculation for the total future value

    Args:
        monthly_investment (parameter): User input from 0-1000
        yearly_interest (paramter): User input from 0-15
        years (parameter): User input from 0-50

    Returns:
        variable: float calculation result
    """
    # convert yearly values to monthly values
    # sets monthly_interest_rate variable to yearly_interest divided by 12 divided by 100
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12  # set months variable to years multiplied by 12

    # calculate future value
    future_value = 0.0  # sets future_value variable to 0
    for i in range(months):  # for each month input
        future_value += monthly_investment  # add the monthly investment to future_value
        # set monthly_interest variable to future_value * the monthly_interest_rate
        monthly_interest = future_value * monthly_interest_rate
        # add the monthly interest to the future_value variable
        future_value += monthly_interest

    return future_value  # return the future value until i gets to the amount of months input


def main():
    """Display all the code to calculate the future value
    """
    choice = "y"  # set choice variable to y
    while choice.lower() == "y":  # while choice (sets input to lowercase) is y
        # sets monthly_investment to a user input from 0 to 1000 while calling the get_number funciton
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number(
            "Enter yearly interest rate:\t", 0, 15)  # sets yearly_interest_rate to a user input from 0 to 15 while calling the get_number function
        # sets years to a user input from 0 to 50 while calling the get)integer function
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value while calling the caluclate_future_value_function
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print()  # display a space
        # display the calculated future_value rounded by 2 decimal places
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()  # display a space

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()  # display a space

    print("Bye!")  # display a goodbye message


    # if started as the main module, call the main function
if __name__ == "__main__":
    main()
