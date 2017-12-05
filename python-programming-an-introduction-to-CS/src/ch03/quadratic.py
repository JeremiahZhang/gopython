# quadratic.py
#   A program that computes the real roots of a quadratic equation.
#   Illustrates use of the math of library.
#   Note: this program crashes if the equation has no real roots.

# Makes the math library available
import math
import sys

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    x = b * b - 4 * a * c

    if x >= 0:
        disc_root = math.sqrt(x)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print()
        print("The solutions are: ({0} , {1})".format(root1, root2))
    else:
        sys.exit("Please enter other coefficients.")

main()
