from campy.graphics.gobjects import GOval


class Robot:
    # Constructor
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    @staticmethod
    def say_hey():
        print('hey')

    @staticmethod
    def say_cool():
        print('guys, it\'s cool')

    # Methods
    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def intro(self):
        print(f'height: {self.h} / weight: {self.w}')

    def bmi(self):
        # weight / height_in_meter**2
        height_in_meter = self.h/100
        bmi = self.w / height_in_meter**2
        print(round(bmi, 2))


if __name__ == '__main__':
    print('[robot.py] __name__:', __name__)


if __name__ == 'robot':
    print('Thanks for using robot. Now we also release new version: SuperRobot. Try it!')
