import sys
sys.path.append('..')

from ch04.graphics import *
from ch11.dieview2 import DieView
from ch10.button import Button

class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")

        banner = Text(Point(300, 30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.msg = Text(Point(300, 380), "Welcome to the dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.create_dice(Point(300, 100), 75)

        self.buttons = []
        self.add_dice_button(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300,230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300,280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)

        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def create_dice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []

        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)

    def add_dice_button(self, center, width, height):
        center.move(-3*width, 0)

        for i in range(1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def set_money(self, amt):
        self.money.setText("${0}".format(amt))

    def show_result(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)

        self.msg.setText(text)

    def set_dice(self, values):
        for i in range(5):
            self.dice[i].set_value(values[i])

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.get_label() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an activate button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.get_label()

    def want_to_play(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def chose_dice(self):
        choices = []
        while True:
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4",
                             "Die 5", "Roll Dice", "Score"])

            if b[0] == "D":
                i = eval(b[4]) - 1
                if i in choices:
                    self.dice[i].set_color("black")
                else:
                    choices.append(i)
                    self.dice[i].set_color("gray")
            else:
                for d in self.dice:
                    d.set_color("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices

    def close(self):
        self.win.close()
