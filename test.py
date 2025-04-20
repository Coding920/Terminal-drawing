import time
from cursor import Cursor
import shapes as s

cursor = Cursor()


def main():
    cursor.clear_screen()
    rect_demo()
    circle_demo()
    line_demo()
    cursor.cursor_visible()
    cursor.return_home()


def rect_demo():
    ofsx = 0  # Offset X
    ofsy = 0  # Offset Y
    for _ in range(11):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        cursor.draw_rect(
            s.Point(5+ofsx, 5+ofsy, "x"),
            s.Point(10+ofsx, 5+ofsy, "x"),
            s.Point(5+ofsx, 10+ofsy, "x"),
            s.Point(10+ofsx, 10+ofsy, "x")
        )
        time.sleep(0.05)
    for _ in range(1, 11):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsy += 1
        cursor.draw_rect(
            s.Point(5+ofsx, 5+ofsy, "x"),
            s.Point(10+ofsx, 5+ofsy, "x"),
            s.Point(5+ofsx, 10+ofsy, "x"),
            s.Point(10+ofsx, 10+ofsy, "x")
        )
        time.sleep(0.05)
    for _ in range(1, 11):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx -= 1
        cursor.draw_rect(
            s.Point(5+ofsx, 5+ofsy, "x"),
            s.Point(10+ofsx, 5+ofsy, "x"),
            s.Point(5+ofsx, 10+ofsy, "x"),
            s.Point(10+ofsx, 10+ofsy, "x")
        )
        time.sleep(0.05)
    for _ in range(1, 11):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsy -= 1
        cursor.draw_rect(
            s.Point(5+ofsx, 5+ofsy, "x"),
            s.Point(10+ofsx, 5+ofsy, "x"),
            s.Point(5+ofsx, 10+ofsy, "x"),
            s.Point(10+ofsx, 10+ofsy, "x")
        )
        time.sleep(0.05)
    # Transform Rect
    for _ in range(16):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        ofsy += 1
        cursor.draw_rect(
            s.Point(5, 5, "x"),
            s.Point(10+ofsx, 5, "x"),
            s.Point(5, 10+ofsy, "x"),
            s.Point(10+ofsx, 10+ofsy, "x")
        )
        time.sleep(0.05)
    # Rotate Rect
    ofsx, ofsy = 0, 0
    for _ in range(20):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        ofsy += 1
        cursor.draw_rect(
            s.Point(5+ofsx, 5, "x"),
            s.Point(25, 5+ofsy, "x"),
            s.Point(5, 25-ofsy, "x"),
            s.Point(25-ofsx, 25, "x")
        )
        time.sleep(0.1)


def circle_demo():
    ofs = 0  # offset
    for _ in range(11):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofs += 1
        cursor.draw_circle(
            s.Point(20, 20, "x"),
            8 + ofs
        )
        time.sleep(0.1)
    time.sleep(0.5)
    for _ in range(1, 16):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofs -= 1
        cursor.draw_circle(
            s.Point(20, 20, "x"),
            8 + ofs
        )
        time.sleep(0.1)
    ofsx, ofsy = 0, 0
    for _ in range(1, 16):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        ofsy += 1
        cursor.draw_circle(
            s.Point(20+ofsx, 20+ofsy, "x"),
            8 + ofs
        )
        time.sleep(0.1)
    for _ in range(1, 16):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        ofsy -= 1
        cursor.draw_circle(
            s.Point(20+ofsx, 20+ofsy, "x"),
            8 + ofs
        )
        time.sleep(0.1)


def line_demo():
    ofsx = 0
    for _ in range(15):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        cursor.draw_line(
            s.Point(30, 15, "x"),
            s.Point(30+ofsx, 30)
        )
        time.sleep(0.1)
    ofsx, ofsy = 0, 0
    for _ in range(15):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        ofsy += 1
        cursor.draw_line(
            s.Point(30, 15, "x"),
            s.Point(45, 30)
        )
        cursor.draw_line(
            s.Point(30-ofsx, 15+ofsy, "x"),
            s.Point(45, 30)
        )
        time.sleep(0.1)
    ofsx, ofsy = 0, 0
    for _ in range(15):
        cursor.clear_screen()
        cursor.cursor_invisible()
        ofsx += 1
        ofsy += 1
        cursor.draw_line(
            s.Point(30, 15, "x"),
            s.Point(45, 30)
        )
        cursor.draw_line(
            s.Point(15, 30, "x"),
            s.Point(45, 30)
        )
        cursor.draw_line(
            s.Point(15, 30, "x"),
            s.Point(45-ofsx, 30-ofsy)
        )
        time.sleep(0.1)

# Idea for an ascii shape editor?
# Tool to make ascii art easier to make

# cursor.draw_custom_ascii(1, 1, r""" ---   --- \ / v """)
# cursor.draw_triangle(
#     s.Point(12, 12, "x"),
#     s.Point(24, 24, "x"),
#     s.Point(0, 24, "x")
# )


main()
