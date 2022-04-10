"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 10

# Global Variable
window = GWindow()


def main():
	onmouseclicked(create_hole)


def create_hole(event):
	# hole = GOval(SIZE, SIZE, x=event.x, y=event.y)
	hole = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
	hole.filled = True
	window.add(hole)


if __name__ == '__main__':
	main()
