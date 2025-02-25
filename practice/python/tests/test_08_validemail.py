import unittest
import os
from src.c08_validemail import valid_email

class TestValidEmail(unittest.TestCase):

    def test_valid_email(self):
        expected_output = [
            "victus23@gmail.com",
            "datamonk@gmail.com"
        ]
        
        result = valid_email()
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
