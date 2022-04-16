"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

BREAKOUT GRAPHICS FOCUS ON MOUSE LISTENER EVENTS
"""
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from breakoutgraphics_super import BreakoutGraphicsSuper


class BreakoutGraphics(BreakoutGraphicsSuper):
    def __init__(self, **args):
        super().__init__(**args)

        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.paddle_move)

    # The ball bump into paddle
    def ball_hits_paddle(self):
        is_x_hit_paddle = self.ball.x + self.ball.width >= self.paddle.x and \
            self.ball.x <= self.paddle.x + self.paddle.width
        is_y_hit_paddle = self.ball.y + self.ball.height >= self.paddle.y and \
            self.ball.y <= self.paddle.y + self.paddle.height

        return is_x_hit_paddle and is_y_hit_paddle

    # Mouse listeners
    def handle_click(self, event):
        if self.get_vy() > 0 or event.y < 0:
            return

        self.set_ball_velocity()
        self.started = True

    # Define range of paddle moving
    def paddle_move(self, event):
        if self.window.width - self.paddle.width / 2 >= event.x >= self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width / 2
