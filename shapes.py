import math


NUMERATOR = 0
DENOMINATOR = 1


class Point:
    def __init__(self, x, y, letter=None):
        self.x = x
        self.y = y
        self.letter = letter


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
                points.append(Point(x1 + i, y, self.p1.letter))

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
                points.append(Point(x, y1 + i, self.p1.letter))

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
    def __init__(self,
                 top_left: Point,
                 top_right: Point,
                 bottom_left: Point,
                 bottom_right: Point):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def list_points(self) -> list[Point]:
        points = []
        top = Line(self.top_left, self.top_right)
        right = Line(self.top_right, self.bottom_right)
        bottom = Line(self.bottom_left, self.bottom_right)
        left = Line(self.bottom_left, self.top_left)
        points.extend(top.list_points())
        points.extend(right.list_points())
        points.extend(bottom.list_points())
        points.extend(left.list_points())
        return points


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def list_points(self) -> list[Point]:
        points = []
        sides = []
        sides.append(Line(self.p1, self.p2))
        sides.append(Line(self.p2, self.p3))
        sides.append(Line(self.p3, self.p1))
        for side in sides:
            points.extend(side.list_points())
        return points


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
