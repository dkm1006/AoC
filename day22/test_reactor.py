import unittest
from reactor import read_instructions, initialize_reactor, initialize_sparse_reactor

MINI_INPUT_FILE = "mini_test_input.txt"
INPUT_FILE = "test_input.txt"

class TestImageEnhancement(unittest.TestCase):
    def test_mini(self):
        """
        Test: part1 mini
        """
        instructions = read_instructions(MINI_INPUT_FILE)
        reactor_cuboid = initialize_reactor(instructions, min_start=-50, max_end=51)
        self.assertEqual(reactor_cuboid.sum(), 39)

    def test_part1(self):
        """
        Test: part1
        """
        instructions = read_instructions(INPUT_FILE)
        reactor_cuboid = initialize_reactor(instructions, min_start=-50, max_end=51)
        self.assertEqual(reactor_cuboid.sum(), 590784)

if __name__ == '__main__':
    unittest.main()
