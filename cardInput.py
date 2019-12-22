import json
import cards

###  Unstable Script for entering cards into cards.json
###  created by Avynn Donaghe (12/21/19)


def main():
    openFile = open("cards.json", "a")

    while(True):
        tier = int(input("tier:"))
        prestige = int(input("prestige:"))
        bonus = input("bonus:")
        redCost = int(input("redCost:"))
        greenCost = int(input("greenCost:"))
        blueCost = int(input("blueCost:"))
        brownCost = int(input("brownCost:"))
        whiteCost = int(input("whiteCost:"))

        newCard = cards.card(tier, prestige, bonus, cards.cost(redCost, greenCost, blueCost, brownCost, whiteCost))

        json.dump(newCard.encode(), openFile)

        print("==============NEXT CARD================")

main()
