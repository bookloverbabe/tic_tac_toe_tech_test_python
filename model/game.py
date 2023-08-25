# Created board, now need to create players X and O, who can insert into board
# If players meet certain patterns, they win.
from .board import *

class Game():
    def __init__(self):
        self.player_one = "X"
        self.player_two = "O"

    def intro(self):
        # Create players 1 and 2
        print('Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0')

    def play(self):  
        # Create board class outside loop
        board = Board()  
        for i in range(9):
            board.printBoard()
            # If i, which represents each turn, returns a modulo 0f 0 i.e an even number of turns, it is player ones turn. Remember than sequences run from 0 to 8.
            if i % 2 == 0:
                player = self.player_one
            else:
                player = self.player_two

            print(f'Player {player}, it\'s your turn. Enter a position (1 to 9): ')
            move = input()
            # Validate and update each move onto the board. board.grid represents dictionary that contains the board
            # move in board.grid checks whether the provided move corresponds to a valid position on the game board. First line checks if the move is empty
            # If true, board.grid[move] = player assigns players symbol to board, [] used to access elements in dictionary
            if move in board.grid and board.grid[move] == ' ':
                board.grid[move] = player
            else:
                print('Oops! This space is taken, try again')
                continue
            # If either player 1 or 2 have three adjoining places, they win
            for row in range(len(grid)):
                for column in range(len(grid)):
                    print(f'Player {player} is the winner!')

            # If there has been nine moves and no winner, declare a tie
            
        
    # Example of a tie code
    # def tie_validate(position_player):  
    # if len(position_player['X']) + len(position_player['O']) == 9:  
    #     return True  
    # return False  
    