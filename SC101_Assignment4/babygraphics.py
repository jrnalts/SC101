"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    grid_width = width - GRAPH_MARGIN_SIZE*2        # 圖表寬
    start = GRAPH_MARGIN_SIZE                       # 起始點
    equal_part = grid_width / len(YEARS)-2          # 等分
    x_coordinate = start + equal_part * year_index  # 取得X座標
    return x_coordinate


def get_y_coordinate(height, rank_index):
    grid_height = height - GRAPH_MARGIN_SIZE * 2    # 圖表高
    start = GRAPH_MARGIN_SIZE                       # 起始點
    equal_part = grid_height / 1000                 # 等分
    y_coordinate = start + equal_part * rank_index  # 取得Y座標
    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    m = GRAPH_MARGIN_SIZE
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    canvas.create_line(m, m, width-m, m)
    canvas.create_line(m, height-m, width-m, height-m)

    for i in range(len(YEARS)):
        x = get_x_coordinate(width, i)
        canvas.create_line(x, 0, x, height)

        # 年份的 Y座標一律是 height-m
        canvas.create_text(x+TEXT_DX, height-m, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    for name in lookup_names:
        if name in name_data:
            points = []
            # 名字排名在 1000 名之外
            years = list(int(key) for key in name_data[name])
            out_of_name_data = list(set(YEARS) - set(years))
            for year in sorted(out_of_name_data):
                x = get_x_coordinate(width, YEARS.index(int(year)))
                y = height - GRAPH_MARGIN_SIZE
                rank = '*'
                points.append((x, y, rank))

            # 取得該名字的年份&排名
            for year, rank in name_data[name].items():
                if int(rank) < 1000:
                    x = get_x_coordinate(width, YEARS.index(int(year)))
                    y = get_y_coordinate(height, int(rank))
                points.append((x, y, rank))

            line_color = COLORS[lookup_names.index(name) % len(COLORS)]  # 設定線條顏色
            for p in sorted(points):
                index = points.index(p)
                if index < len(points)-1:
                    np = points[index+1]
                    canvas.create_line(p[0], p[1], np[0], np[1],
                                       width=LINE_WIDTH,
                                       fill=line_color)
                    canvas.create_text(p[0]+TEXT_DX, p[1],
                                       text=f'{name} {p[2]}',
                                       anchor=tkinter.SW)

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
