from terminal import Terminal
from terminal import Terminal as term
from shapes import Point, Line, Rectangle, Triangle, Circle


class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0
        terminal = Terminal()
        self.max_x = terminal.columns
        self.max_y = terminal.rows

    def return_home(self):
        self.x, self.y = 0, 0
        print(term.Home_pos, end="")

    def set_pos(self, point: Point):
        self.x, self.y = point.x, point.y + 1
        print(f"{term.Escape}{self.x};{self.y}H", end="")

    def place_letter(self, point: Point, letter: str):
        self.set_pos(point)
        print(letter, end="")

    def draw_line(self, p1: Point, p2: Point):
        line = Line(p1, p2)
        points = line.list_points()
        for point in points:
            self.place_letter(point, "x")

    def draw_rect(self, x: int, y: int, height: int, width: int):
        self.draw_line(x, y, x + width, y)
        self.draw_line(x, y + height, x + width, y + height)
        self.draw_line(x, y, x, y + height)
        self.draw_line(x + width, y, x + width, y + height)
