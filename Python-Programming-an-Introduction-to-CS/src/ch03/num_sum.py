# num_sum.py
#   A program to find the sum of the first n natural numbers, where
#   the value of n is provided by the user.

def main():
    print("Please enter the number n.")
    print("The number n is a whole number, n >= 0")

    n = eval(input("Enter: "))

    sum = 0

    for i in range(n+1):
        sum += i

    print("The sum of n is {}.".format(sum))

main()
