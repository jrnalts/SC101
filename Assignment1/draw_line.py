"""
File: draw_line.py
Name: Draw line
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 10

# Global Variable
window = GWindow()
switch = True  # True: set point ; False: draw line
dp = None  # point's position


def main():
    onmouseclicked(draw_line)


def draw_line(e):
    global switch, dp
    if e.y >= 0:  # prevent action when dragging window
        dx, dy = find_center(e)
        if switch:
            window.add(GOval(SIZE, SIZE, x=dx, y=dy))
            dp = (e.x, e.y)  # Record the position of current point
            switch = False
        else:
            if dp is not None:
                window.remove(window.get_object_at(dp[0], dp[1]))
                window.add(GLine(dp[0], dp[1], dx, dy))
            switch = True


def find_center(e):
    return e.x - SIZE / 2, e.y - SIZE / 2


if __name__ == "__main__":
    main()
