import unittest
from location import *
from game import *
from dialogues import *

class TestMethods(unittest.TestCase):
    
    def test_crone_dialogue(self):
        crone_dialogue.play_dialogue("start")

if __name__ == "__main__":
    unittest.main()