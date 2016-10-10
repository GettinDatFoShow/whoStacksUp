from stack import *
from player import *
from choice import *

def checkChoice(choice):
    try:
        result = int(choice)
    except ValueError:
        return 0
    if result >= 2:
        return 2
    return 1

def swapPlayers(currentPlayer):
    currentPlayer = not(currentPlayer)
    CHOICE = Choice.ZERO
    return CHOICE, currentPlayer

def game(stackSize):
    CHOICE = 0 # set game state
    numStack = Stack()
    numStack.createStack(stackSize, 1, 11)
    playerOne = Player(input("Player 1, Enter your name: "))
    playerTwo = Player(input("Player 2, Enter your name: "))
    playerList = [playerOne, playerTwo] # string name list
    playerSums = [playerOne.getPlayerSum(), playerTwo.getPlayerSum()]
    currentPlayer = False # player flag, Defaults to the Oth (first) player in the list of players
    while numStack.size() > 1:
        if CHOICE == Choice.ZERO:
            print('\nCurrent Stack: \n{}'.format(numStack))
            CHOICE = checkChoice(input("\n {}, it is your turn to choose to take 1 or 2 numbers : ".format(playerList[currentPlayer].getPlayerName())))
        elif CHOICE == Choice.ONE:
            playerSums[currentPlayer] += numStack.pop()
            CHOICE, currentPlayer = swapPlayers(currentPlayer)
        elif CHOICE == Choice.TWO:
            for i in range(2):
                playerSums[currentPlayer] += numStack.pop()
            CHOICE, currentPlayer = swapPlayers(currentPlayer)
    if not numStack.isEmpty():
        playerSums[currentPlayer] += numStack.pop()
    for i in range(2):
        print("{0}'s sum is : {1} ".format(playerList[i].getPlayerName(), playerSums[i]))
    print("The winner is : {}! Congrats! YAY! ".format(playerList[playerSums.index(max(playerSums))].getPlayerName()))
game(11)