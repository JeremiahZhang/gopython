# numeric_name.py
#   A program to calculate the numeric value of a single name
#   provided as input.
#   Example: Zelle: 26+5+12+12+5 = 60
#            a is 1, b is 2, ..., z is 26.
"""
This program is to calculates the numeric value
single name.
Please enter a single name: Zelle
The numeric value of the name Zelle is 60.
"""

def main():
    print("This program is to calculate the numeric value")
    print("single name.")

    # Input
    name = input("Please enter a single name: ")
    name_lower = name.lower()
    name_value = 0

    # Processing
    for i in range(len(name_lower)):
        letter_value = ord(name_lower[i]) - 96
        name_value += letter_value

    # Output
    print("The numeric value of the name {0} is {1}."
          .format(name, name_value))

if __name__ == '__main__':
    main()
