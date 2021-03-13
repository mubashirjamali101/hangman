#IMPORTS


#-------------------------------------------

#GLOBAL VARIABLED & OPERATIONS
username = "John"                           # default user name
turns = 10                                  # default turn count is 10
line = "-------------------------------"    # a default string to display line
character = {
    "1": "/  \\",
    "2": "/\\",
    "3": "\\ /",
    "4": "| |",
    "5": "/ \\",
    "6": "\\()/",
    "7": "\\()/_|",
    "8": "/",
    "9": "",
    "10": "",
}

#-------------------------------------------

#DEFINED FUNCTIONS
def welcome():
    username = getUserName()
    print(f"| WELCOME {username.upper()} |")
    print(f"{line}","\nENTER quit() OR q() TO EXIT",f"\n{line}")

def getUserName():                          #get the user name
    xUser = input("WHAT ARE YOU CALLED: ")
    if xUser != "":                         #   if username is not empty then set it at
        return xUser.lower()                #-> username or just let the defualt one

def decreaseTheTurn(turnsDecrease):         # get the left turns and minus one from them
    turnsDecrease -= 1
    return turnsDecrease



def main():                                 # main function of the program
    welcome()

#-------------------------------------------

#GLOBALLY CALLED FUNCTIONS


#-------------------------------------------

