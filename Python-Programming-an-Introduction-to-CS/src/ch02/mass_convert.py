# mass_convert.py
#   A program to convert mass measured in kilogram to Pound

def main():
    print("This is a program to convert mass measured")
    print("in kilogram to pound.")

    # input
    kilogram = eval(input("Enter the mass measured in kilogram:_> "))
    # process
    pound = 2.20462 * kilogram
    # output
    print("The pound of the mass is: {} puounds".format(pound))

main()
