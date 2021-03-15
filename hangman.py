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


def getRandomWord():  # function to get new random word
    randomWord = DATA[random.randint(1, 99)]
    return randomWord.lower()


def getUserGuess():  # get the guess letter by user
    userInput = input("GUESS THE LETTER: ")

    if userInput.lower() == "quit()" or userInput.lower() == "q()":
        quit()
    elif(len(userInput) == 1):
        return userInput.lower()
    elif userInput == "" or len(userInput) != 1:
        print(f"YOUR INPUT \"{userInput}\" IS NOT VALID")
        return "invalid"
    else:
        return "invalid"


def checkTheGuess(guess, word, alreadyGuessed):
    for l in alreadyGuessed:
        char = l[0]
        if guess == char:
            alreadyGuessed[l] = guess
    return alreadyGuessed


def getListFromWord(word):
    listFromWord = {}
    i = 0

    for a in word:
        i += 1
        id = a+f"{i}"
        listFromWord[id] = "_ "
    return listFromWord


def arrayToString(array):
    stringFormed = ""

    for char in array:
        stringFormed += array[char]
    return stringFormed


def getTurns(word):
    size = len(word)
    if size <= 10:
        return 12
    else:
        return size*(int(size/2))


def mainLoop():  # main loop of program, runs out on zero turns
    newRandomWord = getRandomWord()  # newly generated random word
    guessedWordInMemory = getListFromWord(newRandomWord)  # var to put correct user guesses
    guessedWordString = arrayToString(guessedWordInMemory)
    turns = getTurns(newRandomWord)  # default turn count is 10
    print(line)

    while turns != 0:
        turns -= 1  # on every iteration decrease a turn
        print(f"TURNS LEFT: {turns}")
        Guess = getUserGuess()

        if Guess != "invalid" and len(Guess) == 1:
            guessedWordInMemory = checkTheGuess(
                Guess, newRandomWord, guessedWordInMemory)
            guessedWordString = arrayToString(guessedWordInMemory)

        print(f"GUESSED: {guessedWordString}")

        if guessedWordString == newRandomWord:
            print("YOU WIN :)")
            user_input = input("PLAY AGAIN [y/n]")
            if user_input.lower() == "y":
                start()
            else:
                break
        elif turns == 0:
            print("YOU LOSE, THE WORD WAS ", newRandomWord)
            user_input = input("PLAY AGAIN [y/n]")
            if user_input.lower() == "y":
                start()
            else:
                break
        print(line)


def start():  # main starter of the program
    mainLoop()

# -------------------------------------------

#GLOBALLY CALLED FUNCTIONS
welcome()
start()


# -------------------------------------------
