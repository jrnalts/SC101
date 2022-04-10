"""
File: my_drawing.py
Name: 
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow()
    # face = GOval(200, 200, x=100, y=100)
    # window.add(face)
    #
    # l_eye = GOval(25, 25, x=150, y=150)
    # window.add(l_eye)
    # r_eye = GOval(25, 25, x=200, y=150)
    # window.add(r_eye)
    # nose = GOval(25, 25, x=175, y=175)
    # paint(nose, 'red')
    # window.add(nose)
    #
    # mouth = GRect(80, 50, x=150, y=220)
    # paint(mouth, 'blue')
    # window.add(mouth)

    label = GLabel("Hello World!")
    label.font = '-40'
    window.add(label, x=200, y=200)


def paint(obj, color):
    obj.filled = True
    obj.fill_color = color


if __name__ == '__main__':
    main()
