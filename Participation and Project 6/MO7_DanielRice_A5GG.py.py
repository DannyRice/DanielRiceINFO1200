#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 3/14/2023
# Project #: MO7_P2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import random  # imports the default random file


def display_title():
    '''
    Displays the title of the program
    '''
    print("Guess the number!")  # display message
    print()  # display a space


def get_limit():
    '''
    Get's the user's input for the upper limit of the range of numbers
    '''
    limit = int(input("Enter the upper limit for the range of numbers: ")
                )  # Sets limit variable value to user input
    return limit  # sends limit back


def play_game(limit):
    ''' 
    Calls the random function and sets a limit to it, which in input by the user

    param:
        limit - integer input by the user as the max value of the number range
    '''
    count = 0  # sets count variable to 0
    # sets number variable to the called function random.randint with 1 to the input limit parameters
    number = random.randint(1, limit)
    # display message with limit variable value
    print(f"I'm thinking of a number from 1 to {limit}\n")

    while True:  # infinite while loop
        # sets the guess variable to an integer input by the user
        guess = int(input("Your guess: "))
        if guess < number:  # if statement if input guess variable is less than the random number
            print("Too low.")  # display message
            count += 1  # adds 1 to the count variable
        elif guess > number:  # elif statement if input guess variable is greater than the random number
            print("Too high.")  # display message
            count += 1  # adds 1 to the count variable
        else:  # if none of the above conditions are met
            guess == number  # when the input guess is == to the random number
            count += 1  # adds 1 to the count variable
            # displays victory message with count variable
            print(f"You guessed it in {count} tries.\n")
            return  # resets loop


def main():
    '''
    Main program that displays the title, has user set limit, and plays the game
    '''
    display_title()  # calls function that displays title

    again = "y"  # sets again variable to "y"
    while again.lower() == "y":  # while loop for when again is set to "y"
        limit = get_limit()  # sets limit variable to the called get_limit function
        # calls the play_game fuction with the input limit variable
        play_game(limit)

        # sets again variable to user input
        again = input("Play again? (y/n): ")
        print()  # dsiplays a space
    print("Bye!")  # display goodbye message


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
