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

# exercise 5
def main2():
    print("This program calculates the future value")
    print("of an investment, that the year is defined by the user")

    principal, apr = eval(input("Please enter principal and rate, seperated by comma: "))
    num_year = eval(input("Please input the year you want to invest: "))

    principal = principal * (1 + apr) ** num_year

    print("The value in {0} years is: {1}.".format(num_year, principal))

main2()
