"""calc.py

A four function calculator using Python arithmetic.
Illustrates use of objects and lists to build a
simple GUI.
"""

import sys
sys.path.append("..")

from ch04.graphics import *
from ch10.button import Button

class Calculator:

    def __init__(self):
        # create the window for the calculator
        win = GraphWin("calculator")
        win.setCoords(0, 0, 6, 7)
        win.setBackground("slategray")

        self.win = win
        # Now create the widgets
        self.__create_buttons()
        self.__create_display()

    def __create_buttons(self):
        # Creat list of buttons
        # Start with all the standard sized buttons
        # b_specs gives center coords and label of buttons
        b_specs = [(2,1,'0'), (3,1,'.'),
                   (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                   (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                   (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C')]

        self.buttons = []
        for (cx, cy, label) in b_specs:
            self.buttons.append(Button(self.win,Point(cx,cy), .75, .75, label))
        # create the larget = buttons
        self.buttons.append(Button(self.win,Point(4.5,1), 1.75, .75, "="))
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __create_display(self):
        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill('white')
        bg.draw(self.win)

        text = Text(Point(3,6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        self.display = text

    def get_button(self):
        # Wait for a button to be clicked and returns the
        # label of the button that was clicked.
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.get_label() # method exit

    def process_button(self, key):
        # Update the display of the calculator for press of the key
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            # Backspace: slice off the last character
            self.display.setText(text[: -1])
        elif key == '=':
            try:
                result = eval(text)
            except:
                result = 'ERROR'
            self.display.setText(str(result))
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)

    def run(self):
        # Infinite 'event loop' to process button clicks
        while True:
            key = self.get_button()
            self.process_button(key)

if __name__ == '__main__':
    MyCalc = Calculator()
    MyCalc.run()
