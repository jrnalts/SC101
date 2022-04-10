"""
File: my_drawing.py
Name: WALL·E
----------------------
"""

from campy.graphics.gobjects import GLine, GOval, GArc, GRect, GPolygon
from campy.graphics.gwindow import GWindow

# Global Variable
window = GWindow(width=800, height=533, title='WALL·E')
paint_yellow = '#fdc358'  # R:253, G:195, B:88
dark_paint_yellow = '#d87f07'  # R:216, G:127, B:7
dark_grey = '#4d4a4a'  # R:77, G:74, B:74


def main():
    """
    嘗試以 campy 繪圖致敬皮克斯動畫經典：瓦力
    原圖出處: https://zhihuimami.com/jianbihua/48606.html#images-1
    """
    right_hand()
    right_foot()
    body()
    head()
    left_hand()
    left_foot()


def head():
    neck()
    eye()


def neck():
    poly(paint_yellow, (419, 181), (447, 170), (469, 204), (439, 211))
    line(437, 173, 21, 34)
    poly(paint_yellow, (433, 118), (450, 116), (450, 138), (443, 139), (445, 146), (441, 147), (441, 160), (426, 167))
    oval(25, 16, 408, 163, color=paint_yellow)
    oval(20, 16, 420, 160, color=paint_yellow)
    oval(18, 20, 431, 155, color=paint_yellow)
    poly(paint_yellow, (409, 129), (430, 105), (443, 115), (430, 131), (431, 165), (409, 165))
    oval(25, 16, 393, 108, color=paint_yellow)
    oval(20, 16, 404, 105, color=paint_yellow)
    oval(18, 20, 417, 100, color=paint_yellow)


def eye():
    # eye
    arc(54, 58, 470, 70, 210, 230, color='grey')
    poly('grey', (406, 45), (367, 122), (447, 92))
    poly(paint_yellow, (410, 73), (420, 69), (436, 84), (412, 99), (407, 95))

    # socket
    arc(180, 240, 270, -13, 240, 130, color='white', frame='white')
    arc(180, 240, 271, -13, 240, 130)
    arc(180, 240, 304, 36, 60, 130)
    arc(180, 240, 413, -15, 170, 130, color='white', frame='white')
    arc(180, 240, 412, -15, 170, 130)
    arc(180, 240, 379, 34, 350, 130, color='white', frame='white')
    arc(180, 240, 379, 34, 350, 130)
    line(405, 45, -94, 30)
    line(413, 42, 94, 30)
    frameless_poly('white', (311, 0), (405, 0), (405, 44), (311, 74))
    frameless_poly('white', (507, 0), (413, 0), (413, 41), (507, 71))

    # eyeball
    oval(40, 40, 358, 64, color='grey')
    oval(40, 40, 422, 64, color='grey')
    oval(20, 20, 371, 74, color='black')
    oval(20, 20, 437, 74, color='black')
    oval(5, 5, 380, 78, color='white')
    oval(5, 5, 446, 78, color='white')


def body():
    poly(paint_yellow, (314, 204), (448, 226), (448, 400), (314, 370))
    poly(paint_yellow, (437, 183), (558, 199), (448, 226), (314, 204))
    poly('black', (456, 186), (512, 193), (440, 211), (388, 202))
    poly(paint_yellow, (448, 226), (558, 199), (558, 355), (448, 400))

    # Accessories
    poly('grey', (314, 204), (448, 226), (448, 288), (314, 261))
    poly(dark_grey, (314, 214), (448, 236), (448, 288), (314, 261))
    poly('grey', (334, 218), (428, 233), (428, 284), (334, 264))
    poly(dark_paint_yellow, (448, 252), (526, 227), (545, 230), (462, 257))
    poly(paint_yellow, (462, 257), (545, 230), (545, 262), (462, 292))
    poly('grey', (448, 252), (462, 257), (462, 292), (448, 288))


def right_hand():
    poly('grey', (274, 179), (292, 184), (273, 205), (254, 203))
    poly(paint_yellow, (253, 161), (264, 147), (283, 181), (281, 192), (261, 197))
    poly(dark_paint_yellow, (254, 203), (273, 205), (319, 280), (306, 282))
    poly(paint_yellow, (273, 205), (292, 184), (337, 252), (319, 280))
    poly('grey', (183, 93), (258, 122), (236, 175), (163, 149), (170, 122), (181, 126), (183, 121), (174, 118))
    poly('grey', (192, 107), (250, 132), (241, 154), (183, 132))
    poly('grey', (253, 131), (268, 138), (253, 165), (230, 150))


def left_hand():
    poly('grey', (377, 340), (372, 316), (394, 263), (413, 270), (391, 320), (393, 346))
    poly('grey', (430, 268), (451, 260), (455, 278), (433, 283))
    poly('grey', (407, 267), (430, 263), (438, 276), (432, 288), (402, 284))
    poly('grey', (430, 277), (451, 285), (423, 325), (423, 357), (404, 352), (399, 320))


def right_foot():
    poly('grey', (313, 279), (406, 391), (333, 431), (245, 396))
    arc(220, 290, 326, 278, 80, 120, color=dark_grey)
    oval(15, 20, 329, 377, color='grey')


def left_foot():
    poly('grey', (533, 297), (597, 302), (629, 455), (529, 488), (444, 462))
    arc(270, 400, 532, 319, 107, 85, color=dark_grey)
    oval(15, 20, 561, 342, color='grey')
    oval(15, 20, 541, 375, color='grey')
    oval(15, 20, 534, 425, color='grey')
    oval(30, 45, 562, 392, color='grey')
    oval(18, 24, 568, 401, color=dark_grey)


def line(x, y, px, py):
    obj = GLine(x, y, x+px, y+py)
    window.add(obj)


def rect(width, height, px, py, color='transparent'):
    obj = GRect(width, height)
    paint(obj, color, px, py)


def oval(width, height, px, py, color='transparent'):
    obj = GOval(width, height)
    paint(obj, color, px, py)


def arc(width, height, px, py, start, sweep, color='transparent', frame='transparent'):
    # 寬、高、X座標、Y座標、起始角、角變量
    obj = GArc(width, height, start, sweep)
    paint(obj, color, px, py, frame)


def poly(color, *args):
    obj = GPolygon()
    # 座標請按順時針方向設定
    for arg in args:
        obj.add_vertex(arg)
    paint(obj, color, 0, 0)


def frameless_poly(color, *args):
    obj = GPolygon()
    # 座標請按順時針方向設定
    for arg in args:
        obj.add_vertex(arg)
    paint(obj, color, 0, 0, frame=color)


def paint(obj, color, px, py, frame='transparent'):
    if color is not 'transparent':
        obj.filled = True
        obj.fill_color = color
    if frame is not 'transparent':
        obj.color = frame
    window.add(obj, x=px, y=py)


if __name__ == '__main__':
    main()
