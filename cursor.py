from terminal import Terminal


class Cursor:
    Escape = "\x1b["
    stupid_character_to_stop_thing = "]"
    CR = "\r"
    NL = "\n"
    Home_pos = f"{Escape}H"

    def __init__(self):
        self.x = 0
        self.y = 0
        terminal = Terminal()
        self.max_x = terminal.columns
        self.max_y = terminal.rows

    def return_home(self):
        self.x, self.y = 0, 0
        print(self.Home_pos, end="")

    def set_pos(self, x: int, y: int):
        self.x, self.y = x, y
        print(f"{self.Escape}{y};{x}H", end="")

    def place_letter(self, x: int, y: int, letter: str):
        self.set_pos(x, y)
        print(letter, end="")

    def draw_line(self, x1, y1, x2, y2):
        for i in range(x1, x2):
            self.place_letter(i, y1, "x")

    def draw_rect(self, x: int, y: int, height: int, width: int):
        for i in range(x, width + x + 1):
            pass
