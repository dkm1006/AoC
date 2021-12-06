import unittest
from obstacle_avoidance import OceanMap, read_input, is_horizontal_or_vertical_line

INPUT_FILE = 'test_input.txt'

class TestAvoidance(unittest.TestCase):
    def test_horizontal_or_vertical_lines(self):
        """
        Test Part 1: Only consider horizontal or vertical lines
        """
        ocean_map = OceanMap(size=10)
        lines = read_input(INPUT_FILE)
        for start, end in filter(is_horizontal_or_vertical_line, lines):
            ocean_map.mark_horizontal_or_vertical_line(start, end)
            
        num_overlapping_points = ocean_map.overlapping_points(threshold=2).sum()
        self.assertEqual(num_overlapping_points, 5)

    def test_diagonal_lines(self):
        """
        Test Part 2: Also consider diagonal lines
        """
        ocean_map = OceanMap(size=10)
        lines = read_input(INPUT_FILE)
        for start, end in lines:
            ocean_map.mark_line(start, end)
            
        num_overlapping_points = ocean_map.overlapping_points(threshold=2).sum()
        self.assertEqual(num_overlapping_points, 12)

if __name__ == '__main__':
    unittest.main()
