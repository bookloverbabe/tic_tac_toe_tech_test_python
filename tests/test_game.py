import unittest
from unittest.mock import patch
from model.game import Game

class TestGame(unittest.TestCase):

    def test_intro(self):
        game = Game()
        with patch('builtins.print') as mock_print:
            game.intro()
            mock_print.assert_called_with('Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0')

    def test_play(self):
        # Create a game instance
        game = Game()
        # Mock user input for the game (example moves for a game)
        with patch('builtins.input', side_effect=['1', '2', '4', '5', '7']):
            # Capture the actual output from the game
            actual_output = []
            with patch('builtins.print', side_effect=lambda x: actual_output.append(x)):
                game.play()

                # Now, you can assert that the expected print statements were called
                expected_output = [
                    " | | ",
                    "-+-+-",
                    " | | ",
                    "-+-+-",
                    " | | ",
                    "Player X, it's your turn. Enter a position (1 to 9): ",
                    " | | ",
                    "-+-+-",
                    " | | ",
                    "-+-+-",
                    "X| | ",
                    "Player O, it's your turn. Enter a position (1 to 9): ",
                ]
            # Compare the actual and expected output
            for actual_line, expected_line in zip(actual_output, expected_output):
                self.assertEqual(actual_line.strip(), expected_line.strip())

    def test_win(self):
        # Create a game instance
        game = Game()

        # Mock user input for the game (example: X wins)
        with patch('builtins.input', side_effect=['1', '2', '4', '5', '7']):
            # Simulate a winning condition for player X
            game.play()

            # Capture the actual state of the board
            actual_board_state = []
            # Lambda is an anonymous inline function consisting of a single expression which is evaluated when the function is called
            # side_effect is a parameter of the patch context manager that allows you to specify a 
            # custom function to be called each time the mocked print function is called.
            # the custom function is a lambda function that takes an argument x (which is typically what you pass to print) and appends x to the actual_board_state list. 
            # Essentially, it captures what is being printed and stores it in actual_board_state.
            with patch('builtins.print', side_effect=lambda x: actual_board_state.append(x)):
                game.board.printBoard()

            # Define the expected state of the board after a win (X wins)
            expected_board_state = [
            "X| | ",
            "-+-+-",
            "X|O| ",
            "-+-+-",
            "X|O| ",
        ]

        # Compares the captured actual output (stored in the actual_board_state list) 
        # with the expected output (stored in the expected_board_state list) in a unit test
        # In zip: iterates over several iterables in parallel, producing tuples with an item from each one, e,g creates a tuple containing one
        # from actual and expected, second tuple and so on to compare actual versus expected. 
        for actual_line, expected_line in zip(actual_board_state, expected_board_state):
            # .strip() is used to remove any leading or trailing whitespace characters
            self.assertEqual(actual_line.strip(), expected_line.strip())

    def test_validate_move(self):
        # Create a game instance
        game = Game()

        # Mock user input for the game (example: valid moves)
        with patch('builtins.input', side_effect=['1', '3', '5']):
            self.assertTrue(game.validate_move(input(), game.player_one))

        # Test with invalid moves
        with patch('builtins.input', side_effect=['1', '3', '1']):
            # Manually provide invalid input and validate
            self.assertNotEqual(game.validate_move('1', game.player_one))


    # def test_check_winner(self):

    
    # def test_check_tie(self):

    

if __name__ == '__main__':
    unittest.main()








    
