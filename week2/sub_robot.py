from robot import Robot


class SubRobot(Robot):
    def __init__(self, height, weight, color, count):
        super().__init__(height, weight, color)
        self.count = count

    def start_count(self):
        for i in range(self.count):
            print('...', i + 1)
