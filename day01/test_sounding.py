import unittest
from sounding import read_sonar, count_increases, sliding_window

INPUT_FILE = 'test_input.txt'

class TestSounding(unittest.TestCase):
    def test_simple_increase(self):
        """
        Test Part 1: count every increase from previous value
        """
        result = count_increases(read_sonar(INPUT_FILE))
        self.assertEqual(result, 7)
    
    def test_sliding_increase(self):
        """
        Test Part 2: count only increases from 
        sliding window to previous window
        """
        data = read_sonar(INPUT_FILE)
        windows = sliding_window(data, window_size=3, fn=sum)
        result = count_increases(windows)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
