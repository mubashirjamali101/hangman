# IMPORTS
from wordlist import DATA  # importing 100 random unique meaningful words

# -------------------------------------------

# GLOBAL VARIABLED & OPERATIONS
line = "-------------------------------"    # a default string to display line
randomWordList = []

# -------------------------------------------

# DEFINED FUNCTIONS


def welcome():  # Initial intro and few basic function
    username = getUserName()
    print(f"| WELCOME {username.upper()} TO GUESS THE WORD |")
    print(f"{line}", "\nENTER quit() OR q() TO EXIT", f"\n{line}")


def getUserName():                          # get the user name
    xUser = input("WHAT ARE YOU CALLED: ")
    if xUser != "":                         # if username is not empty then set it at
        return xUser.lower()                # -> username or just let the defualt one
    else:
        return "Guest"

# get the left turns and minus one from them
# def decreaseTheTurn(turnsDecrease):
#     turnsDecrease -= 1
#     return turnsDecrease


def getRandomWord():  # function to get new random word
    return "Dummy"


def mainLoop():  # main loop of program, runs out on zero turns
    turns = 10
    # default turn count is 10
    newRandomWord = getRandomWord()

    while turns != 0:
        turns -= 1  # on every iteration decrease a turn


def start():  # main starter of the program
    welcome()
    mainLoop()

# -------------------------------------------


# GLOBALLY CALLED FUNCTIONS
start()

# -------------------------------------------
