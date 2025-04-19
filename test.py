import time
from cursor import Cursor
import shapes as s

cursor = Cursor()
for i in range(50):
    cursor.cursor_invisible()
    upper_corner = s.Point(5 + i, 5 + i, "*")
    cursor.draw_rect(upper_corner, 20, 20)
    time.sleep(.1)
    cursor.clear_screen()
cursor.cursor_visible()
cursor.return_home()

# Idea for an ascii shape editor?
# Tool to make ascii art easier to make

# cursor.draw_custom_ascii(1, 1, r""" ---   --- \ / v """)
