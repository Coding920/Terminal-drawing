import shutil


class Terminal:
    Escape = "\x1b["
    CR = "\r"
    NL = "\n"
    Home_pos = f"{Escape}H"
    Clear_screen = "\x1bc"
    Cursor_invisible = f"{Escape}?25l"
    Cursor_visible = f"{Escape}?25h"

    def __init__(self):
        self.size = shutil.get_terminal_size()
        self.rows = self.size.lines
        self.columns = self.size.columns
