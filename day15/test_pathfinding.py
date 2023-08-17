import unittest
from pathfinding import read_input, find_lowest_total_risk

INPUT_FILE = "test_input.txt"

class TestPathfinding(unittest.TestCase):
    def test_init(self):
        """
        Test: Create graph
        """
        expected_shape = (10, 10)
        densitymap = read_input(INPUT_FILE)
        self.assertEqual(expected_shape, densitymap.shape)

    def test_find_optimal_path(self):
        """
        Test: find total risk for optimal path
        """
        expected_lowest_total_risk = 40
        densitymap = read_input(INPUT_FILE)
        actual_total_risk = find_lowest_total_risk(densitymap)
        self.assertEqual(expected_lowest_total_risk, actual_total_risk)
            

if __name__ == '__main__':
    unittest.main()
