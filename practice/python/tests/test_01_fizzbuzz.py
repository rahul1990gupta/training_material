from src import c01_fizzbuzz as fb
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fb.fizzbuzz(1), '1')
        self.assertEqual(fb.fizzbuzz(3), 'Fizz')
        self.assertEqual(fb.fizzbuzz(5), 'Buzz')
        self.assertEqual(fb.fizzbuzz(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
