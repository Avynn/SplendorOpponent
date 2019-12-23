import sys
import json

sys.path.insert(1, "../model")

import cards

###  Unstable script for entering tiles into tile.json
###  created by Avynn Donaghe (12/22/19)

def main():
    openFile = open("tiles.json", "a")

    while(True):
        prestige = int(input("prestige: "))
        whiteCost = int(input("whiteCost: "))
        greenCost = int(input("greenCost: "))
        redCost = int(input("redCost: "))
        blueCost = int(input("blueCost: "))
        brownCost = int(input("brownCost: "))

        newTile = cards.tile(prestige, cards.cost(redCost, greenCost, blueCost, brownCost, whiteCost))

        json.dump(newTile.encode(), openFile)

        print("=============NEXT TILE===========")
        
main()
