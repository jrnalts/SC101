from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 3
MIN_Y_SPEED = 2
NUM_LIVES = 3


class ZoneGraphics:
    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):

        # Create window
        self.window = GWindow(width=window_width, height=window_height, title='zone game')

        # Create zone
        self.zone = GRect(width=zone_width, height=zone_height)
        self.set_zone()

        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.vx = 0
        self.vy = 0
        self.set_ball()

        # Initialize mouse listeners
        onmouseclicked(self.handle_click)

    def set_zone(self):
        self.zone.color = 'blue'
        self.window.add(self.zone,
                        x=(self.window.width - self.zone.width) / 2,
                        y=(self.window.height - self.zone.height) / 2)

    # set ball initial status
    def set_ball(self):
        self.ball.filled = True
        self.ball.fill_color = self.ball.color = 'peru'
        self.ball.lives = NUM_LIVES
        self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

        # if ball in the zone, reset it
        while self.ball_in_zone():
            self.set_ball_position()

    # give ball a random position
    def set_ball_position(self):
        self.ball.x = random.randint(0, self.window.width - self.ball.width)
        self.ball.y = random.randint(0, self.window.height - self.ball.height)

    # give ball a random velocity
    def set_ball_velocity(self):
        self.vx = random.randint(0, MAX_SPEED)
        self.vy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.vx *= -1
        if random.random() > 0.5:
            self.vy *= -1

    # check if ball in the zone
    def ball_in_zone(self):
        zone_left = self.zone.x
        zone_right = self.zone.x + self.zone.width
        # 球的 X座標+球寬 大於等於 zone 的 X座標:   表示球在 zone 左側的右邊
        # 球的 X座標 小於等於 zone 的 X座標+zone寬: 表示球在 zone 右側的左邊
        is_x_in_zone = self.ball.x + self.ball.width >= zone_left and self.ball.x <= zone_right

        zone_top = self.zone.y
        zone_bottom = self.zone.y + self.zone.height
        # 球的 Y座標+球高 大於等於 zone 的 Y座標:   表示球在 zone 頂側的下方
        # 球的 Y座標 小於等於 zone 的 Y座標+zone高: 表示球在 zone 底側的上方
        is_y_in_zone = self.ball.y + self.ball.height >= zone_top and self.ball.y <= zone_bottom

        return is_x_in_zone and is_y_in_zone

    def handle_click(self, event):
        if self.window.get_object_at(event.x, event.y) == self.ball:
            self.set_ball()

