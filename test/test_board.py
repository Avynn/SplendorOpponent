import unittest
import sys
import os

os.chdir("../")
sys.path.insert(1, "model")

import board

class boardTests(unittest.TestCase):

    def test_initFullGame(self):
        b = board.board(4)

        self.assertEqual(b.numGreen, 7)
        self.assertEqual(b.numBlue, 7)
        self.assertEqual(b.numWhite, 7)
        self.assertEqual(b.numBrown, 7)
        self.assertEqual(b.numRed, 7)
        self.assertEqual(b.numNobles, 5)

    def test_init3PlayerGame(self):
        b = board.board(3)

        self.assertEqual(b.numGreen, 5)
        self.assertEqual(b.numBlue, 5)
        self.assertEqual(b.numWhite, 5)
        self.assertEqual(b.numBrown, 5)
        self.assertEqual(b.numRed, 5)
        self.assertEqual(b.numNobles, 4)

    def test_initDuel(self):
        b = board.board(2)

        self.assertEqual(b.numGreen, 4)
        self.assertEqual(b.numBlue, 4)
        self.assertEqual(b.numWhite, 4)
        self.assertEqual(b.numBrown, 4)
        self.assertEqual(b.numRed, 4)
        self.assertEqual(b.numNobles, 3)

    def test_RaiseIfLow(self):
        self.assertRaises(Exception, board.board, 1)

    def test_raiseIfHigh(self):
        self.assertRaises(Exception, board.board, 5)

    def rest_raiseIfNotNum(self):
        self.assertRaises(Exception, board.board, ">")
        
    def test_ActiveInit(self):
        b = board.board(4)

        self.assertEqual(len(b.tier1Active), 4)
        self.assertEqual(len(b.tier2Active), 4)
        self.assertEqual(len(b.tier3Active), 4)

if __name__ == "__main__":
    unittest.main()
        
        
        
