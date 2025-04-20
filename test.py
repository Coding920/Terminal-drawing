import time
from cursor import Cursor
import shapes as s

cursor = Cursor()
cursor.draw_triangle(
    s.Point(12, 12, "x"),
    s.Point(24, 24, "x"),
    s.Point(0, 24, "x")
)
cursor.return_home()

# Idea for an ascii shape editor?
# Tool to make ascii art easier to make

# cursor.draw_custom_ascii(1, 1, r""" ---   --- \ / v """)
