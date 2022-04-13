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
    def __init__(self):
        super().__init__()

        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.paddle_move)

    # The ball bump into paddle
    def ball_hits_paddle(self):
        paddle_left = self.paddle.x
        paddle_right = self.paddle.x + self.paddle.width
        is_x_hit_paddle = self.ball.x + self.ball.width >= paddle_left and self.ball.x <= paddle_right

        paddle_top = self.paddle.y
        paddle_bottom = self.paddle.y + self.paddle.height
        is_y_hit_paddle = self.ball.y + self.ball.height >= paddle_top and self.ball.y <= paddle_bottom

        return is_x_hit_paddle and is_y_hit_paddle

    # Mouse listeners
    def handle_click(self, event):
        self.set_ball_velocity()
        if event.y > 0:
            self.started = True
        return self.started

    # Define range of paddle moving
    def paddle_move(self, event):
        if self.window.width - self.paddle.width / 2 >= event.x >= self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width / 2
