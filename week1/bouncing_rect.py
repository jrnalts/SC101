"""
File: bouncing_rect.py
Name: 
------------------------
This file shows how to make a simple 
animation by campy library
"""

from campy.graphics.gobjects import GOval, GRect, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 100

# This controls the pause time (in millisecond) for the animation
DELAY = 10

# This controls the distance pixel of object
DISTANCE = 5


def main():
	window = GWindow()
	rect = set_obj()
	window.add(rect, x=(window.width - SIZE) / 2, y=(window.height - SIZE) / 2)
	vx = DISTANCE
	while True:
		rect.move(vx, 0)
		if rect.x <= 0 or (rect.x + SIZE) >= window.width:
			vx = -vx
		pause(10)


def set_obj():
	rect = GArc(SIZE, SIZE, 0, 90)
	rect.filled = True
	rect.fill_color = 'grey'
	rect.color = 'grey'
	return rect


if __name__ == '__main__':
	main()
