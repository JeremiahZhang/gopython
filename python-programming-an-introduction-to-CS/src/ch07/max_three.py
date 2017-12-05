# max_three.py

def main():
    # Inputs
    x1, x2, x3 = eval(input("Please enter three values: "))

    # Processing
    max = (x1 + x2 + x3) / 3
    if x1 >= max:
        max = x1
    if x2 >= max:
        max = x2
    if x3 >= max:
        max = x3

    # Output
    print("The largest value is {}".format(max))

if __name__ == '__main__':
    main()
