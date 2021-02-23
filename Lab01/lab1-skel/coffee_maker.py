"""
A command-line controlled coffee maker.
"""

import sys
import io
import load_recipes

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

# Functions
def list():
    print(AMERICANO + ", " + CAPPUCCINO + ", " + ESPRESSO)


def resource_status():
    print(WATER + ": " + str(RESOURCES[WATER]) + "%")
    print(COFFEE + ": " + str(RESOURCES[COFFEE]) + "%")
    print(MILK + ": " + str(RESOURCES[MILK]) + "%")


def make_coffee():

    print("Which coffee?")
    coffeeType = sys.stdin.readline().rstrip("\n")

    load_recipes.load(coffeeType)
    
    if coffeeType != AMERICANO and coffeeType != ESPRESSO and coffeeType != CAPPUCCINO:
        print("Try again")

    elif int(RESOURCES[WATER]) >= int(load_recipes.utilities[0]) and int(RESOURCES[COFFEE]) >= int(load_recipes.utilities[1]) and int(RESOURCES[MILK]) >= int(load_recipes.utilities[2]):
        print("Here's your " + coffeeType + "!")
        RESOURCES[WATER] -= load_recipes.utilities[0]
        RESOURCES[COFFEE] -= load_recipes.utilities[1]
        RESOURCES[MILK] -= load_recipes.utilities[2]


def refill():
    print("Which resource? Type 'all' for refilling everything")
    resource = sys.stdin.readline().rstrip("\n")

    if resource == "all":
        RESOURCES[WATER] = 100
        RESOURCES[COFFEE] = 100
        RESOURCES[MILK] = 100
    else:
        RESOURCES[resource] = 100

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

print("I'm a smart coffee maker")
print("Enter command:")
command = sys.stdin.readline().rstrip("\n")

while command != EXIT and __name__ == "__main__":
    if command == LIST_COFFEES:
        list()

    elif command == RESOURCE_STATUS:
        resource_status()
    
    elif command == MAKE_COFFEE:
        make_coffee()
    
    elif command == REFILL:
        refill()


    print("Enter command:")
    command = sys.stdin.readline().rstrip("\n")
