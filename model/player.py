from model import board, cards

class player:

    def __init__(self, name):

        self.name = name

        self.wallet = {
            "red": 0,
            "white": 0,
            "blue": 0,
            "green": 0,
            "brown": 0,
            "joker": 0
        }
        
        self.bonus = {
            "red": 0,
            "white": 0,
            "blue": 0,
            "green": 0,
            "brown": 0
        }

        self.cardsReserved = []
        self.cardsPlayed = []
        self.tilesRecieved = []

        self.prestige = 0
        self.numTurns = 0
