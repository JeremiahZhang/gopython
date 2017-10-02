#!/usr/bin/env python3

# distance_convert.py
#   A program to convert distances measured in kilometers
#   to miles.
#   1 km ~= 0.62 miles.

def main():
    print("This is a program to convert distances measured in kilometers to miles.")

    # input
    kilometers = eval(input("Please input a distance measured in kilometers: _>"))
    # process
    miles = 0.62 * kilometers
    # output
    print("The miles: {}".format(miles))

main()
