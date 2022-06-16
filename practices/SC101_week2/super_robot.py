from sub_robot import SubRobot
from campy.graphics.gobjects import GRect


class SuperRobot(SubRobot):
    def __init__(self, height, weight, rect_color, color, count):
        super().__init__(height, weight, color, count)
        self.r_c = rect_color

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect
