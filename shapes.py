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

    def _draw_lineH(self) -> list[Point]:
        points = []
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        delta_x = x2 - x1
        delta_y = y2 - y1

        dir = -1 if delta_y < 0 else 1
        delta_y *= dir
        if delta_x != 0:
            y = y1
            decision = 2*delta_y - delta_x
            for i in range(delta_x + 1):
                points.append(Point(x1 + i, y))

                if decision > 0:
                    y += dir
                    decision -= 2*delta_x
                decision += 2*delta_y

        return points

    def _draw_lineV(self) -> list[Point]:
        points = []
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        delta_x = x2 - x1
        delta_y = y2 - y1

        dir = -1 if delta_x < 0 else 1
        delta_x *= dir
        if delta_y != 0:
            x = x1
            decision = 2*delta_x - delta_y
            for i in range(delta_y + 1):
                points.append(Point(x, y1 + i))

                if decision > 0:
                    x += dir
                    decision -= 2*delta_y
                decision += 2*delta_x

        return points

    def _find_slope(self):
        x = self.p2.x - self.p1.x
        y = self.p2.y - self.p1.y
        if y == 0 or x == 0:
            return (x, y)
        reduced_fraction = _reduce_fraction(x, y)
        return reduced_fraction

    def list_points(self) -> list[Point]:
        """ Terminal 'ratio' not 1 to 1, so I'm wondering
            if it would be a good idea to 'translate' the users 1 to 1
            input to match how the terminal would like it printed most?

            As in the math for the slope is wrong and maybe
            I have to translate it to a good slope?
            Or cut the line from flattening out?"""
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        if abs(x2 - x1) > abs(y2 - y1):
            return self._draw_lineH()
        else:
            return self._draw_lineV()


class Rectangle:
    def __init__(self, upper_corner: Point, height: int, width: int):
        self.x = upper_corner.x
        self.y = upper_corner.y
        self.height = height
        self.width = width

    def list_points(self):
        points = []
        lines = []
        lines.append(Line(Point(self.x, self.y),
                          Point(self.x, self.y + self.height)))
        lines.append(Line(Point(self.x, self.y + self.height),
                          Point(self.x + self.width, self.y + self.height)))
        lines.append(Line(Point(self.x + self.width, self.y + self.height),
                          Point(self.x + self.width, self.y)))
        lines.append(Line(Point(self.x + self.width, self.y),
                          Point(self.x, self.y)))
        for line in lines:
            points.extend(line.list_points())
        return points


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
        self.radius = radius

    def list_points():
        pass


def _reduce_fraction(numerator, denominator) -> tuple[int]:
    gcd = math.gcd(numerator, denominator)

    numerator //= gcd
    denominator //= gcd
    return (numerator, denominator)
