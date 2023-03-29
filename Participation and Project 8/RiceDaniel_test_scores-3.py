#!/usr/bin/env python3

def display_welcome():
    """Display a welcome message
    """
    print("The Test Scores program")  # display the title
    print("Enter 'x' to exit")  # display the exit option
    print("")  # display a space


def get_scores():
    """Used to add together all input scores and place them in a list

    Returns:
        variable: scores - list of integers
    """
    scores = []  # set scores variable to an empty list
    while True:  # infinite while loop
        # user inputs numbers into the score variable
        score = input("Enter test score: ")
        if score == "x":  # if the input is x
            return scores  # return the scores list
        else:  # if not
            score = int(score)  # sets the score variable to int(score)
            if score >= 0 and score <= 100:  # if the score value si less than or equal to 0 or greater than or equal to 100
                scores.append(score)  # add a new score to the list
            else:  # if not
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")  # display error message


def process_scores(scores):
    """Processes the input scores, and displays the results of the calculations

    Args:
        scores (list): a list created by user input
    """

    total = 0  # sets total variable to 0
    for score in scores:  # for the user input score(s) in scores
        total += score  # add each score to the total variable

    num_scores = len(scores)  # find the number of scores

    average = total / num_scores  # calculate average score
    # calculate median score
    median_index = num_scores // 2  # calculate the median score
    median = 0  # sets median variable to 0
    if num_scores % 2 == 1:  # check if the list has an odd amount of scores
        # sets median to the scores list of median_index
        median = scores[median_index]

    else:  # if not
        # sets middle_1 to the scores list of median_index
        middle_1 = scores[median_index]
        # sets middle_2 to the scores list of median_index but minus 1
        middle_2 = scores[median_index-1]
        # sets median variable as both the middle values divided by 2
        median = (middle_1 + middle_2) / 2

    # format and display the result
    print("")  # display a space
    print("Score total:       ", total)  # display the score total
    print("Number of Scores:  ", num_scores)  # display the number of scores
    print("Average Score:     ", average)  # display the average of scores
    print("Median Score       ", median)  # display the median of scores
    print("Highest Score      ", max(scores))  # display the highest score
    print("Lowest Score       ", min(scores))  # display the lowest score


def main():
    """The main program meant to calculate the total score, number of scores, average, min, max, and median
    """
    display_welcome()  # calls the display_welcome function
    # get list form the get_scores function
    scores = get_scores()
    # get values from the scores list using the process_scores function
    process_scores(scores)
    print("")  # display a spacae
    print("Bye!")  # display a goodbye message


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
