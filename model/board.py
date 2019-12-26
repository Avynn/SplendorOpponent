import sys
from model import cards
import json
import random
import os

class board:

    @staticmethod
    def sortAndShuffle(cardsList):
        tier1 = []
        tier2 = []
        tier3 = []

        for card in cardsList:
            if card.tier == 1:
                tier1.append(card)
            elif card.tier == 2:
                tier2.append(card)
            elif card.tier == 3:
                tier3.append(card)
            else:
                #should raise error, fix later
                print("card was improperly parsed")

        random.shuffle(tier1)
        random.shuffle(tier2)
        random.shuffle(tier3)

        return (tier1, tier2, tier3)

    @staticmethod
    def readCards(*altPath):
        resourcePath = "resources/cards.json"

        if(len(altPath) != 0):
            resourcePath = altPath[0]
        
        fp = open("resources/cards.json", "r")
        cardsJSON = json.load(fp)
        cardsList = []
        
        for card in cardsJSON:
            cardsList.append(cards.card.decode(card))

        fp.close()
            
        return board.sortAndShuffle(cardsList)
    
    def __init__(self, numPlayers, *altResourcePath):
        if(type(numPlayers) is not int):
            raise Exception("numPlayers is not an integer!")
        elif(numPlayers > 4):
            raise Exception("Cannot have more than 4 players")
        elif(numPlayers < 2):
            raise Exception("Cannot have less than 4 players")

        self.numNobles = numPlayers + 1

        numTokens = 7

        if(numPlayers == 2):
            numTokens = numTokens - 3
        elif(numPlayers == 3):
            numTokens = numTokens - 2

        self.numJokers = 5
        self.numGreen = numTokens
        self.numWhite = numTokens
        self.numBrown = numTokens
        self.numRed = numTokens
        self.numBlue = numTokens
        
        self.tier1, self.tier2, self.tier3 = board.readCards() if len(altResourcePath) == 0 else board.readCards(altResourcePath[0])

        self.tier1Active = []
        self.tier2Active = []
        self.tier3Active = []
        
        for i in range(0,4):
            self.tier1Active.append(self.tier1.pop(0))
            self.tier2Active.append(self.tier2.pop(0))
            self.tier3Active.append(self.tier3.pop(0))
