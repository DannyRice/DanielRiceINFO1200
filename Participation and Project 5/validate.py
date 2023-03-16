#!/usr/bin/env python3
# Daniel Rice validation file for the Future Value App

def get_float(prompt, low, high):
    '''
    Validates the input number
    param: input prompt, lower number is set, higher number is set
    '''
    while True:  # infinite while loop
        # sets number as a floated input of the prompt
        number = float(input(prompt))
        if number > low and number <= high:  # if the number is greater than the low number and less than or equal to the high number
            return number  # sends the number variable back to it's caller
        else:  # if number doesn't meet the criteria
            print("Entry must be greater than", low,
                  "and less than or equal to", high)  # display error message


def get_int(prompt, low, high):
    '''
    Validates the input integer
    param: input prompt, lower number, higher number
    '''
    while True:  # infinite while loop
        # sets number as a floated input of the prompt
        number = int(input(prompt))
        if number > low and number <= high:  # if the number is greater than the low number and less than or equal to the high number
            return number  # sends the number variable back to it's caller
        else:  # if number doesn't meet the criteria
            print("Entry must be greater than", low,
                  "and less than or equal to", high)  # display error message


def main():
    '''
    Sets the value for a valid number input
    '''
    choice = "y"  # sets variable choice to "y"
    while choice.lower() == "y":  # while loop for as long as choice is "y"
        # sets valid number to the get_float function and sets limits to the lower number and higher number to 0 and 1000 respectively
        valid_number = get_float("Enter number: ", 0, 1000)
        # display the valid number input
        print("Valid Number = ", valid_number)
        print()  # makes a space

        # sets valid integer to the  get_int function and sets limits to the lower number and higher number to 0 and 50 respectively
        valid_integer = get_int("Enter integer: ", 0, 50)
        # display the valid integer input
        print("Valid Integer = ", valid_integer)
        print()  # makes a space
        choice = input("Repeat? (y/n): ")  # user input to restart program


print("Bye!")  # display goodbye message
# allows code to be executed as a script with top level scope
if __name__ == "__main__":
    main()
