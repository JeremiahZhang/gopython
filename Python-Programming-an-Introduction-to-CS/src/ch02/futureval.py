#!/usr/bin/env python3

# futureval.py
#   A program to compute the value of an investment
#   carried 10 years into future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal, apr = eval(input("Please enter principal & rate, seperated by comma: "))

    principal = principal * (1 + apr) ** 10

    print("The value in 10 years is: {}".format(principal))

main()
