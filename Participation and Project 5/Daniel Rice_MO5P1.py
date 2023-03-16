#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 2/22/2023
# Project #: MO5_P1
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
print("Daniel Rice's Even or Odd Checker")  # display title
print()  # makes a space


def is_even(num):
    '''
    Checks to see if the input number is even by checking for remainder
    param: num is input by the user
    '''
    if num % 2 <= 0:  # if the num remainder is less than or equal to 0
        return True  # send True back
    else:  # if not
        return False  # send False back


def main():
    '''
    Checks if the input integer is an even or odd number
    '''
    print("Daniel's even or odd checker")  # display title
    print()  # makes a sapce
    # user inputs a number to the variable my_num
    my_num = int(input("Enter an integer: "))
    if is_even(my_num):  # if the number is even
        True  # assign the true value
        print("This is an even number.")  # display the even number message
    else:  # if the number is not even
        False  # assign the false value
        print("This is an odd number.")  # print the odd number message


# allows code to be executed as a script with top level scope
if __name__ == "__main__":
    main()
