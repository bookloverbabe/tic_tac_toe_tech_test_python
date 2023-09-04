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
        # Test the play method
        with patch('builtins.print') as mock_print:
            # Use patch to mock user input
            with patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                game = Game()
                game.play()

                # Now, you can assert that the expected print statements were called
                expected_output = [
                   'Welcome to tic tac toe! Player 1 will play with X and player 2 will play with 0'
                   ' | | '
                   '-+-+-'
                   ' | | '
                   '-+-+-'
                   ' | | '
                   "Player X, its your turn. Enter a position (1 to 9):"
                   ]
                # This iterates over the mock_print function, to ensure that the correct output
                # is made at the correct point of the game

                # mock_print.call_args_list loops through each recorded call to print. call_args is 
                # a tuple that holds arguments passed to print
                for call_args in mock_print.call_args_list:
                    # call_args[0[0] extracts first argumgent in call_args tuple 
                    printed_output = call_args[0][0]
                    # The self.assertEqual assertion is used to compare the actual printed output (captured by the mock) with the expected output
                    # Compares printed_output with first item in expected_output. expected_output.pop(0) removes 
                    # and returns the first item from the list for comparison
                    self.assertEqual(printed_output, expected_output.pop(0))

    def test_win(self):
        # Test the play method
        with patch('builtins.print') as mock_print:
            # Use patch to mock user input
            with patch('builtins.input', side_effect=['[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]']):
                game = Game()
                game.win()
                expected_output_two = [                    
                    "X| | ",
                    "-+-+-",
                    "X| | ",
                    "-+-+-",
                    "X| | ",]
                for call_args in mock_print.call_args_list:
                    printed_output_two = call_args[0][0]
                    self.assertEqual(printed_output_two, expected_output_two.pop(0))
    
    def test_tie(self):
                # Test the play method
        with patch('builtins.print') as mock_print:
            # Use patch to mock user input
            with patch('builtins.input', side_effect=['[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]']):
                game = Game()
                game.win()
                expected_output_two = [                    
                    "X| | ",
                    "-+-+-",
                    "0|X | ",
                    "-+-+-",
                    "X| | ",]
                for call_args in mock_print.call_args_list:
                    printed_output_two = call_args[0][0]
                    self.assertEqual(printed_output_two, expected_output_two.pop(0))
    

if __name__ == '__main__':
    unittest.main()








    
