from cursor import Cursor
from shapes import Point

cursor = Cursor()
cursor.draw_custom_ascii(1, 1,
                         r"""

    ---   ---
       \ /
        v
""")
cursor.draw_line(Point(5, 5), Point(5, 100))
cursor.draw_rect(1, 1, 20, 20)
cursor.return_home()


# Idea for an ascii shape editor?
# Tool to make ascii art easier to make
