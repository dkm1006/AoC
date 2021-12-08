import unittest
import numpy as np
import positioning

INPUT_FILE = 'test_input.txt'

class TestPositioning(unittest.TestCase):
    # TODO: There should be a test for read_input, too
    def test_positioning_part1(self):
        """
        Test: part1
        """
        positions = positioning.read_input(INPUT_FILE)
        costs = positioning.sol_part_2(positions, cost_fn=np.array)
        optimal_position = costs.argmin()
        optimal_fuel_consumption = costs.min()
        self.assertEqual(optimal_position, 2)
        self.assertEqual(optimal_fuel_consumption, 37)

    def test_positioning_part2(self):
        """
        Test: part2
        """
        positions = positioning.read_input(INPUT_FILE)
        costs = positioning.sol_part_2(positions, cost_fn=np.cumsum)
        optimal_position = costs.argmin()
        optimal_fuel_consumption = costs.min()
        self.assertEqual(optimal_position, 5)
        self.assertEqual(optimal_fuel_consumption, 168)

if __name__ == '__main__':
    unittest.main()
