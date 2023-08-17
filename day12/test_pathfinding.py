import unittest
from pathfinding import read_input

INPUT_FILES = tuple(f"test_input{i}.txt" for i in (1, 2, 3)) 

class TestPathfinding(unittest.TestCase):
    def test_init(self):
        """
        Test: Create graph
        """
        for expected_graph_size, input_file in zip((6, 7, 10), INPUT_FILES):
            graph = read_input(input_file)
            self.assertEqual(len(graph), expected_graph_size)

    def test_count_paths(self):
        """
        Test: part1
        """
        for expected_num_paths, input_file in zip((10, 19, 226), INPUT_FILES):
            graph = read_input(input_file)
            num_paths = len(graph['start'].find_paths_to('end'))
            self.assertEqual(num_paths, expected_num_paths)

if __name__ == '__main__':
    unittest.main()
