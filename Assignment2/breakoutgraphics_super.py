"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

SUPER CLASS OF BREAKOUT GRAPHICS FOR BASIC CONFIG
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
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
COLORS = ('red', 'sandybrown', 'orange', 'gold', 'yellow', 'greenyellow', 'green', 'cadetblue', 'blue', 'purple')


class BreakoutGraphicsSuper:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle_offset = paddle_offset
        self.set_paddle()

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.set_bricks()

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.set_ball()

        # Set velocity for the ball
        self.__vx = 0
        self.__vy = 0

        # The switch to check game is started or not
        self.started = False

    # Default initial values for the paddle
    def set_paddle(self):
        self.paddle.filled = True
        self.paddle.fill_color = self.paddle.color = 'black'
        self.paddle.x = (self.window.width - self.paddle.width) / 2
        self.paddle.y = self.window.height - self.paddle_offset
        self.window.add(self.paddle)

    # Build all bricks on the window
    def set_bricks(self):
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                brick.color = brick.fill_color = COLORS[col]

                brick_x = row * (self.brick_width + self.brick_spacing)
                brick_y = self.brick_offset + col * (self.brick_height + self.brick_spacing)
                self.window.add(brick, x=brick_x, y=brick_y)

    # Default initial values for the ball
    def set_ball(self):
        self.reset()
        self.ball.filled = True
        self.ball.fill_color = self.ball.color = 'black'
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.window.add(self.ball)

    # Set for game start or restart
    def reset(self):
        self.__vx = 0
        self.__vy = 0
        self.started = False

    def set_ball_velocity(self):
        self.__vx = random.randint(1, MAX_X_SPEED)
        self.__vy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__vx *= -1

    # Getters and Setters of velocity
    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def set_vx(self):
        self.__vx *= -1

    def set_vy(self):
        self.__vy *= -1
