def main():
    file_name = input("What file are the numbers in? ")
    infile = open(file_name, "r")

    sum = 0.0
    count = 0

    for line in infile:
        sum += eval(line)
        count = count + 1

    print("\nThe average of the numbers is {}".format(sum / count))

if __name__ == '__main__':
    main()
