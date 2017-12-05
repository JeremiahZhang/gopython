def main():
    file_name = input("What file are the numbers in? ")
    infile = open(file_name, "r")

    sum = 0.0
    count = 0

    line = infile.readline()

    print(line, end="")

    while line != "":
        sum += eval(line)
        count += 1

        line = infile.readline()

    print("The average of the numbers is {}".format(sum / count))

if __name__ == '__main__':
    main()
