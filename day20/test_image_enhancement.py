import unittest
from image_enhancement import read_input, apply_multiple_enhancement_steps

INPUT_FILE = "test_input.txt"

class TestImageEnhancement(unittest.TestCase):
    def test_2_steps(self):
        """
        Test: part1
        """
        enhancer_algo, img = read_input(INPUT_FILE)
        final_img = apply_multiple_enhancement_steps(img, enhancer_algo,
                                                     steps=2, verbose=False)
        self.assertEqual(final_img.sum(), 35)

    def test_50_steps(self):
        """
        Test: part2
        """
        enhancer_algo, img = read_input(INPUT_FILE)
        final_img = apply_multiple_enhancement_steps(img, enhancer_algo,
                                                     steps=50, verbose=False)
        self.assertEqual(final_img.sum(), 3351)

if __name__ == '__main__':
    unittest.main()
