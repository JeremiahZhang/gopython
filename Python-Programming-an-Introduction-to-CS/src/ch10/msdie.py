# msdie.py
#   Class definition for n-sided die.

"""
>>> from msdie import MSDie
>>> die = MSDie()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'sides'
>>> die = MSDie(16)
>>> die.roll()
>>> die.get_value()
10
>>> die.get_value()
10
>>> die.roll()
>>> die.set_value(9)
>>> die.get_value()
9
"""

from random import randrange

class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

def main():
    die1 = MSDie(12)
    die1.set_value(8)
    print(die1.get_value())

if __name__ == '__main__':
    main()
