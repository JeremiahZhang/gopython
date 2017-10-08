# quadratic5.py

import math

def main():
    print("This program finds the real solution to a quadratic\n")

    try:
        a, b, c = input("Please enter the coefficients (a, b, c): ")
        disc_root = math.sqrt(b * b - 4 * a * c)

        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)

        print("\nThe solutions are: {0}, {1}".format(root1, root2))

    except ValueError:
        print("\nNo real roots")

if __name__ == '__main__':
    main()
