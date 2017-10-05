# month.py
#   A program to print the abbreviation of a moth, given its number

def main():
    # The variable months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = eval(input("Enter a month number (1-12): "))

    # Computer starting position of month n in months
    pos = (n - 1) * 3

    # Grab the appropriate slice from months
    month_abbrev = months[pos: pos+3]

    # Print the result
    print("The month abbreviation is {}.".format(month_abbrev))

if __name__ == '__main__':
    main()
