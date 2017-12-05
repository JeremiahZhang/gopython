""" Roller.py
Graphics program to roll a pair of dice. Uses custon widgets
Button and DieView.
"""

import sys
sys.path.append('..')

from random import randrange

from ch04.graphics import *

from ch10.button import Button
from dieview2 import DieView

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)

    roll_button = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    roll_button.activate()
    quit_button = Button(win, Point(5, 1), 2, 1, "Quit")

    # Even loop
    pt = win.getMouse()
    # print(type(pt))
    # print(pt.getX())
    while not quit_button.clicked(pt):
        if roll_button.clicked(pt):
            value1 = randrange(1, 7)
            die1.set_value(value1)
            value2 = randrange(1, 7)
            die2.set_value(value2)
            quit_button.activate()

        pt = win.getMouse()

    # close up shop
    win.close()

if __name__ == '__main__':
    main()
