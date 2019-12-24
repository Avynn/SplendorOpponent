import unittest
import sys
import os

os.chdir("../")
sys.path.insert(1, "model")

import gameManager

class managerTests(unittest.TestCase):

    def test_init(self):
        manager = gameManager.manager(4,4)

        self.assertEqual(len(manager.players), 4)
        
if __name__ == "__main__":
    unittest.main()