import os


class Terminal:
    def __init__(self):
        self.size = os.get_terminal_size()
        self.rows = self.size.lines
        self.columns = self.size.columns
