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

    # Mouse listeners
    def handle_click(self, event):
        if self.get_vy() != 0 or event.y < 0:
            return
        self.set_ball_velocity()
        self.started = True
