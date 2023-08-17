import unittest
from stepping import read_input, sum_flashes

INPUT_FILE = 'test_input.txt'

class TestFlash(unittest.TestCase):
    def test_score_corrupted_lines(self):
        """
        Test: part1
        """
        expected_result = 1656
        board = read_input(INPUT_FILE)
        result = sum_flashes(board)
        self.assertEqual(result, expected_result)

    def test_autocomplete(self):
        """
        Test: part2
        """
        expected_result = 288957
        lines = read_input(INPUT_FILE)
        result = process_lines(lines)[1]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
