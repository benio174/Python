import math
import pytest
from circles import Circle

@pytest.fixture
def circles():
    return {
        "a": Circle(2, 0, 4),
        "b": Circle(0, 0, 2),
        "c": Circle(2, 0, 4),
        "d": Circle(0, 0, 6),
        "e": Circle(0, 0, 5),
        "f": Circle(10, 0, 4),
        "g": Circle(2, 2, 3),
        "h": Circle(6, 0, 4),
        "i": Circle(6, 5, 2),
    }

def test_repr(circles):
    assert repr(circles["a"]) == "Circle(2, 0, 4)"
    assert repr(circles["b"]) == "Circle(0, 0, 2)"

def test_eq(circles):
    assert circles["a"] == circles["c"]
    assert circles["a"] != circles["b"]
    assert circles["b"] != circles["d"]

def test_area(circles):
    assert math.isclose(circles["a"].area(), math.pi * 16)
    assert math.isclose(circles["b"].area(), math.pi * 4)
    assert math.isclose(circles["d"].area(), math.pi * 36)

def test_move(circles):
    assert circles["a"].move(2, 1) == Circle(4, 1, 4)
    assert circles["a"].move(-2, 1) == Circle(0, 1, 4)
    assert circles["b"].move(-2, -3) == Circle(-2, -3, 2)

def test_cover(circles):
    assert circles["b"].cover(circles["e"]) == Circle(0, 0, 5)
    assert circles["e"].cover(circles["b"]) == Circle(0, 0, 5)
    assert circles["a"].cover(circles["f"]) == Circle(6, 0, 8)
    assert circles["e"].cover(circles["h"]) == Circle(2.5, 0, 7.5)
    assert circles["g"].cover(circles["i"]) == Circle(3.6, 3.2, 5)

def test_from_points():
    circle = Circle.from_points(((0, 0), (4, 0), (2, 4)))
    assert math.isclose(circle.pt.x, 2)
    assert math.isclose(circle.pt.y, 1.5)
    assert math.isclose(circle.radius, math.sqrt(6.25))

    with pytest.raises(ValueError, match="Punkty są współliniowe"):
        Circle.from_points(((0, 0), (2, 0), (4, 0)))

    with pytest.raises(ValueError, match="Punkty są współliniowe"):
        Circle.from_points(((1, 1), (1, 1), (3, 3)))

    with pytest.raises(ValueError, match="Musisz podać dokładnie trzy punkty"):
        Circle.from_points(((0, 0), (1, 1)))

    with pytest.raises(ValueError, match="Musisz podać dokładnie trzy punkty"):
        Circle.from_points("niepoprawny argument")