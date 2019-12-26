from model import board, cards

class player:

    def __init__(self, name):

        self.name = name

        #wallet
        self.numRed = 0
        self.numBlue = 0
        self.numGreen = 0
        self.numWhite = 0
        self.numBrown = 0
        self.numJoker = 0
        self.redBonus = 0
        self.blueBonus = 0
        self.greenBonus = 0
        self.whiteBonus = 0
        self.brownBonus = 0

        self.cardsReserved = []
        self.cardsPlayed = []
        self.tilesRecieved = []

        self.prestige = 0
        self.numTurns = 0
