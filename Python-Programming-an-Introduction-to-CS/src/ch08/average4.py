def main():
    sum = 0.0
    count = 0
    x_str = input("Enter a number (<Enter> to quit) _> ")

    while x_str != "":
        x = eval(x_str)
        sum += x
        count += 1
        x_str = input("ENter a number (<Enter> to quit) _> ")

    print("\nThe average of the number is {}".format(sum / count))

if __name__ == '__main__':
    main()
