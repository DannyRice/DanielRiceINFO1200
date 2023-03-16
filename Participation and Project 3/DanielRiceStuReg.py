# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Crandall)
# Date: Feb 11, 2023
# Project #: MO3
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
print("Daniel Rice Student Registration")  # Title of document
print()  # makes a space

first_name = (input("First name: "))  # user inputs first name
last_name = (input("Last name: "))  # User inputs last name
birth_year = (input("Birth year: "))  # User inputs birth year
print()  # makes a space

tempPassword = first_name + '*' + birth_year

# Prints the welcome message with the users full name and birth year
print('Welcome ' + str(first_name) + ' ' + str(last_name) + '!')
print()  # makes a space

print("Your registration is complete.")  # shows text
# shows temporary password based off of user's input first name, an asterisk, and birth year
print("Your temporary password is: " + tempPassword)
