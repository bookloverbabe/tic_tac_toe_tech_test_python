import unittest
from model import *

class BoardTest(unittest.TestCase):
    def test_printBoard(board):
        board = Board()
        # board.printBoard(board)
        board.grid =  ([' | | '],
                   ['-+-+- '],
                   [' | | '],
                   ['-+-+-'],
                   [' | |'])
        board.assertEqual(board.grid)
if __name__ == '__main__':
    unittest.main()