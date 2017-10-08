# quadratic6.py

import math

def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a, b, c = input("Please enter the coefficients (a, b, c): ")
        disc_root = math.sqrt(b ** 2 - 4 * a * c)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)

        print("\nThe solutions are: {}, {}".format(root1, root2))

    except ValueError as excObj:
        print(str(excObj))
        if str(excObj) == "math domain error":
            print("No real roots!")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError :
        print("\nYou did not enter three number!")
    except TypeError:
        print("\nYour inputs were not all numbers!")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")

if __name__ == '__main__':
    main()
