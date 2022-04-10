"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
img = GImage('mole.png')
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='whack_a_mole')
score = 0
score_board = GLabel('Score: ' + str(score))


def main():
    onmouseclicked(whack)
    score_board.font = '-60'
    window.add(score_board, x=0, y=score_board.height)

    while True:
        generate_mole()
        pause(DELAY)


def whack(e):
    global score
    obj = window.get_object_at(e.x, e.y)
    if obj is not None and obj is not score_board:
        window.remove(obj)
        score += 1
        score_board.text = 'Score: ' + str(score)


def generate_mole():
    # img = GImage('mole.png')
    max_width = window.width - img.width
    max_height = window.height - img.height
    random_x = random.randint(0, max_width)
    random_y = random.randint(score_board.height, max_height)
    window.add(img, x=random_x, y=random_y)


if __name__ == '__main__':
    main()
