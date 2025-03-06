import unittest
from src import c05_linkedlistreverse as lr

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse(self):
        ll = lr.LinkedList()
        for i in [1, 2, 3, 4, 5]:
            ll.append(i)
        ll.reverse()
        self.assertEqual(ll.to_list(), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
