class Player:
    def __init__(self, pName):
        self.playerName = pName
        self.totalSum = 0

    def setPlayerSum(self, sum):
        self.totalSum += sum

    def getPlayerSum(self):
        return self.totalSum

    def getPlayerName(self):
        return self.playerName

    def setPlayerName(self, pName):
        self.playerName = pName