from src import c02_matrotate as mr
import unittest

class TestMatRotate(unittest.TestCase):
    def test_rotate_counter_clockwise(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        result = mr.rotate_counter_clockwise(matrix)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
