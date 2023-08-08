import unittest
from model.game import *
from model.board import *

class TestGame(unittest.TestCase):

    def test_intro(self):
        game = Game()
        game.intro()
        response = 'Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0'
        self.assertTrue(response)