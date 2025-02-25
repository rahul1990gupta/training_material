import unittest
from src import c04_mergesort as ms  

class TestMergeSort(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(ms.merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(ms.merge_sort([5, 3, 8, 1, 2]), [1, 2, 3, 5, 8])

    def test_duplicate_values(self):
        self.assertEqual(ms.merge_sort([4, 2, 4, 1, 3, 2]), [1, 2, 2, 3, 4, 4])

    def test_negative_values(self):
        self.assertEqual(ms.merge_sort([-5, -1, -3, -2]), [-5, -3, -2, -1])

    def test_empty_list(self):
        self.assertEqual(ms.merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(ms.merge_sort([7]), [7])

if __name__ == "__main__":
    unittest.main()
