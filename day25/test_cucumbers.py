import unittest
from seacucumbers import read_input, simulate_migration

INPUT_FILE = "test_input.txt"

class TestCucumbers(unittest.TestCase):
    def test_part1(self):
        """
        Test: part1
        """
        sea_floor = read_input(INPUT_FILE)
        num_steps = simulate_migration(sea_floor)
        self.assertEqual(num_steps, 58)

if __name__ == '__main__':
    unittest.main()
