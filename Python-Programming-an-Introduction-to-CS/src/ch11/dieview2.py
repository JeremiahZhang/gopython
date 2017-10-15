import sys
sys.path.append('..')

from ch04.graphics import *

class DieView:
    """DiewView is a widget that displays a graphical
    representation of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die."""

        # first define some standard values
        self.win = win
        self.background = "white"
        self.foreground = "black"
        self.psize = 0.1 * size # radius of each pip
        hsize = size / 2.0
        offset = 0.6 * hsize  # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circle for standard pip locations
        self.pips = [ self.__make_pip(cx-offset, cy-offset),
                     self.__make_pip(cx-offset, cy),
                     self.__make_pip(cx-offset, cy+offset),
                     self.__make_pip(cx, cy),
                     self.__make_pip(cx+offset, cy-offset),
                     self.__make_pip(cx+offset, cy),
                     self.__make_pip(cx+offset, cy+offset) ]

        # Create
        self.ontable = [ [], [3], [2, 4], [2, 3, 4],
                        [0, 2, 4, 6], [0, 2, 3, 4, 6],
                        [0, 1, 2, 4, 5, 6] ]

        self.set_value(1)

    def __make_pip(self, x, y):
        """Internal helper method to draw a pip at (x, y)"""

        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def set_value(self, value):
        """Set this die to display value."""

        self.value = value

        for pip in self.pips:
            pip.setFill(self.background)

        for i in self.ontable[value]:
            self.pips[i].setFill(self.foreground)

    def set_color(self, color):
        self.foreground = color
        self.set_value(self.value)
