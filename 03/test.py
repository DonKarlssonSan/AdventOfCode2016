import unittest
from day03part1 import possible_triangles
class MyTest(unittest.TestCase):

    def test_possible_triangles(self):
        triangles = '5 10 25'
        result = possible_triangles(triangles)
        self.assertEqual(result, 0)

