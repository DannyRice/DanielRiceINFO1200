#!/usr/bin/env python3

import csv  # allow use of csv module
import sys  # allow use of sys module

FILENAME = "movies_test.csv"  # global constant for filename


def exit_program():
    """Stops the program
    """
    print("Terminating program.")  # display termination message
    sys.exit()  # closes the program


def read_movies():
    """Open and interact with csv file

    Returns:
        list: contains input movies
    """
    try:  # try to open the file and read it
        movies = []  # make movies an empty list
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)  # set csv reader to the reader variable
            for row in reader:  # for each row
                movies.append(row)  # add movies to the list
        return movies  # return list
    except FileNotFoundError as e:  # exception for file not found
        # print(f"Could not find {FILENAME} file.")
        # exit_program()
        return movies  # return list
    except Exception as e:  # exception for catching all exceptions
        print(type(e), e)  # print exception type
        exit_program()  # call exit_program function


def write_movies(movies):
    try:  # try to open the file for writing
        with open(FILENAME, "w", newline="") as file:  # open the file using a writer object
            # raise BlockingIOError("Test the OSError exception.")
            # call the csv module to write the files and assign it to the writer variable
            writer = csv.writer(file)
            # write the passed in movies paramter to the file
            writer.writerows(movies)
    except OSError as e:  # exception for OS realted errors
        print(type(e), e)  # print the error emssage
        exit_program()  # call exit_program funciton
    except Exception as e:  # exception for catching all exceptions
        print(type(e), e)  # print exception type
        exit_program()  # call exit_program function


def list_movies(movies):
    """Displays all the added movies in the list

    Args:
        movies (list): holds movies and their information
    """
    for i, movie in enumerate(movies, start=1):  # for every movie in the list
        # print out the movie information
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()  # display a space


def add_movie(movies):
    """Adds a movie to the list

    Args:
        movies (list): holds movies and their information
    """
    name = input("Name: ")  # Gets user input for movie name
    while True:  # infinite while loop
        try:  # try to check if year is a valid number
            year = int(input("Year: "))  # user inputs year
        except ValueError:  # exception for user input
            print("Invalid year. Please try again.")  # display error message
            continue  # loop back
        if year <= 0:  # if year is less than or equal to
            # display error message
            print("Year must be greater than zero. Please try again.")
            continue  # loop back
        else:  # if year is valid
            break  # end the loop

    movie = [name, year]  # sets parameters for movie list
    movies.append(movie)  # adds the movie to the list
    write_movies(movies)  # write the list to the csv file
    print(f"{name} was added.\n")  # display confirmation message


def delete_movie(movies):
    """Delets a movie from the list

    Args:
        movies (list): holds movies and their information
    """
    while True:  # infinite while loop
        try:  # try to get a number from the user
            number = int(input("Number: "))  # user inputs a number
        except ValueError:  # exception for user input
            # display error message
            print("Invalid integer. Please try again.")
            continue  # loop back
        # if number is less than 1 or shorter than the list length
        if number < 1 or number > len(movies):
            # display error message
            print("There is no movie with that number. Please try again.")
        else:  # if nubmer is valid
            break  # end loop
    # get rid of the list item (-1 because user input can't have 0)
    movie = movies.pop(number - 1)
    write_movies(movies)  # write the change to the file
    print(f"{movie[0]} was deleted.\n")  # display confirmation message


def display_menu():
    """Menu layout of commands
    """
    print("The Movie List program")  # display title
    print()  # display a space
    print("COMMAND MENU")  # display menu title
    print("list - List all movies")  # display list command
    print("add -  Add a movie")  # display add command
    print("del -  Delete a movie")  # display delete command
    print("exit - Exit program")  # display exit command
    print()  # display a space


def main():
    """Runs the movie program
    """
    display_menu()  # calls the display menu function
    movies = read_movies()  # sets movies variable to the read_movies function
    while True:  # infinte while loop
        command = input("Command: ")  # user inputs a command
        if command.lower() == "list":  # if user inputs list
            list_movies(movies)  # call list_movies function
        elif command.lower() == "add":  # if user inputs add
            add_movie(movies)  # call add_movie function
        elif command.lower() == "del":  # if user inputs del
            delete_movie(movies)  # call delete_movie function
        elif command.lower() == "exit":  # if user inputs exit
            break  # end program
        else:  # if invalid command
            # display error message
            print("Not a valid command. Please try again.\n")
    print("Bye!")  # display goodbye message


# set main as top level scope
if __name__ == "__main__":
    main()
