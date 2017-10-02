# pizza_price.py
#   A program to calculate the cost per square inch of a circular
#   pizza, given its diameter and price.

import math

def main():

    diameter, price = eval(input("Enter the diameter(inch), price of your pizza: "))

    cost = 4 * price / (math.pi * diameter ** 2)

    print()
    print("The cost per square inch is: {}".format(cost))

main()
