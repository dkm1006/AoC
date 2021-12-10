import unittest
from chunks import read_input, process_lines

INPUT_FILE = 'test_input.txt'

class TestChunks(unittest.TestCase):
    def test_score_corrupted_lines(self):
        """
        Test: part1
        """
        expected_result = 26397  # 2*3+57+1197+25137
        lines = read_input(INPUT_FILE)
        result = process_lines(lines)[0]
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
