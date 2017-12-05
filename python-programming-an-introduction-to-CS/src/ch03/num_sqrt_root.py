# num_sqrt_root.py
#   A program implements Newton's method to guess the
#   square root of x which is inputed by the usr.

import math

def main():
    print("Please enter the number x you want to get the square root of.")
    print("Please also enter n which is the number of times to imporove the guess.")
    print()

    x, n = eval(input("Please enter x, n (seperated by a commna): "))
    guess = x / 2

    for i in range(n):
        guess = (guess + x / guess) / 2

    true_value = math.sqrt(x)

    accuracy = (1 - abs(true_value - guess) / true_value) * 100

    print("The final guess is {}.".format(guess))
    print("The guess accuracy of {} times is {}%.".format(n, accuracy))

main()
