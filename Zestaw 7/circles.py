from points import Point
import math
import unittest

class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius**2

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if self.radius >= distance + other.radius:
            return Circle(self.pt.x, self.pt.y, self.radius)
        if other.radius >= distance + self.radius:
            return Circle(other.pt.x, other.pt.y, other.radius)

        new_radius = (distance + self.radius + other.radius) / 2
        if distance != 0:
            v = (new_radius - self.radius) / distance
        else:
            v = 0

        x = self.pt.x + dx * v
        y = self.pt.y + dy * v

        return Circle(x, y, new_radius)

class TestCircleCover(unittest.TestCase):
    def setUp(self):
        self.a = Circle(2, 0, 4)
        self.b = Circle(0, 0, 2)
        self.c = Circle(2, 0, 4)
        self.d = Circle(0, 0, 6)
        self.e = Circle(0, 0, 5)
        self.f = Circle(10, 0, 4)
        self.g = Circle(2, 2 ,3)
        self.h = Circle(6, 0, 4)
        self.i = Circle(6, 5, 2)

    def test__repr__(self):
        self.assertEqual(self.a.__repr__(), "Circle(2, 0, 4)")
        self.assertEqual(self.b.__repr__(), "Circle(0, 0, 2)")

    def test__eq__(self):
        self.assertEqual(self.a.__eq__(self.c), True)
        self.assertEqual(self.a.__eq__(self.b), False)
        self.assertEqual(self.b.__eq__(self.d), False)

    def test__ne__(self):
        self.assertEqual(self.a.__ne__(self.c), False)
        self.assertEqual(self.a.__ne__(self.b), True)
        self.assertEqual(self.b.__ne__(self.d), True)

    def test_area(self):
        self.assertEqual(self.a.area(), math.pi * 16)
        self.assertEqual(self.b.area(), math.pi * 4)
        self.assertEqual(self.d.area(), math.pi * 36)

    def test_move(self):
        self.assertEqual(self.a.move(2, 1), Circle(4, 1, 4))
        self.assertEqual(self.a.move(-2, 1), Circle(0, 1, 4))
        self.assertEqual(self.b.move(-2, -3), Circle(-2, -3, 2))

    def test_cover(self):
        self.assertEqual(self.b.cover(self.e), Circle(0, 0, 5))
        self.assertEqual(self.e.cover(self.b), Circle(0, 0, 5))
        self.assertEqual(self.a.cover(self.f), Circle(6, 0, 8))
        self.assertEqual(self.e.cover(self.h), Circle(2.5, 0, 7.5))
        self.assertEqual(self.g.cover(self.i), Circle(3.6, 3.2, 5))


if __name__ == "__main__":
    unittest.main()