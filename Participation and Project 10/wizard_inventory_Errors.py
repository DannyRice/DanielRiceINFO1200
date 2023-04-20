import random  # added

ITEMS_FILENAME = "wizard_all_items.txt"  # missing "all"
INVENTORY_FILENAME = "wizard_inventory.txt"  # missing "I"


def read_items():
    items = []
    with open(ITEMS_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items


def read_inventory():
    inventory = []  # made into a list
    with open(INVENTORY_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            inventory.append(line)
    return inventory


def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")


def display_title():
    print("The Wizard Inventory program")
    print()


def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def walk(inventory):
    items = read_items()
    remaining_items = [i for i in items if i not in inventory]
    item = random.choice(remaining_items)
    print(f"While walking down a path, you see {item}.")  # took out extra "s"
    choice = input("Do you want to grab it? (y/n): ")
    while choice.lower == "y":  # replaced "if" with "while" and added .lower
        if len(inventory) >= 4:  # added =
            print("You can't carry any more items. Drop something first.\n")
        else:
            inventory.append(item)
            print(f"You picked up {item}.\n")
            write_inventory(inventory)  # missing a letter, tabbed over


def show(inventory):
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
    print()  # tabbed over


def drop_item(inventory):
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(inventory):
            print("Invalid item number.\n")
        else:
            item = inventory.pop(number-1)
            print(f"You dropped {item}.\n")
            write_inventory(inventory)
    except:
        pass


def main():
    display_title()
    display_menu()

    inventory = read_inventory()  # added paranthesis
    while True:
        command = input("Command: ")
        if command.lower() == "walk":  # added .lower
            walk(inventory)
        elif command.lower() == "show":  # added .lower
            show(inventory)
        elif command.lower() == "drop":  # added .lower
            drop_item(inventory)
        elif command.lower() == "exit":  # added .lower
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")  # spacing back


if __name__ == "__main__":
    main()
