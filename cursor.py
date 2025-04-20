from terminal import Terminal
from terminal import Terminal as term
from shapes import Point, Line, Rectangle, Triangle, Circle


class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0
        terminal = Terminal()
        self.max_x = terminal.columns
        self.max_y = terminal.rows - 1  # Account for home row

    def cursor_invisible(self):
        print(f"{term.Cursor_invisible}", end="", flush=True)

    def cursor_visible(self):
        print(f"{term.Cursor_visible}", end="", flush=True)

    def clear_screen(self):
        print(term.Clear_screen, end="", flush=True)

    def return_home(self):
        self.x, self.y = 0, 0
        print(term.Home_pos, end="", flush=True)

    def set_pos(self, point: Point):
        self.x, self.y = point.x, point.y + 1
        print(f"{term.Escape}{self.y};{self.x}H", end="", flush=True)

    def place_point(self, point: Point):
        if point.y > self.max_y:
            return
        self.set_pos(point)
        print(point.letter, end="", flush=True)

    def place_points(self, points: list[Point]):
        for point in points:
            self.place_point(point)

    def draw_line(self, p1: Point, p2: Point):
        """
        Draws line from point 1 to point 2 using
        the bresenham's line algorithm
        """
        line = Line(p1, p2)
        points = line.list_points()
        self.place_points(points)

    def draw_rect(self,
                  top_left: Point,
                  top_right,
                  bottom_left,
                  bottom_right):
        rect = Rectangle(top_left, top_right, bottom_left, bottom_right)
        points = rect.list_points()
        self.place_points(points)

    def draw_triangle(self, p1: Point, p2, p3):
        triangle = Triangle(p1, p2, p3)
        points = triangle.list_points()
        self.place_points(points)

    def draw_circle(self, center_point: Point, radius: int):
        circle = Circle(center_point, radius)
        points = circle.list_points()
        self.place_points(points)

    def draw_custom_ascii(self, x, y, ascii):
        self.set_pos(Point(x, y))
        print(ascii, end="", flush=True)
