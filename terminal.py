import shutil


class Terminal:
    Escape = "\x1b["
    CR = "\r"
    NL = "\n"
    Home_pos = f"{Escape}H"

    def __init__(self):
        self.size = shutil.get_terminal_size()
        self.rows = self.size.lines
        self.columns = self.size.columns
