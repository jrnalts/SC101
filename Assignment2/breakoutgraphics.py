"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 3    # Initial vertical speed for the ball
MAX_X_SPEED = 3        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3		   # Number of attempts
COLORS = ('red', 'sandybrown', 'orange', 'gold', 'yellow', 'greenyellow', 'green', 'cadetblue', 'blue', 'purple')


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.paddle_offset = paddle_offset
        self.set_paddle()

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.vx = 0
        self.vy = 0
        self.set_ball()

        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.set_bricks()

    # initialize paddle
    def set_paddle(self):
        self.paddle.filled = True
        self.paddle.fill_color = self.paddle.color = 'black'
        self.window.add(self.paddle,
                        x=(self.window.width - self.paddle.width) / 2,
                        y=(self.window.height - self.paddle.paddle_offset))

    # initialize ball
    def set_ball(self):
        self.ball.filled = True
        self.ball.fill_color = self.ball.color = 'black'
        self.ball.lives = NUM_LIVES
        self.set_ball_position()
        # Default initial velocity for the ball
        self.set_ball_velocity()
        self.window.add(self.ball)

    # give ball a random position
    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    # give ball a random velocity
    def set_ball_velocity(self):
        self.vx = random.randint(1, MAX_X_SPEED)
        self.vy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.vx *= -1
        if random.random() > 0.5:
            self.vy *= -1

    def set_bricks(self):
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                brick.color = brick.fill_color = COLORS[col]

                brick_x = row * (self.brick_width + self.brick_spacing)
                brick_y = self.brick_offset + col * (self.brick_height + self.brick_spacing)
                self.window.add(brick, x=brick_x, y=brick_y)

    # ball bump into paddle
    def ball_hits_paddle(self):
        zone_left = self.paddle.x
        zone_right = self.paddle.x + self.paddle.width
        is_x_in_zone = self.ball.x + self.ball.width >= zone_left and self.ball.x <= zone_right

        zone_top = self.paddle.y
        zone_bottom = self.paddle.y + self.paddle.height
        is_y_in_zone = self.ball.y + self.ball.height >= zone_top and self.ball.y <= zone_bottom

        return is_x_in_zone and is_y_in_zone

    def handle_click(self, event):
        return True
        # self.window.get_object_at(event.x, event.y) == self.ball

    def paddle_move(self, event):
        if self.window.width - self.paddle.width / 2 >= event.x >= self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width / 2

