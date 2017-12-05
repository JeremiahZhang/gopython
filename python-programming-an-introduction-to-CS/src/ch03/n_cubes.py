# n_cubes.py
#   A program to find the sum of the cubes of the first n
#   natural numbers, where the value of n is provided by
#   the usr.

def main():
    print("Please enter the number n: ")

    n = eval(input("Enter here: "))

    sum = 0

    for i in range(1, n+1):
        sum += i ** 3

    print("The sum is {}.".format(sum))

main()
