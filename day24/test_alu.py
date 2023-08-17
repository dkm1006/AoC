import unittest
from alu import Programme, find_lowest_input

INPUT_FILE = "input.txt"
SIMPLE_INPUTS = tuple(f"simple_input_{i}.txt" for i in (1,2,3))

class TestALU(unittest.TestCase):
    def test_part1(self):
        """
        Test: part1
        """
        monad = Programme.from_instruction_file(INPUT_FILE)
        self.assertEqual(monad(12345678901111).variables['z'], 1)
        self.assertEqual(monad(13579246899999).variables['z'], 0)


if __name__ == '__main__':
    unittest.main()
