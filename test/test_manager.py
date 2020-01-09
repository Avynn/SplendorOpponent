import unittest
import sys
import os
from model import gameManager

class managerTests(unittest.TestCase):

    resourcePath = "SplendorOpponent/resources/cards.json"

    def test_init(self):
        manager = gameManager.manager(4,4, self.resourcePath)

        self.assertEqual(len(manager.players), 4)

    def test_getThreeCoins(self):
        manager = gameManager.manager(4,4, self.resourcePath)

        manager.getThreeCoins(manager.players[0], manager.board, ("red", "green", "blue"))

        self.assertEqual(manager.players[0].wallet["red"], 1)
        self.assertEqual(manager.players[0].wallet["green"], 1)
        self.assertEqual(manager.players[0].wallet["blue"], 1)
        
if __name__ == "__main__":
    unittest.main()
