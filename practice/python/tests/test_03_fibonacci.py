from src import c03_fibonacci as fb 
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        n = 10
        expected_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
        self.assertEqual(fb.fibonacci(n), expected_output)

if __name__ == "__main__":
    unittest.main()
