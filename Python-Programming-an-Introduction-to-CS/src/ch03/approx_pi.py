# approx_pi.py
#   A program to approximate the value of pi.

import math

def main():
    print("Please enter the number of term to sum, which approximates pi.")
    print()

    n = eval(input("Enter n: "))

    total_sum = 0

    for i in range(1, n+1):
        total_sum += (-1) ** (i + 1) * 4 / (2 * i - 1)

    error_rate = abs((math.pi - total_sum)) / math.pi * 100

    print("The approximation of pi is: {}".format(total_sum))
    print("The error rate is {} %".format(error_rate))

main()
