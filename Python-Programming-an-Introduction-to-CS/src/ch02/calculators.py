# calulators.py
#   A program allows the user to type a mathmatical expresion,
#   and then print the value of the expression.

def main():
    print("This is a program to allow users to type a math ")
    print("expression, and then print the value of the expr!")
    print("plus: 1 + 1")
    print("minus: 1 - 1")
    print("multiply: 1 * 2")
    print("division: 1 / 3")
    print("exponetn: 2 ** 2")
    print("Mixture.")
    print("If you want to exit, please input 111")

    for i in range(100):
        x = eval(input("Please input a math expression _> "))

        if x == 111:
            break

        print("The value of the expression is {}".format(x))

main()
