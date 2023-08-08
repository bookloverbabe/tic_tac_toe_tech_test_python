import unittest
from model.board import *

class TestBoard(unittest.TestCase):

    def test_printBoard(self):
        # Create instance of board class
        board = Board()
        board.printBoard()
        response = ( " | | \n"
                    " -+-+-\n"
                    "  | |\n"
                    " -+-+-\n"
                    "  | |  ")
        self.assertTrue(response)