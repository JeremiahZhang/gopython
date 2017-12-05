# cal_area.py
#   Program to calculate the volume and surface area of
#   a sphere from its radius, given as input.

import math

def main():

    radius = eval(input("Please enter the radius of the sphere: "))

    volume = 4 / 3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    print("The volume and area of the sphere are {0}, {1}".format(volume, area))

main()
