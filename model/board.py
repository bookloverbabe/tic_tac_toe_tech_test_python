# This class creates the grid for the game, consists of three rows of three, use a disctionary to 
# assign a number to each square. Dictionary is a key value pair, like hash in Ruby.
class Board():
    def __init__(board):
        grid = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

    def printBoard(grid):
        print(grid['7'] + '|' + grid['8'] + '|' + grid['9'])
        print('-+-+-')
        print(grid['4'] + '|' + grid['5'] + '|' + grid['6'])
        print('-+-+-')
        print(grid['1'] + '|' + grid['2'] + '|' + grid['3'])

BoardObject = Board
grid = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
Board.printBoard(grid)
