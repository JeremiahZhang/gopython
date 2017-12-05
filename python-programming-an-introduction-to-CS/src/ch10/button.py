import sys
sys.path.append("..")

from ch04.graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it.
    """

    def __init__(self, win, center, width, height, label):
        """Creates a rectangle button, eg:
        qb = Button(my_win, center_point, width, height, "Quit")
        """

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h

        # Rectangle
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        # Label in Rectangle
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, p):
        """Returns true if button active and p is inside."""
        # print(type(p))
        # print(1)
        p_x = p.getX()
        p_y = p.getY()
        return (self.active and
                self.xmin <= p_x <= self.xmax and
                self.ymin <= p_y <= self.ymax)

    def get_label(self):
        """Returns the label string of this button."""
        return self.label.getText()
