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


def main():
    global graphics, ball

    # Add the animation loop here!
    while True:
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
    for x, y in graphics.ball_corners():  # Get 4 corners of the ball
        obj = graphics.window.get_object_at(x, y)
        if obj is not None:
            if graphics.get_vy() > 0:
                graphics.set_vx()
            graphics.set_vy()

            if obj is not graphics.paddle and isinstance(obj, type(graphics.paddle)):
                graphics.window.remove(obj)
                break  # one corner has collided


def check_if_ball_touch_window_edge():
    if graphics.ball_hits_paddle() or ball.x <= 0 or ball.x + ball.width >= graphics.window.width:
        graphics.set_vx()
    if graphics.ball_hits_paddle() or ball.y <= 0:
        graphics.set_vy()
    if ball.y + ball.height >= graphics.window.height:
        graphics.set_ball()


if __name__ == '__main__':
    main()
