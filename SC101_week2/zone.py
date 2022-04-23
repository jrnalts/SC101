from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()
    ball = graphics.ball
    lives = NUM_LIVES

    while True:
        if lives == 0:
            break

        # Gate keeper
        if graphics.ball_in_zone():
            lives -= 1
            graphics.set_ball()

        # Ball touch window edge
        if ball.x <= 0 or ball.x + ball.width >= graphics.window.width:
            graphics.vx *= -1
        if ball.y <= 0 or ball.y + ball.height >= graphics.window.height:
            graphics.vy *= -1

        # Update
        ball.move(graphics.vx, graphics.vy)

        # Pause
        pause(FRAME_RATE)



if __name__ == '__main__':
    main()
