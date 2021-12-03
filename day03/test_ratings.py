import unittest
from ratings import (
    calculate_power_consumption, calculate_life_support_rating
)

INPUT_FILE = 'test_input.txt'

class TestNavigation(unittest.TestCase):
    def test_power_consumptiom(self):
        """
        Test Part 1: Power consumption
        """
        expected_gamma_rate = 22
        expected_epsilon_rate = 9
        expected_power_consumption = 198
        result = calculate_power_consumption(INPUT_FILE)
        self.assertEqual(result, expected_power_consumption)

    def test_life_support(self):
        """
        Test Part 2: Life support
        """
        expected_life_support_rating = 230
        result = calculate_life_support_rating(INPUT_FILE)
        self.assertEqual(result, expected_life_support_rating)

if __name__ == '__main__':
    unittest.main()
