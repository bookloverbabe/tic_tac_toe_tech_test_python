# Created board, now need to create players X and O, who can insert into board
# If players meet certain patterns, they win.
from model.board import Board

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
                player_current = self.player_one
            else:
                player_current = self.player_two

            print (f"Player {player_current}, it's your turn. Enter a position (1 to 9): ")
            move = input()
            # Validate and update each move onto the board. board.grid represents dictionary that contains the board
            # move in board.grid checks whether the provided move corresponds to a valid position on the game board. First line checks if the move is empty
            # If true, board.grid[move] = player assigns players symbol to board, [] used to access elements in dictionary
            if move in board.grid and board.grid[move] == ' ':
                board.grid[move] = player_current
            else:
                print('Oops! This space is taken, try again')
                continue
    def win(player_one, player_two, player_current):
        # If either player 1 or 2 have three adjoining places, they win
        win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  
        # Create for loop to check if wining combinations is met
        for x in win_combinations:
            if all(y in player_one or player_two[player_current] for y in x):
                print(f'Player {player_current} is the winner!')
        return False

            # If there has been nine moves and no winner, declare a tie
            
        
    # Example of a tie code
    # def tie_validate(position_player):  
    # if len(position_player['X']) + len(position_player['O']) == 9:  
    #     return True  
    # return False  
    