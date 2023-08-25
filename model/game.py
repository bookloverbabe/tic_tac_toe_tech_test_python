# Created board, now need to create players X and O, who can insert into board
# If players meet certain patterns, they win.
from model.board import *

class Game():
    def __init__(self):
        self.player_one = "X"
        self.player_two = "0"

    def intro(self):
        # Create players 1 and 2
        print('Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0')

    def play(self):    
        for i in range(9):
            board = Board()
            board.printBoard()
    