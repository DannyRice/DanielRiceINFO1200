#!/usr/bin/env python3
print("Daniel Rice's Test Scores App") #print my name and my app

# display a welcome message
print("The Test Scores program") # shows the welcome message
print()#makes a space
print("Enter 3 test scores") #shows instructions
print("======================") #makes a divider made out of = signs

# get scores from the user
score1 = int(input("Enter test score: ")) #input for variable score1
score2 = int(input("Enter test score: "))#input for variable score2
score3= int(input("Enter test score: "))#input for variable score3

# calculate average score
average_score = round((score1 + score2 + score3) / 3) #rounds the average of all the scores

#calculate total score
total_score = score1 + score2 + score3 #the sum of all the scores
             
# format and display the result
print("======================")#makes a divider made out of = signs
print("Your Scores: ", str(score1), str(score2), str(score3))# prints all the inputed scores
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score) #Prints both the total score and the average score
print()
print("Bye") #shows the goodbye message


