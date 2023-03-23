#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 3/23/2023
# Project #: MO8_P1
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.


import tkinter as tk  # import the tkinter module as tk to help make widgets
# imports the tkinter module as ttk and messagebox to help make frames and add an error message
from tkinter import ttk, messagebox
import locale  # import locale to help with number formatting

# import the Pythagorean class from the triangle file
from triangle import Pythagorean


class CalculatorFrames(ttk.Frame):
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
        CalculatorFrame(parent).grid(row=0, column=0)
        # Create the 2nd parent grid on the right
        CalculatorFrame(parent).grid(row=0, column=1)

        # Add the Exit button along with it's position and size, that closes the entire GUI
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(
            row=1, column=1, sticky=tk.E, padx=15, pady=10)


class CalculatorFrame(ttk.Frame):
    """Class that holds the main code in a frame

    Args:
        ttk (module): A themed widget set that uses the frame widget
    """

    def __init__(self, parent):
        """Create a frame for the GUI

        Args:
            parent (variable): Set to the Pythagorean Class
        """
        ttk.Frame.__init__(
            self, parent, padding="10 10 10 10")  # call ttk.Frame to set margins for the GUI
        self.parent = parent  # give the self parameter to parent and set it to parent
        # give the self parameter to pythagorean and set it to the Pythagorean class
        self.pythagorean = Pythagorean()
        self.message = ""  # give the self parameter to message and make it blank

        # Define string variables for text entry fields
        self.A = tk.StringVar()  # sets A as a string variable
        self.B = tk.StringVar()  # sets B as a string variable
        self.C = tk.StringVar()  # sets C as a string variable

        self.initComponents()  # calls the initCompenents fucntion

    def initComponents(self):
        """Creates all the labels and their respective locations and size
        """

        # Display the grid of labels and text entry fields

        # Creates the label named A and sets the location
        ttk.Label(self, text="A: ").grid(
            column=0, row=0, sticky=tk.E)
        # Creates an entry box and sets it's input to the A variable, as well as the location and size
        ttk.Entry(self, width=25, textvariable=self.A).grid(
            column=1, row=0)

        # Creates the label named B and sets the location
        ttk.Label(self, text="B: ").grid(
            column=0, row=1, sticky=tk.E)
        # Creates an entry box and sets it's input to the B variable, as well as the location and size
        ttk.Entry(self, width=25, textvariable=self.B).grid(
            column=1, row=1)

        # Creates the label named C and sets the location
        ttk.Label(self, text="C: ").grid(
            column=0, row=3, sticky=tk.E)
        # Creates an entry box set to the C variable, sets the location and size, and makes it not editable
        ttk.Entry(self, width=25, textvariable=self.C,
                  state="readonly").grid(
            column=1, row=3)

        self.makeButtons()  # calls the makeButtons function

        for child in self.winfo_children():  # for loop that includes the child variables in winfo_children
            # sets grid layout as 5 by 3 pixels on the x and y axis respectively
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        """Function to create button frames using ttk.Button
        """
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the 4th row and the first column
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Create a button that uses the clear function, located on the 1st column and 1st row
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=0, row=0, padx=5)
        # Create a button that uses the calculate function,  located on the 2nd column and the 1st row
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=1, row=0)

    def get_float(self, val, fieldName):
        """Check the valididty of the inpuit float

        Args:
            val (Any): Return the validity of the user's input
            fieldName (Any): Calls the corresponding field name on the GUI

        Returns:
            str: validity
        """
        try:
            # tests if it can return the string with argument of val
            return float(val)
        except ValueError:  # if not, it's a bad argument
            # adds to the self.message variable whichever invalid field was input and displays an error message
            self.message += f"{fieldName} must be a valid number.\n"

    def clear(self):
        """Sets each field to be blank
        """
        self.A.set("")  # Set A to blank
        self.B.set("")  # Set B to blank
        self.C.set("")  # Set C to blank

    def calculate(self):
        """Calculates the input values and adds it to the madlib, shows errors if a mistake is made
        """
        self.message = ""   # clear any error message

        # Gets the A input and adds it to the pythagorean calculation, as well as checks if it is a valid number
        self.pythagorean.A = self.get_float(
            self.A.get(), "A")
        # Gets the B input and adds it to the pythagorean calculation, as well as checks if it is a valid number
        self.pythagorean.B = self.get_float(
            self.B.get(), "B")

        if self.message == "":  # if there are no errors
            # set the C box to the combined value of all the input variables
            self.C.set(self.pythagorean.calculateC())
        else:  # if there is an error
            # call messagebox module and has it display an error message
            messagebox.showerror("Error", self.message)


# sets main as top level scope
if __name__ == "__main__":
    root = tk.Tk()  # imported tk, set name as root
    root.title("Pythagorean Theorem Calculator")  # displays title
    CalculatorFrames(root)  # runs the Calculator class
    root.mainloop()  # call the mainloop of tk with the root variable
