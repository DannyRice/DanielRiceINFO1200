#!/usr/bin/env python3

# display a welcome message
print("Welcome to Daniel Rice's Future Value Calculator")
print()  # make a spaces

choice = "y"  # sets the choice variable to y
while choice.lower() == "y":  # starts a while loop if choice is equal to y
    is_valid = False  # sets the is_valid variable to false
    while is_valid == False:  # starts a while loop if is_valid is false

        # user inputs their monthly investment
        monthly_investment = float(input("Enter monthly investment:\t"))
        # if monthly investment input is greater than 0 and less than or equal to 1000
        if monthly_investment > 0 and monthly_investment <= 1000:
            is_valid = True  # then set is_valid to true
        else:  # if the input value is not in the set parameter, then print statement
            # prints statement
            print("Entry must be greater than 0 and less than 1000. Please try again.")
    is_valid = False  # resets variable to false
    while is_valid == False:  # starts another while loop if is_valid is false
        # user inputs the yearly interest rate
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        # if the yearly interest rate input is greater than 0 and less than or equal to 15
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = True  # then set is_valid to true
        else:  # if the input value is not in the set parameter, then print statement
            # pints the statement
            print("Entry must be greater than 0 and less than 15. Please try again.")
    is_valid = False  # resets is_valid to false
    while is_valid == False:  # starts another while loop if is_valid is false
        # user inputs the amount of years they want to see
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:  # If the years set is greater than 0 and less than 50
            is_valid = True  # then is_valid will become true
        else:  # if the input value is not in the set parameter, then print statement below
            # the staement that will be printed
            print("Entry must be greater than 0 and less than 50. Please try again.")
    print()  # makes a space

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12  # months is equal to years multiplied by 12

    # calculate the future value
    future_value = 0
    # for loop that starts at 1 and as it repeats, adds 1 to the month value
    for i in range(1, months + 1):
        # future value will add the monthly_investment value
        future_value += monthly_investment
        # the monthly interest amount is equal to the future value multiplied by the monthly interest rate
        monthly_interest_amount = future_value * monthly_interest_rate
        # the future value than adds the product of the monthly interest equation
        future_value += monthly_interest_amount
        if i % 12 == 0:  # if statement that puts the month and modulo 12 to get the remainder
            # print each of the months and their related future value, increasing each time
            print("Year = ", i // 12, "\tFuture Value = ", round(future_value, 2))

    print()  # makes a space

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()  # makes a space

print("Bye!")  # print a goodbye message
