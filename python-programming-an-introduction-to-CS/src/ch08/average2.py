def main():
    sum = 0.0
    count = 0.0

    moredata = "yes"

    while moredata[0] == "y":
        x = eval(input("Enter a number _> "))
        sum += x
        count += 1
        moredata = input("Do you have more numbers (yes or no)? ")

    print("\nThe average of the numbers is {}".format(sum / count))

if __name__ == '__main__':
    main()
