# factorial.py
#   A program to compute the factorial of a numbers
#   Illustrates for loop with an accumulator.

def main():
    n = eval(input("Please enter a whole number: "))

    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor

    print("The factorial of {0} is {1}.".format(n, fact))

main()
