import unittest
import naive_growth
from growth import grow

INPUT_FILE = 'test_input.txt'

class TestNaiveGrowth(unittest.TestCase):
    def test_different_days(self):
        """
        Test: 18/80 days
        """
        initial_school = naive_growth.initialize_school(INPUT_FILE)
        result = naive_growth.grow(initial_school=initial_school, days_remaining=18)
        self.assertEqual(len(result), 26)
        result = naive_growth.grow(initial_school=result, days_remaining=80-18)
        self.assertEqual(len(result), 5934)


class TestGrowth(unittest.TestCase):
    def test_different_days(self):
        """
        Test: 18/80/256 days
        """
        result = grow(input_file=INPUT_FILE, days_remaining=18)
        self.assertEqual(sum(result), 26)
        result = grow(input_file=INPUT_FILE, days_remaining=80)
        self.assertEqual(sum(result), 5934)
        result = grow(input_file=INPUT_FILE, days_remaining=256)
        self.assertEqual(sum(result), 26984457539)

if __name__ == '__main__':
    unittest.main()
