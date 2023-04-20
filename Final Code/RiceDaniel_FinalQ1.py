#!/usr/bin/env python3


def sales_tax(total):
    """Calculate the Sales Tax value

    Args:
        total (float): User input total

    Returns:
        variable: total multiplied by tax
    """
    tax = 0.06  # set tax variable to 0.06
    sales_tax = total * tax  # calculate sales_tax variable by multiplying total by tax
    return sales_tax  # return the sales_tax variable


def main():
    """Sales Tax calculator main program
    """
    print("Sales Tax Calculator\n")  # display title
    # set total variable to float the user input
    total = float(input("Enter total: "))
    # set total_after_tax variable to total added to the calling the sales_tax funciton, all rounded by 2 decimal places
    total_after_tax = round(total + sales_tax(total), 2)
    # display the calculation results
    print("Total after tax: ", total_after_tax)


# set main as top level scope
if __name__ == "__main__":
    main()
