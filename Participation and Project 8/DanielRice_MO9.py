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


def main():
    display_title
    display_menu
