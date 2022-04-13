"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3		   # Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball = graphics.ball

    # Add the animation loop here!
    while True:
        # Ball Collision
        ball_collision(graphics)

        # Ball touch window Edge
        check_if_ball_touch_window_edge(graphics)

        # Update
        if graphics.started:
            ball.move(graphics.get_vx(), graphics.get_vy())

        # Pause
        pause(FRAME_RATE)


def ball_collision(graphics):
    ball = graphics.ball
    for x, y in ball_corners(ball):  # Get 4 corners of the ball
        obj = graphics.window.get_object_at(x, y)
        if obj is not None:
            # graphics.set_vx()
            graphics.set_vy()
            if obj is not graphics.paddle and isinstance(obj, type(graphics.paddle)):
                graphics.window.remove(obj)
                break  # if one corner has collided


def check_if_ball_touch_window_edge(graphics):
    ball = graphics.ball
    if graphics.ball_hits_paddle() or ball.x <= 0 or ball.x + ball.width >= graphics.window.width:
        graphics.set_vx()
    if graphics.ball_hits_paddle() or ball.y <= 0:
        graphics.set_vy()
    if ball.y + ball.height >= graphics.window.height:
        graphics.set_ball()


def ball_corners(obj):
    return [
        (obj.x, obj.y),
        (obj.x + obj.width, obj.y),
        (obj.x, obj.y + obj.height),
        (obj.x + obj.width, obj.y + obj.height)
    ]


if __name__ == '__main__':
    main()
