import unittest

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __hash__(self):
        return hash((self.x, self.y))


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.zero = Point(3, 4)
        self.one = Point(5, 6)
        self.two = Point(3, 4)

    def test__str__(self):
        self.assertEqual(self.zero.__str__(), "(3, 4)")
        self.assertEqual(self.one.__str__(), "(5, 6)")

    def test__repr__(self):
        self.assertEqual(self.zero.__repr__(), "Point(3, 4)")
        self.assertEqual(self.one.__repr__(), "Point(5, 6)")

    def test__eq__(self):
        self.assertEqual(self.zero.__eq__(self.one), False)
        self.assertEqual(self.zero.__eq__(self.two), True)

    def test__ne__(self):
        self.assertEqual(self.zero.__ne__(self.one), True)
        self.assertEqual(self.zero.__ne__(self.two), False)

    def test__add__(self):
        self.assertEqual(self.zero.__add__(self.one), (8, 10))
        self.assertEqual(self.zero.__add__(self.two), (6, 8))

    def test__sub__(self):
        self.assertEqual(self.zero.__sub__(self.one), (-2, -2))
        self.assertEqual(self.zero.__sub__(self.two), (0, 0))

    def test__mul__(self):
        self.assertEqual(self.zero.__mul__(self.one), 39)
        self.assertEqual(self.zero.__mul__(self.two), 25)

    def test_cross(self):
        self.assertEqual(self.zero.cross(self.one), -2)
        self.assertEqual(self.zero.cross(self.two), 0)

    def test_length(self):
        self.assertEqual(self.zero.length(), 5)
        self.assertEqual(self.one.length(), 61**0.5)

