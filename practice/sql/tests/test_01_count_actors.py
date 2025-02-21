import unittest
from src.db_utils import execute


class TestCountActors(unittest.TestCase):
    def test_count_actors(self):
        with open('src/c01_count_actors.sql', 'r') as f:
            sql = f.read()
        result = execute(sql)
        self.assertEqual(result[0][0], 200)
