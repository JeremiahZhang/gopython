# triangle_area.py
#   A program to calculate the area of a triangle given the
#   length of its three sides, a, b, c.

import math

def main():
    print("Please enter three sides of an triangle.")
    print("a, b, c")

    a, b, c = eval(input("Enter here, seperated by a comma _> "))

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area of the triangle is {}.".format(area))

main()
