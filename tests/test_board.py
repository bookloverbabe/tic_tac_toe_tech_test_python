import unittest
from model.board import *

class BoardTest(unittest.TestCase):
    def test_printBoard(self):
        result = ( | | 
                  -+-+-
                   | | 
                  -+-+-
                   | | )
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()