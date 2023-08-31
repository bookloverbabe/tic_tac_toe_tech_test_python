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
                    " | | ",
                    "Player O, it's your turn. Enter a position (1 to 9): ",
                    # ... and so on
                ]
                for call_args in mock_print.call_args_list:
                    printed_output = call_args[0][0]
                    self.assertEqual(printed_output, expected_output.pop(0))

if __name__ == '__main__':
    unittest.main()








    
