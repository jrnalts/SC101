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

    # Add the animation loop here!
    ball = graphics.ball
    lives = NUM_LIVES

    while True:
        if lives == 0:
            break

        # Bounce
        # self.window.get_object_at(event.x, event.y) == self.ball

        # Ball touch window edge
        if graphics.ball_hits_paddle() or ball.x <= 0 or ball.x + ball.width >= graphics.window.width:
            graphics.set_vx()
        if graphics.ball_hits_paddle() or ball.y <= 0 or ball.y + ball.height >= graphics.window.height:
            graphics.set_vy()

        # Update
        if graphics.is_started:
            ball.move(graphics.get_vx(), graphics.get_vy())

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
