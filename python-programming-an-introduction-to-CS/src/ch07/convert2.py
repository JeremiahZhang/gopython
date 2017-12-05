# convert2.py

def main():
    celsius = eval(input("What's the Celsius temperature?"))
    fahrenheit = 9/5 * celsius + 32

    print("The temperature is {} degrees in Fahrenheit.".format(fahrenheit))

    # Print warnings
    if fahrenheit > 90:
        print("It's relly hot out there. Be carefully.")
    if fahrenheit < 30:
        print("Bahla.... Be sure to dress warmly!")

if __name__ == '__main__':
    main()
