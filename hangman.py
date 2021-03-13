# IMPORTS
import random
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
    randomWord = DATA[random.randint(1, 99)]
    print(randomWord)
    return randomWord


def getUserGuess():  # get the guess letter by user
    userInput = input("GUESS THE LETTER: ")
    return userInput

def checkTheGuess(guess, word, alreadyGuessed):
    if guess[0] in word:
        index = word.find(guess[0])
        indexedWord = alreadyGuessed[index]
        alreadyGuessed.replace(indexedWord, guess)
        return alreadyGuessed
    else:
        alreadyGuessed

def checkIfWin(alreadyGuessed, word):
    if alreadyGuessed == word:
        return True
    else:
        False

def mainLoop():  # main loop of program, runs out on zero turns
    # default turn count is 10
    turns = 10
    newRandomWord = getRandomWord() # newly generated random word
    userGuessedWord = "_ " * len(newRandomWord)  # user guessed word will be updated upon correct guess of user
    while turns != 0:
        turns -= 1  # on every iteration decrease a turn
        userGuess = getUserGuess().lower()
        userGuessedWord = checkTheGuess(userGuess, newRandomWord, userGuessedWord)
        if checkIfWin(userGuessedWord, newRandomWord):
            print("YOU WIN")
            break
        elif turns >= 1:
            return  #doNothingContinue
        else:
            print("YOU LOSE")
            break
        


def start():  # main starter of the program
    welcome()
    mainLoop()

# -------------------------------------------


# GLOBALLY CALLED FUNCTIONS
start()


# -------------------------------------------
