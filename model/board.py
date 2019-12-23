import sys
import cards
import json
import random

class board:

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

    def readCards():
        fp = open("resources/cards.json", "r")
        cardsJSON = json.load(fp)
        cardsList = []
        
        for card in cardsJSON:
            cardsList.append(cards.card.decode(card))

        return board.sortAndShuffle(cardsList)
    
    def __init__(self):
        self.tier1, self.tier2, self.tier3 = board.readCards()
        
