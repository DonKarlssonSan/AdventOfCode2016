import unittest
from day03part1 import possible_triangles

class MyTest(unittest.TestCase):

    def test_possible_triangles(self):
        triangles = '5 10 25'
        self.assertEqual(possible_triangles(triangles), 0)


