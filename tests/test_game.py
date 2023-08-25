import unittest
from unittest.mock import patch
from model.game import *
from model.board import *

class TestGame(unittest.TestCase):

    def test_intro(self):
        game = Game()
        game.intro()
        response = 'Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0'
        self.assertTrue(response)
    
    def test_play(self):
        game = Game()
        game.play()
        response = ( " | | \n"
                    " -+-+-\n"
                    "  | |\n"
                    " -+-+-\n"
                    "  | |  ")
        self.assertTrue(response)
        response_two = ('Player 1, you will go first. Remember, that your symbol is X')
        self.assertTrue(response_two)
        # Mock input to test validation and update of board. Use patch.dict() to patch the dictionary
        game = Game()
        game.play()
        with patch.dict(board, {'7': 'X', '3': 'O'}) as patched_board:
            assert patched_board == ( "X| | \n"
                                   " -+-+-\n"
                                   "  | |\n"
                                   " -+-+-\n"
                                   "  | |O ") 
        # Mock input where player is decleared a winner
        # game = Game()
        # game.play()
        self.assertTrue('Player one is the winner!')
        with patch.dict(board_two, {'1': 'X', '2':'X', '3': 'X'}) as patched_board_two:
            assert patched_board_two == (" | | \n"
                                    " -+-+-\n"
                                    "  | |\n"
                                    " -+-+-\n"
                                    " X|X|X") 







    
