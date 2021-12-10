import unittest
import numpy as np
from minimum import read_input, sum_risk_levels, find_largest_basins

INPUT_FILE = 'test_input.txt'

class TestHeightmap(unittest.TestCase):
    def test_minimum(self):
        """
        Test: part1
        """
        heightmap = read_input(INPUT_FILE)
        result = sum_risk_levels(heightmap)
        self.assertEqual(result, 15)

    def test_basins(self):
        """
        Test: part2
        """
        expected_result = 9 * 14 * 9
        heightmap = read_input(INPUT_FILE)
        largest_basins = find_largest_basins(heightmap)[:3]
        result = np.prod(largest_basins)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
