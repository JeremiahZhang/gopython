# maxn.py

def main():
    print("This program is to find the maximum of a series of numbers.")

    n = eval(input("How many numbers are there? "))

    max = eval(input("Enter a number _> "))

    for i in range(n-1):
        x = eval(input("Enter a numer _> "))
        if x > max:
            max = x

    print("The largest value is:{}".format(max))

if __name__ == '__main__':
    main()
