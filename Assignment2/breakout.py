"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

BREAKOUT GAME, TRY IT!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3		   # Number of attempts

# Global variables
graphics = BreakoutGraphics()
ball = graphics.ball
lives = NUM_LIVES


def main():
    global graphics, ball, lives
    while True:
        # GAME OVER
        if lives <= 0:
            break

        # Ball Collision
        ball_collision()

        # Ball touch window Edge
        check_if_ball_touch_window_edge()

        # Update
        if graphics.started:
            ball.move(graphics.get_vx(), graphics.get_vy())

        # Pause
        pause(FRAME_RATE)


def ball_collision():
    for x, y in graphics.corners(ball):  # Get 4 corners of the ball
        obj = graphics.window.get_object_at(x, y)
        if isinstance(obj, type(graphics.paddle)):
            if obj is not graphics.paddle:
                graphics.window.remove(obj)
            graphics.set_vy()
            break  # it means one corner has collided


def check_if_ball_touch_window_edge():
    global lives
    if ball.x <= 0 or ball.x + ball.width >= graphics.window.width:
        graphics.set_vx()
    if ball.y <= 0:
        graphics.set_vy()
    if ball.y + ball.height >= graphics.window.height:
        lives -= 1
        graphics.set_ball()


if __name__ == '__main__':
    main()
