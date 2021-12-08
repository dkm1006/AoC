import unittest
import digits

INPUT_FILE = 'test_input.txt'

class TestDigits(unittest.TestCase):
    def test_digits1(self):
        """
        Test: part1
        """
        input_values = digits.read_input(INPUT_FILE)
        result = digits.count_1478(input_values)
        self.assertEqual(result, 26)

    def test_positioning_part2(self):
        """
        Test: part2
        """
        expected_result = 5353 + 61229
        input_values = digits.read_input(INPUT_FILE)
        result = digits.sum_outputs(input_values)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
