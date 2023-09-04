# Created board, now need to create players X and O, who can insert into board
# If players meet certain patterns, they win.
from board import Board
# from model.board import Board

class Game():
    def __init__(self):
        self.player_one = "X"
        self.player_two = "O"
        self.board = Board() 

    def intro(self):
        # Create players 1 and 2
        print('Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0')

    def play(self):  
        # Create board class outside loop
        # Instance variable, , which are initialized in the __init__ method of the Game class
        self.board.printBoard()
        for i in range(9):
            self.board.printBoard()
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
            if move in self.board.grid and self.board.grid[move] == ' ':
                self.board.grid[move] = player_current
            else:
                print('Oops! This space is taken, try again')
                continue

    def win(self, board, player_current):
        win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        # This line initiates a loop that iterates through each combo in the win_combinations list. Each combo is a 
        # list of positions that represents a possible winning combination.
        for combo in win_combinations:
            # This line checks if all positions in the current combo have been filled with the symbol of the current player (player_current)
            # [str(pos)] denotes a list or dictionary access. Here, it's used to access a 
            # value in a dictionary using a string as the key. pos is a varialbe representing a position on the board. 
            # Need to convert position, which is an int, into a string
            if all(board.grid[str(position)] == player_current for position in combo):
                print(f"Player {player_current} is the winner!")
                return True  # Indicates the game is won
        return False  # Indicates the game is not won yet

    def tie(self, board):
        return all(board.grid[str(position)] != ' ' for position in range(1, 10))
    
        # The main function here runs the program

def main():
    game = Game()
    game.intro()
    board = Board()  # Create the board
    player_current = game.player_one  # Start with player 1
    for _ in range(9):  # Maximum of 9 moves
        board.printBoard()
        game.play()
        if game.win(board, player_current):
            print(f"Player {player_current} is the winner!")
            break
        if game.tie(board):
            print("It's a tie!")
            break
        game.play(board, player_current)
        # Switch to the other player for the next turn
        player_current = game.player_one if player_current == game.player_two else game.player_two

    # This is where using the if __name__ == '__main__' code block comes in handy. Code within this block won’t run unless the module is 
    # executed in the top-level environment.
if __name__ == '__main__':
    main()