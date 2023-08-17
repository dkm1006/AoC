import unittest
import numpy as np
from beacon_scan import parse_scanner_report, construct_beacon_map

INPUT_FILE_MINI = "mini_test_input.txt"
INPUT_FILE = "test_input.txt"

class TestImageEnhancement(unittest.TestCase):
    def test_2d(self):
        """
        Test: 2D mini example
        """
        scanners = parse_scanner_report(INPUT_FILE_MINI)
        translation = find_transformation(scanners[0], scanners[1])
        self.assertEqual(translation, np.array((5, 2)))
        beacon_map = construct_beacon_map(scanners)
        num_beacons = beacon_map.sum()
        self.assertEqual(num_beacons, 3)

    def test_3d(self):
        """
        Test: 3D Part 1
        """
        scanners = parse_scanner_report(INPUT_FILE)
        beacon_map = construct_beacon_map(scanners)
        num_beacons = beacon_map.sum()
        self.assertEqual(num_beacons, 79)

if __name__ == '__main__':
    unittest.main()
