def main():
    file_name = input("What file are the numbers in? _> ")
    infile = open(file_name, "r")

    sum = 0.0
    count = 0

    line = infile.readline()

    while line != "":
        # update sum and count for values in line
        for x_str in line.split(","):
            sum += eval(x_str)
            count += 1

        line = infile.readline()

    print("\nThe average of the numbers is {}".format(sum / count))

if __name__ == '__main__':
    main()
