from campy.graphics.gwindow import GWindow
# from robot import Robot
# from sub_robot import SubRobot
from super_robot import SuperRobot
import robot

# Global variables
# window = GWindow()
# r1 = Robot(180, 73, color='red')
# r2 = Robot(160, 50)
# r3 = SubRobot(170, 60, color='magenta', count=5)
r4 = SuperRobot(170, 60, 'blue', color='yellow', count=10)


def main():
    global r1, r2, r3, r4
    # generate_ball()
    # intro()
    # bmi()
    # say_hey()
    # r3_act()
    # r4_act()
    print(robot.__name__)
    print(SuperRobot.__name__)
    print(r4.__name__)


def r4_act():
    r4.say_cool()
    r4.bmi()
    r4.intro()
    r4.start_count()
    b4 = r4.give_me_a_ball(300)
    rc4 = r4.give_me_a_rect(100)
    window.add(b4)
    window.add(rc4)


def r3_act():
    r3.say_cool()
    r3.bmi()
    r3.intro()
    r3.start_count()
    ball3 = r3.give_me_a_ball(100)
    # window.add(ball3)


def say_hey():
    Robot.say_hey()
    r1.say_cool()


def intro():
    print('r2_intro:', r2.intro())


def bmi():
    print('r1_BMI:', r1.bmi())


def generate_ball():
    b1 = r1.give_me_a_ball(500)
    b2 = r2.give_me_a_ball(300)
    # window.add(b1)
    # window.add(b2)


if __name__ == '__main__':
    print('[robot_starter.py] __name__:', __name__)
    main()
