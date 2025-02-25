import unittest
from src import c06_bstsearch as bs  

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = bs.BST()
        for value in [10, 5, 15, 3, 7, 12, 18]:
            self.bst.insert(value)

    def test_search_existing_value(self):
        self.assertTrue(self.bst.search(10))
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(15))
        self.assertTrue(self.bst.search(7))

    def test_search_non_existing_value(self):
        self.assertFalse(self.bst.search(20))
        self.assertFalse(self.bst.search(0))
        self.assertFalse(self.bst.search(13))

    def test_search_empty_bst(self):
        empty_bst = bs.BST()
        self.assertFalse(empty_bst.search(10))

if __name__ == "__main__":
    unittest.main()
