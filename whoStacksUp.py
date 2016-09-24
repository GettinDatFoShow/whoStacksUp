import random
import stack
import time

def stackCreate(stackSize):
    "returns a stack of the size requested"
    resultStack = stack.Stack()
    randomNum = 0
    for i in range(stackSize):
        randomNum = random.randint(1,10)
        resultStack.push(randomNum)
    return resultStack

def checkChoice(choice):
    try:
        result = int(choice)
    except ValueError:
        return 0
    if result >= 2:
        return 2
    else:
        return 1


def game(stackSize):
    CHOICE = 0 # Set Game State
    numStack = stackCreate(stackSize) # randomize creation of stack size
    player1sum = 0 # player 1 total
    player2sum = 0 # player 2 total
    player1 = input("Player 1, Enter your name: ")
    print("\n Thank you. \n")
    player2 = input("Player 2, Enter your name: ")
    print("\n Thank you. Ok, lets get started. \n")
    print(" Each player may choose 1 or 2 numbers per turn from the stack, the player ")
    print("with the highest sum of integers chosin from the stack wins. ")
    print("\n" + "="*7 + " Lets Begin! "  + "="*7 + "\n")
    players = [player1, player2] #string name list
    playerSums = [player1sum, player2sum]
    currentPlayer = False # player flag, Defaults to the Oth (first) player in the list of players
    while numStack.size() > 1:
        if CHOICE == 0:
            print("\n Here is the stack of numbers..")
            print(" "*5, numStack,"\n")
            CHOICE = checkChoice(input("\n {}, it is your turn to choose to take 1 or 2 numbers : ".format( players[currentPlayer] )))

        elif CHOICE == 1:
            playerSums[currentPlayer] += numStack.pop()
            currentPlayer = not(currentPlayer)
            CHOICE = 0

        elif CHOICE == 2:
            for i in range(2):
                playerSums[currentPlayer] += numStack.pop()
            currentPlayer = not(currentPlayer)
            CHOICE = 0

    if not numStack.isEmpty:
        playerSums[currentPlayer] += numStack.pop()
    print("\n Totals are : \n")
    for i in range(2):
        print("{0}'s sum is : {1} ".format(players[i], playerSums[i]))

    print("The winner is : {}! Congrats! YAY! ".format(players[playerSums.index(max(playerSums))]))


game(11)
