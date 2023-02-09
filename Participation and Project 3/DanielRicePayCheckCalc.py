print("Daniel Rice Pay Check Calculator App")  # Title of document
print()  # makes a space

# user inputs the amount of hours that they worked
hoursWorked = float(input("Hours Worked: "))
payRate = float(input("Hourly Pay Rate: "))  # user inputs their hourly pay
print()  # makes a space

# creates the variable grossPay based off of hours worked multiplied by hourly pay
grossPay = hoursWorked * payRate

print("Gross Pay: " + str(grossPay))  # displays the Gross Pay
taxRate = 18  # creates the variable taxRate
print("Tax Rate: " + str(taxRate) + "%")  # displays the tax rate
# creates the varbiale taxAmount based off of the Gross pay multiplied by the tax rate divided by 100
taxAmount = grossPay * (taxRate / 100)
print("Tax Amount: " + str(taxAmount))  # displays the tax amount
# creates the variable takeHomePay based off of the Gross pay minus the tax amount, and rounds the outcome by 2 decimal places
takeHomePay = round(grossPay - taxAmount, 2)
print("Take Home Pay: " + str(takeHomePay))  # displays the take home pay
