import math


NUMERATOR = 0
DENOMINATOR = 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.slope = self._find_slope()

    def list_points(self) -> list[Point]:
        points = [Point(self.p2.x, self.p2.y)]
        x = self.p2.x
        y = self.p2.y

        while x > self.p1.x and y > self.p1.y:
            x -= self.slope[NUMERATOR]
            y -= self.slope[DENOMINATOR]
            if x % 1 == 0 and y % 1 == 0:
                points.append(Point(x, y))

        points.append(Point(self.p1.x, self.p1.y))
        return points

    def _find_slope(self):
        x = self.p2.x - self.p1.x
        y = self.p2.y - self.p1.y
        if y == 0 or x == 0:
            return (x, y)
        reduced_fraction = _reduce_fraction(x, y)
        return reduced_fraction


class Rectangle:
    def __init__(self, upper_corner: Point, height: int, width: int):
        self.x = upper_corner.x
        self.y = upper_corner.y
        self.height = height
        self.width = width


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.x1 = p1.x
        self.x2 = p2.x
        self.x3 = p3.x
        self.y1 = p1.y
        self.y2 = p2.y
        self.y3 = p3.y


class Circle:
    def __init__(self, center: Point, radius):
        self.x = center.x
        self.y = center.y


def _reduce_fraction(numerator, denominator) -> tuple[int]:
    gcd = math.gcd(numerator, denominator)

    numerator //= gcd
    denominator //= gcd
    return (numerator, denominator)
