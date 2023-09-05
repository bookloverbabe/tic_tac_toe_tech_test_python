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

           # Compare the actual and expected board states
        for actual_line, expected_line in zip(actual_board_state, expected_board_state):
            self.assertEqual(actual_line.strip(), expected_line.strip())

    # def test_validate_move(self):

    
    # def test_check_winner(self):

    
    # def test_check_tie(self):
    #             # Test the play method
    #     with patch('builtins.print') as mock_print:
    #         # Use patch to mock user input
    #         with patch('builtins.input', side_effect=['[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]']):
    #             game = Game()
    #             game.win()
    #             expected_output_two = [                    
    #                 "X| | ",
    #                 "-+-+-",
    #                 "0|X | ",
    #                 "-+-+-",
    #                 "X| | ",]
    #             for call_args in mock_print.call_args_list:
    #                 printed_output_two = call_args[0][0]
    #                 self.assertEqual(printed_output_two, expected_output_two.pop(0))
    

if __name__ == '__main__':
    unittest.main()








    
