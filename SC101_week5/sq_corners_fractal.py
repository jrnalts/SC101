"""
File: sq_corners_fractal.py
Name:
-----------------------------------
This program draws a fractal with GRect on GWindow.
Students will find it useful to understand the order
of each recursive calls.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GRect
from campy.gui.events.timer import pause

# Constants
SIZE = 300      # It controls the width and height of the GRect on canvas
LEVEL = 3       # It controls the recursive depth of fractal
DELAY = 200     # The pause time in miliseconds

# This is the canvas for GRect
window = GWindow(width=1000, height=800)


def main():
	center_x = window.width/2
	center_y = window.height/2
	draw_rect(LEVEL, 300, center_x, center_y)


def draw_rect(level, width, center_x, center_y):
	if level == 0:
		return  # pass
	else:
		# 左上
		draw_rect(level-1, width/2, center_x-width/2, center_y-width/2)
		# 右下
		draw_rect(level - 1, width / 2, center_x + width / 2, center_y + width / 2)

		rect = GRect(width, width, x=center_x - width / 2, y=center_y - width / 2)
		rect.filled = True
		rect.fill_color = 'snow'
		window.add(rect)
		pause(DELAY)

		# 右上
		draw_rect(level-1, width/2, center_x+width/2, center_y-width/2)
		# 左下
		draw_rect(level-1, width/2, center_x-width/2, center_y+width/2)


if __name__ == '__main__':
	main()
