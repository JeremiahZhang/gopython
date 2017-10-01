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

# exercise 6
def main3():
    print("This program calculates the total accumulation of")
    print("your investment, in the condition that you invest a certain fixed amount")
    print("money every years.")

    # The money you want to invest every year
    print("Please　enter principal of each year and rate, seperate by comma:")
    annual_principal, apr = eval(input())

    print("How many years do you want to invest?")
    num_year = eval(input("Please enter the number of years: "))

    total_accumulation = annual_principal * (1 + apr) * ((1 + apr)**num_year -1) / apr
    print("The total_accumulation of the investment: {}".format(total_accumulation))

# main()
# main2()
main3()
