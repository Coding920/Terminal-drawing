import time
from cursor import Cursor
import shapes as s

cursor = Cursor()
for i in range(50):
    cursor.cursor_invisible()
    cursor.draw_rect(5 + i, 5, 20, 20)
    time.sleep(.1)
    cursor.clear_screen()
cursor.cursor_visible()
cursor.return_home()

# Idea for an ascii shape editor?
# Tool to make ascii art easier to make

# cursor.draw_custom_ascii(1, 1, r""" ---   --- \ / v """)
