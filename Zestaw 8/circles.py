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

    @classmethod
    def from_points(cls, points):
        if not isinstance(points, (list, tuple)) or len(points) != 3:
            raise ValueError("Musisz podać dokładnie trzy punkty w krotce lub liście.")

        (x1, y1), (x2, y2), (x3, y3) = points

        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if d == 0:
            raise ValueError("Punkty są współliniowe, nie można utworzyć okręgu.")

        cx = (
                ((x1 ** 2 + y1 ** 2) * (y2 - y3) +
                 (x2 ** 2 + y2 ** 2) * (y3 - y1) +
                 (x3 ** 2 + y3 ** 2) * (y1 - y2)) / d
        )
        cy = (
                ((x1 ** 2 + y1 ** 2) * (x3 - x2) +
                 (x2 ** 2 + y2 ** 2) * (x1 - x3) +
                 (x3 ** 2 + y3 ** 2) * (x2 - x1)) / d
        )

        # Promień okręgu
        radius = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)

        return cls(cx, cy, radius)

    @property
    def top(self):
        return self.pt.y - self.radius

    @property
    def bottom(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)


c1 = Circle.from_points(([1, 0], [2, 5], [4, 8]))
print(c1)
print(f"Środek: ({c1.pt.x}, {c1.pt.y})")
print(f"Promień: {c1.radius}")


