# Name: (First Name Last Name)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date:
# Project #: M11
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import csv  # import csv module

FILENAME = "contacts.csv"  # set variable to csv filename


def display_title():
    """Generate the title for the program
    """
    print("Daniel Rice's Contact Manager App")  # display title
    print("")  # display a space


def display_menu():
    """Generate command menu for the program
    """
    print("\nCOMMAND MENU")  # display menu title
    print("")  # display a space
    print("list - Display all contacts")  # display list command
    print("view - View a contact")  # display view command
    print("add - Add a contact")  # display add command
    print("del - Delete a contact")  # display delete command
    print("exit - Exit program")  # display exit command
    print("")  # display a space


def read_contacts():
    """Read the contacts from the csv

    Returns:
        list: contains the contact info
    """
    contacts = []  # make contacts list that is empty
    try:  # try to read the file
        with open(FILENAME, "r", newline="") as file:  # open the csv file in read mode
            # call csv module to read the csv file and set it as a variable
            reader = csv.reader(file)
            for row in reader:  # for each row in the csv file
                contacts.append(row)  # add contacts to the list
    except FileNotFoundError:  # exception for file not found
        # display error message
        print("Could not find contacts file! Starting new contacts file...")
    return contacts  # return list


def display(contacts):
    """Display the contact list

    Args:
        contacts (list): contains the contact info
    """
    if len(contacts) == 0:  # if the list has no items
        print("There are no contacts in the list")  # display update message
        return  # return to command menu
    else:  # if there are items in the list
        for i, row in enumerate(contacts, start=1):  # for each item in the list
            print(f"{i}. {row[0]}")  # display each contact
        print("")  # display a space


def view(contacts):
    """View the information in the list for a contact

    Args:
        contacts (list): contains the contact info
    """
    number = get_contact_number(
        contacts)  # calls the get contact number function
    if number > 0:  # if the user inputs a number greater than 0
        # subtract that number by 1 for list conversion purposes
        contact = contacts[number-1]
        print("Name:", contact[0])  # display contact name
        print("Email:", contact[1])  # display the contact email
        print("Phone:", contact[2])  # display the contact phone number
        print("")  # display a space


def get_contact_number(contacts):
    """Gets the user's input to choose which contact they want to see

    Args:
        contacts (list): contains the contact info

    Returns:
        int: User inputs a number 
    """
    while True:  # infinte while koop
        try:  # try to get a user input number
            # set number variable as user input integer
            number = int(input("Number: "))
        except ValueError:  # exception for value error
            print("Invalid integer.\n")  # display error message
            return -1  # return number -1

        # if the number is less than 1 or greater than the number of contacts in the list
        if number < 1 or number > len(contacts):
            print("Invalid contact number.\n")  # display error message
            return -1  # return number -1
        else:  # if it's valid
            return number  # return number variable


def add(contacts):
    """Allows user ot add a contact and their information to the csv file / list

    Args:
        contacts (list): contains the contact info
    """
    name = input("Name: ")  # user inputs a name
    email = input("Email: ")  # user inputs an email
    phone = input("Phone: ")  # user inputs a phone number
    contact = []  # set contact as an empty list
    contact.append(name)  # add the input name to the list
    contact.append(email)  # add the input email to the list
    contact.append(phone)  # add the input phone number to the list
    contacts.append(contact)  # add the contact list to the contacts list
    write_contacts(contacts)  # write the changes to the csv file
    print(f"{contact[0]} was added.")  # display update


def write_contacts(contacts):
    """Adds changes to the csv file

    Args:
        contacts (list): contains the contact info
    """
    with open(FILENAME, "w", newline="") as file:  # open the file in write mode
        # set writer to call the csv module to change the file
        writer = csv.writer(file)
        writer.writerows(contacts)  # adds info to new row


def delete(contacts):
    """Allows user to delete a contact from the file

    Args:
        contacts (list): contains the contact info
    """
    number = get_contact_number(
        contacts)  # set number variable to call the get_contact_number function
    if number > 0:  # if number variable is greater than 0
        contact = contacts.pop(number-1)  # take out contact from list
        print(f"{contact[0]} was deleted.\n")  # display update message
    write_contacts(contacts)  # write changes to the file


def main():
    """Runs the contacts program
    """
    contacts = read_contacts()  # sets contacts to call the read_contacts funciton
    display_title()  # call display_title function
    display_menu()  # call display_menu function
    while True:  # infinte while loop
        command = input("Command: ")  # set command to user input
        if command.lower() == "list":  # if user inputs list command
            display(contacts)  # call display function
        elif command.lower() == "view":  # if user inputs view command
            view(contacts)  # call view function
        elif command.lower() == "add":  # if user inputs add command
            add(contacts)  # call add function
        elif command.lower() == "del":  # if user inputs delete command
            delete(contacts)  # call delete function
        elif command.lower() == "exit":  # if user inputs exit command
            break  # end program
        else:  # if invalid command was input
            # display error message
            print("Not a valid command. Please try again.\n")
    print("Bye!")  # display goodbye message


# set top level scope to main
if __name__ == "__main__":
    main()
