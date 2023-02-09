print("Daniel Rice's Tip Calculator App")  # Program name
print()  # makes a space

# user inputs the cost of their meal
costOfMeal = float(input("Cost of meal: "))
# user inputs the tip percent they would like to pay
tipPercentage = float(input("Tip Percent: "))
print()  # makes a space

# multiplies the cost of the meal multiplied by the tip percentage divided by 100, and rounded to the second decimal place
tipAmount = round(costOfMeal * (tipPercentage / 100), 2)
print("Tip amount: " + str(tipAmount))  # displays the calculated tip amount
# adds the tip amount to the cost of the meal, rounded to the second decimal place
totalAmount = round(costOfMeal + tipAmount, 2)
# displays the total cost of the meal
print("Total amount: " + str(totalAmount))
