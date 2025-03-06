import unittest
from src import c07_stopwords as sw

class TestStopWords(unittest.TestCase):
    def test_detect_stopword(self):
        stopword = sw.detect_stopword()
        self.assertEqual(stopword, "the") 

if __name__ == "__main__":
    unittest.main()
