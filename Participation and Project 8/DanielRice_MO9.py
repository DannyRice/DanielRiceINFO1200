#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: March 29, 2023
# Project #: M09
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

def display_title():
    """Displays the title for the game
    """
    print("Daniel Rice's Wizard Inventory Game")  # Displays the title
    print("")  # displays a space


def display_menu():
    """Displays the layout and text of the menu options
    """
    print("")  # displays a space
    print("")  # displays a space
    print("COMMAND MENU")  # displays the menu section title
    print("")  # displays a space
    print("show - Show all items")  # displays a command option
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print("")  # displays a space


# sets the inventory variable to a list
inventory = ["Staff", "Boots", "Robes"]


def show(inventory):
    """I used to present the items from the inventory list

    Args:
        inventory (list): Items that the wizard carries
    """
    for number, item in enumerate(inventory, start=1):  # for each item in the inventory list
        print(f"{number}. {item}")  # print each item
        print("")  # displays a space


def grab_item(inventory):
    """Adds an item that the user inputs to the list (max of 4 items in inventory)

    Args:
        inventory (list): Items that the wizard carries
    """
    if len(inventory) >= 4:  # If the number of items is more than or equal to 4
        # display error message
        print("You can't carry any more items. Drop something first.\n")
    else:  # if not
        item = input("Name: ")  # user inputs an item anme
        inventory.append(item)  # item gets added to the list
        print(f"{item} was added.\n")  # displays a confirmation message


def edit_item(inventory):
    """Allows the user to edit a specific item in the wizard's inventory

    Args:
        inventory (list): Items that the wizard carries
    """
    number = int(input(
        "Number: "))  # user inputs item number to edit and store it in the number variable
    # if the number is 1 or more and less than the number of items in the inventory
    if number < 1 or number > len(inventory):
        print("Invalid item number.\n")  # Display error message
    else:  # if not
        # Allows the user to update the item name
        item = input("Updated name: ")
        # Sets the new item number and updates the name
        inventory[number-1] = item
        # displays update message
        print(f"Item number {number} was updated.\n")


def drop_item(inventory):
    # user inputs item number to remove and store it in the number variable
    number = int(input("Number: "))
    # if the number is 1 or more and less than the number of items in the inventory
    if number < 1 or number > len(inventory):
        print("Invalid item number.\n")  # Display error message
    else:  # if not
        item = inventory.pop(number-1)  # removes the item chosen
        print(f"{item} was dropped.\n")  # displays update message


def main():
    display_title()
    display_menu()
    while True:
        # command variable is set to the users input
        command = input("Command: ")
        if command == "show":  # if the user inputs the show command
            show(inventory)  # call the show function
        elif command == "grab":  # if the user inputs the grab command
            grab_item(inventory)  # call the grab item function
        elif command == "edit":  # if the user inputs the edit command
            edit_item(inventory)  # call the edit item function
        elif command == "drop":  # if the user inputs the drop command
            drop_item(inventory)  # call the drop function
        elif command == "exit":  # if the user inputs the exit command
            break  # stop the program
        else:
            # display error message
            print("Not a valid command. Please try again.\n")
    print("Bye!")  # display goodbye message


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
