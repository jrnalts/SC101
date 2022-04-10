"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect, GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmousedragged, onmouseclicked

# This constant controls the size of the GRect
SIZE = 10
COLOR = 'black'


# Global Variable
window = GWindow()
mouse = GOval(SIZE, SIZE)


def main():
	onmousemoved(listener)
	onmouseclicked(draw)
	onmousedragged(draw)


def listener(event):
	mouse.x = event.x - mouse.width/2
	mouse.y = event.y - mouse.height/2
	filling_color(mouse)
	window.add(mouse)


def draw(e):
	point = GOval(SIZE, SIZE, x=e.x-SIZE/2, y=e.y-SIZE/2)
	filling_color(point)
	window.add(point)


def filling_color(obj):
	obj.filled = True
	obj.color = COLOR
	obj.fill_color = COLOR
	return obj


if __name__ == '__main__':
	main()
