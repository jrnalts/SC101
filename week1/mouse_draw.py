"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged, onmouseclicked

# This constant controls the size of the pen stroke
SIZE = 10

# Global Variable
window = GWindow()


def main():
	onmousedragged(listener)
	onmouseclicked(listener)


def listener(event):
	rect = GRect(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
	rect = filling_color(rect, event)
	window.add(rect)


def filling_color(obj, event):
	obj.filled = True
	if event.x <= (window.width / 2):
		color = 'red'
	elif event.x >= (window.width / 2):
		color = 'blue'
	obj.color = color
	obj.fill_color = color
	return obj


if __name__ == '__main__':
	main()
