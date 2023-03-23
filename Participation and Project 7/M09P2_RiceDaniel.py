#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 3/23/2023
# Project #: MO8_P2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import tkinter as tk  # import the tkinter module as tk to help make widgets
# imports the tkinter module as ttk and messagebox to help make frames and add an error message
from tkinter import ttk, messagebox

from combine import MadLib  # import the MadLib class from the combine file


class extraMadLibFrame(ttk.Frame):
    """Class that hold multiple parent frames

    Args:
        ttk (module): A themed widget set that uses the frame widget
    """

    def __init__(self, parent):
        """Creates 2 grid frames in the GUI

        Args:
            parent (Any): The main grid frame
        """
        ttk.Frame.__init__(self, parent)  # sets the code to add a frame

        # Create the parent grid on the left
        mainMadLibFrame(parent).grid(row=0, column=0)
        # Create the 2nd parent grid on the right
        mainMadLibFrame(parent).grid(row=0, column=1)

        # Add the Exit button along with it's position and size, that closes the entire GUI
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(
            row=1, column=1, sticky=tk.E, padx=15, pady=10)


class mainMadLibFrame(ttk.Frame):
    """CLass that holds the main code in a frame

    Args:
        ttk (module): A themed widget set that uses the frame widget
    """

    def __init__(self, parent):
        """Create a frame for the GUI

        Args:
            parent (variable): Set to the MadLib Class
        """
        ttk.Frame.__init__(
            self, parent, padding="20 20 20 20")  # call ttk.Frame to set margins for the GUI
        self.parent = parent  # give the self parameter to parent and set it to parent
        # give the self parameter to combination and set it to the Madlib class and set those parameters as blank
        self.combination = MadLib("", "", "", "")
        self.message = ""  # give the self parameter to message and make it blank

        # Define string variables for text entry fields
        self.noun1 = tk.StringVar()  # sets noun1 as a string variable
        self.noun2 = tk.StringVar()  # sets noun2 as a string variable
        self.verb1 = tk.StringVar()  # sets verb1 as a string variable
        self.verb2 = tk.StringVar()  # sets verb2 as a string variable
        self.madlib = tk.StringVar()  # sets madlib as a string variable

        self.initComponents()  # calls the initCompenents fucntion

    def initComponents(self):
        """Creates all the labels and their respective locations and size
        """

        # Display the grid of labels and text entry fields

        # Creates the label named Noun #1 and sets the location
        ttk.Label(self, text="Noun #1:").grid(
            column=0, row=0, sticky=tk.E)
        # Creates an entry box and sets it's input to the noun1 variable, as well as the location and size
        ttk.Entry(self, width=25, textvariable=self.noun1).grid(
            column=1, row=0)

        # Creates the label named Noun #2 and sets the location
        ttk.Label(self, text="Noun #2:").grid(
            column=0, row=1, sticky=tk.E)
        # Creates an entry box and sets it's input to the noun2 variable, as well as the location and size
        ttk.Entry(self, width=25, textvariable=self.noun2).grid(
            column=1, row=1)

        # Creates the label named Verb #1 and sets the location
        ttk.Label(self, text="Verb #1:").grid(
            column=0, row=2, sticky=tk.E)
        # Creates an entry box and sets it's input to the verb1 variable, as well as the location and size
        ttk.Entry(self, width=25, textvariable=self.verb1).grid(
            column=1, row=2)

        # Creates the label named Verb #2 and sets the location
        ttk.Label(self, text="Verb #2:").grid(
            column=0, row=3, sticky=tk.E)
        # Creates an entry box and sets it's input to the verb2 variable, as well as the location and size
        ttk.Entry(self, width=25, textvariable=self.verb2).grid(
            column=1, row=3)

        # Creates the label named Mad Lib: and sets the location
        ttk.Label(self, text="Mad Lib:").grid(
            column=0, row=4, sticky=tk.E)
        # Creates an entry box set to the madlib variable, sets the location and size, and makes it not editable
        ttk.Entry(self, width=50, textvariable=self.madlib,
                  state="readonly").grid(
            column=1, row=4)

        self.makeButtons()  # calls the makeButtons function

        for child in self.winfo_children():  # for loop that includes the child variables in winfo_children
            # sets grid layout as 10 by 10 pixels on the x and y axis respectively
            child.grid_configure(padx=10, pady=10)

    def makeButtons(self):
        """Function to create button frames using ttk.Button
        """
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the 5th row and the first column
        buttonFrame.grid(column=0, row=5, columnspan=2, sticky=tk.E)

        # Create a button that uses the clear function, located on the 3rd column and 6th row
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=2, row=6, padx=5)
        # Create a button that uses the calculate function,  located on the 2nd column and the 6th row
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=1, row=6)

    def get_str(self, val, fieldName):
        """Checks the valididty of the input string

        Args:
            val (Any): Return the validity of the user's input
            fieldName (Any): Calls the corresponding field name on the GUI

        Returns:
            str: validity
        """
        try:
            # tests if it can return the string with argument of val
            return str(val)
        except ValueError:  # if not, it's a bad argument
            # adds to the self.message variable whichever invalid field was input and displays an error message
            self.message += f"{fieldName} must be a valid word.\n"

    def clear(self):
        """Sets each field to be blank
        """
        self.noun1.set("")  # Set noun1 to blank
        self.noun2.set("")  # Set noun2 to blank
        self.verb1.set("")  # Set verb1 to blank
        self.verb2.set("")  # Set verb2 to blank
        self.madlib.set("")  # Set madlib to blank

    def calculate(self):
        """Calculates the input values and adds it to the madlib, shows errors if a mistake is made
        """
        self.message = ""  # clear any error message

        # Gets the noun1 input and adds it to the madlib calculation, as well as checks if it is a valid string
        self.combination.noun1 = self.get_str(
            self.noun1.get(), "Noun #1")
        # Gets the noun2 input and adds it to the madlib calculation, as well as checks if it is a valid string
        self.combination.noun2 = self.get_str(
            self.noun2.get(), "Noun #2")
        # Gets the verb1 input and adds it to the madlib calculation, as well as checks if it is a valid string
        self.combination.verb1 = self.get_str(
            self.verb1.get(), "Verb #1")
        # Gets the verb2 input and adds it to the madlib calculation, as well as checks if it is a valid string
        self.combination.verb2 = self.get_str(
            self.verb2.get(), "Verb #2")

        if self.message == "":  # if there are no errors
            # set the madlib box to the combined value of all the input variables
            self.madlib.set(self.combination.combineMadlib())
        else:  # if there is an error
            # call messagebox module and has it display an error message
            messagebox.showerror("Error", self.message)


# sets main as top level scope
if __name__ == "__main__":
    root = tk.Tk()  # imported tk, set name as root
    root.title("Mad Libs")  # displays title
    extraMadLibFrame(root)  # runs the extraMadLibFrame class
    root.mainloop()  # call the mainloop of tk with the root variable
