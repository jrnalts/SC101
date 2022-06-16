"""
File: bouncing_ball.py
Name: Bouncing ball
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 15
GRAVITY = 1
SIZE = 30
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0  # count for ball over edge
vy = 0  # initial falling speed


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing)
    origin()


def bouncing(e):
    global ball, count, vy
    if vy != 0:
        return
    vy = GRAVITY
    """
    Prevent action when dragging window
    Maximum times for playing: 3
    """
    while e.y > 0 and count < 3:
        if ball.x > window.width:
            count += 1
            vy = 0  # ball stop, initialize falling speed
            origin()
            break

        # ball falling
        vy += GRAVITY
        ball.move(VX, vy)

        # bounce
        if ball.y + SIZE / 2 > window.height:
            vy = -vy * REDUCE
        pause(DELAY)


def origin():
    global ball
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    ball.color = 'orangered'
    ball.fill_color = 'orangered'
    window.add(ball)


if __name__ == "__main__":
    main()
