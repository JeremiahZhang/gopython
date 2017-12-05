def main():
    print("This program is to calculate the average of input numbers.")

    n = eval(input("How many numbers do you have? "))

    sum = 0.0

    for i in range(n):
        x = eval(input("Enter a number _> "))
        sum += x

    print("\nThe average of the number is {}".format(sum / n))

if __name__ == '__main__':
    main()
