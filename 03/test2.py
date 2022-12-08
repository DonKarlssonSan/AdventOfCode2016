import unittest
from day03part2 import possible_triangles_vertically

class MyTest(unittest.TestCase):

    def test_possible_triangles_vertically(self):
        triangles =  r"""  810  679   10
783  255  616
545  626  626"""
        result = possible_triangles_vertically(triangles)
        self.assertEqual(result, 2)


