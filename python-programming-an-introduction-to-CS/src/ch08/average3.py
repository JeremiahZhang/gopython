def main():
    sum = 0.0
    count = 0.0

    x = eval(input("Enter a number (negative to quit) _> "))

    while x >= 0:
        sum += x
        count += 1
        x = eval(input("Enter a number (negative to quit) _> "))

    print("\nThe average of the numbers is {}".format(sum / count))

if __name__ == '__main__':
    main()
