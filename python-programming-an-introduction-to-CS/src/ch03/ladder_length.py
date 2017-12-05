# ladder_lenght.py
#   A program to determine the lenght of a ladder required
#   to reach a given height when leaned against a house.
#   The height and angle of the ladder are given as inputs.

import math

def main():
    print("Please enter the height, angle of the ladder.")
    print("Two numbers, seperated by a comma.")
    print("The angle is in degrees.")
    print()

    height, angle = eval(input("Enter the two numbers here: _> "))

    radians = math.pi / 180 * angle
    lenght = height / math.sin(radians)

    print("The lenght of the ladder is {}.".format(lenght))

main()
