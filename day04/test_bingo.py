import unittest
from bingo import Bingo

INPUT_FILE = 'test_input.txt'

class TestBingo(unittest.TestCase):
    def test_winning_strategy(self):
        """
        Test Part 1: Pick best board
        """
        game = Bingo(INPUT_FILE)
        game.play()
        self.assertEqual(game.winning_order[0], 4512)

    def test_life_support(self):
        """
        Test Part 2: Pick last board
        """
        game = Bingo(INPUT_FILE)
        game.play()
        self.assertEqual(game.winning_order[-1], 1924)

if __name__ == '__main__':
    unittest.main()
