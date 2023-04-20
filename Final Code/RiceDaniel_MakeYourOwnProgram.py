#!/usr/bin/env python3

import csv  # allow use of csv module
import sys  # allow use of sys module

FILENAME = "games_list.csv"  # global constant for filename


def exit_program():
    """Stops the program
    """
    print("Terminating program.")  # display termination message
    sys.exit()  # closes the program


def read_games():
    """Open and interact with csv file

    Returns:
        list: contains input games
    """
    try:  # try to open the file and read it
        games = []  # make games an empty list
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)  # set csv reader to the reader variable
            for row in reader:  # for each row
                games.append(row)  # add games to the list
        return games  # return list
    except FileNotFoundError as e:  # exception for file not found
        return games  # return list
    except Exception as e:  # exception for catching all exceptions
        print(type(e), e)  # print exception type
        exit_program()  # call exit_program function


def write_games(games):
    try:  # try to open the file for writing
        with open(FILENAME, "w", newline="") as file:  # open the file using a writer object
            # raise BlockingIOError("Test the OSError exception.")
            # call the csv module to write the files and assign it to the writer variable
            writer = csv.writer(file)
            # write the passed in games parameter to the file
            writer.writerows(games)
    except OSError as e:  # exception for OS realted errors
        print(type(e), e)  # print the error emssage
        exit_program()  # call exit_program funciton
    except Exception as e:  # exception for catching all exceptions
        print(type(e), e)  # print exception type
        exit_program()  # call exit_program function


def list_games(games):
    """Displays all the added games in the list

    Args:
        games (list): holds games and their information
    """
    for i, game in enumerate(games, start=1):  # for every game in the list
        # print out the game information
        print(
            f"{i}. {game[0]} ({game[1]}, ${game[2]}, {game[3]} million copies sold)")
    print("")  # display a space


def add_game(games):
    """Adds a game to the list

    Args:
        game (list): holds games and their information
    """
    name = input("Name: ")  # Gets user input for game name
    while True:  # infinite while loop
        try:  # try to check if year is a valid number
            year = int(input("Year: "))  # user inputs year
        except ValueError:  # exception for user input
            print("Invalid year. Please try again.")  # display error message
            continue  # loop back
        if year <= 0:  # if year is less than or equal to zero
            # display error message
            print("Year must be greater than zero. Please try again.")
            continue  # loop back
        else:  # if year is valid
            break  # end the loop
    while True:  # another infinite while loop
        try:  # try to check if price is a valid number
            price = round(float(input("Price: ")), 2)  # user inputs price
        except ValueError:  # exception for user input
            print("Invalid price. Please try again.")  # display error message
            continue  # loop back
        if price <= 0:  # if price is less than or equal to zero
            # display error message
            print("Price must be greater than zero. Please try again.")
            continue  # loop back
        else:  # if year is valid
            break  # end the loop
    while True:  # what's this? another infinite while loop?
        try:  # try to check if copies_sold is a valid number
            # user inputs copies sold
            copies_sold = round(
                float(input("Copies Sold(in the millions): ")), 3)
        except ValueError:  # exception for user input
            print("Invalid number. Please try again.")  # display error message
            continue  # loopdeedoop back
        if copies_sold <= 0:  # if copies_sold is less than or equal to zero
            # display error message
            print("Copies Sold must be greater than zero. Please try again.")
            continue  # loop back
        else:  # if year is valid
            break  # end the loop, finally

    game = [name, year, price, copies_sold]  # sets parameters for game list
    games.append(game)  # adds the game to the list
    write_games(games)  # write the list to the csv file
    print(f"{name} was added.\n")  # display confirmation message


def delete_game(games):
    """Delets a game from the list

    Args:
        games (list): holds games and their information
    """
    while True:  # infinite while loop
        try:  # try to get a number from the user
            number = int(input("Number: "))  # user inputs a number
        except ValueError:  # exception for user input
            # display error message
            print("Invalid integer. Please try again.")
            continue  # loop back
        # if number is less than 1 or shorter than the list length
        if number < 1 or number > len(games):
            # display error message
            print("There is no game with that number. Please try again.")
        else:  # if number is valid
            break  # end loop
    # get rid of the list item (-1 because user input can't have 0)
    game = games.pop(number - 1)
    write_games(games)  # write the change to the file
    print(f"{game[0]} was deleted.\n")  # display confirmation message


def display_menu():
    """Menu layout of commands
    """
    print("Daniel Rice's Game Inventory Program")  # display title with my name
    print()  # display a space
    print("COMMAND MENU")  # display menu title
    print("list - List all games")  # display list command
    print("add -  Add a game")  # display add command
    print("del -  Delete a game")  # display delete command
    print("exit - Exit program")  # display exit command
    print()  # display a space


def main():
    """Runs the game program
    """
    display_menu()  # calls the display menu function
    games = read_games()  # sets games variable to the read_games function
    while True:  # infinte while loop
        command = input("Command: ")  # user inputs a command
        if command.lower() == "list":  # if user inputs list
            list_games(games)  # call list_games function
        elif command.lower() == "add":  # if user inputs add
            add_game(games)  # call add_game function
        elif command.lower() == "del":  # if user inputs del
            delete_game(games)  # call delete_game function
        elif command.lower() == "exit":  # if user inputs exit
            break  # end program
        else:  # if invalid command
            # display error message
            print("Not a valid command. Please try again.\n")
    print("Bye Bye!")  # display goodbye message


# set main as top level scope
if __name__ == "__main__":
    main()
