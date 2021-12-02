import unittest
from navigation import Submarine

INPUT_FILE = 'test_input.txt'

class TestNavigation(unittest.TestCase):
    def test_init(self):
        """
        Test Part 1: simple case
        """
        sub = Submarine()
        self.assertEqual(sub.depth, 0)
        self.assertEqual(sub.horizontal, 0)
        self.assertEqual(sub.aim, 0)

    def test_part1(self):
        """
        Test Part 1: simple case
        """
        sub = Submarine()
        for order, value in sub.read_orders(INPUT_FILE):
            sub.update_position_simple(order, value)

        result = sub.multiply_position()
        self.assertEqual(result, 150)
    
    def test_part2(self):
        """
        Test Part 2: forward uses aim to change depth
        """
        sub = Submarine()
        for order, value in sub.read_orders(INPUT_FILE):
            sub.update_position(order, value)

        result = sub.multiply_position()
        self.assertEqual(result, 900)

if __name__ == '__main__':
    unittest.main()
