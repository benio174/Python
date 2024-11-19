from points import Point
import unittest

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self.__eq__(other)

    def center(self):
        return (self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2

    def area(self):
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return Rectangle(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.zero = Rectangle(2, 3, 4, 6)
        self.one = Rectangle(1, 2, 4, 6)
        self.two = Rectangle(2, 3, 4, 6)

    def test__str__(self):
        self.assertEqual(self.zero.__str__(), "[(2, 3), (4, 6)]")
        self.assertEqual(self.one.__str__(), "[(1, 2), (4, 6)]")

    def test__repr__(self):
        self.assertEqual(self.zero.__repr__(), "Rectangle(2, 3, 4, 6)")
        self.assertEqual(self.one.__repr__(), "Rectangle(1, 2, 4, 6)")

    def test__eq__(self):
        self.assertEqual(self.zero.__eq__(self.one), False)
        self.assertEqual(self.zero.__eq__(self.two), True)

    def test__ne__(self):
        self.assertEqual(self.zero.__ne__(self.one), True)
        self.assertEqual(self.zero.__ne__(self.two), False)

    def test_center(self):
        self.assertEqual(self.zero.center(), (3, 4.5))
        self.assertEqual(self.one.center(), (2.5, 4))

    def test_area(self):
        self.assertEqual(self.zero.area(), 6)
        self.assertEqual(self.one.area(), 12)

    def test_move(self):
        self.assertEqual(self.zero.move(2, 3), Rectangle(4, 6, 6, 9))
        self.assertEqual(self.one.move(-2, 4), Rectangle(-1, 6, 2, 10))

