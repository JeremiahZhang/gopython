# point_dist.py
#   A program to calculate the distance of 2 point in 2D.

import math

def main():
    print("Please enter the coordinates of two points.")

    print("Please enter the 1st point: x1, y1")
    x1, y1 = eval(input("Enter here _> "))

    print("Please enter the 2nd point: x2, y2")
    x2, y2 = eval(input("Enter here _> "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("The distance between the two points is {}.".format(distance))

main()
