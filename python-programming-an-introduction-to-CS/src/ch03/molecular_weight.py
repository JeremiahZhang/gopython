# molecular_weight.py
#   A program that determines the molecular weight of a
#   hydrocarbon based on the number of hydrogen, carbon, and
#   oxygen atoms.

def main():
    print("Please input the moles of hydrogen, carbon, oxygen atoms.")
    print("Enter the number like this: a, b, c")
    print()

    hydrogen, carbon, oxygen = eval(input("Please enter here: "))
    molecular_weight = 1.0079 * hydrogen + 12.11 * carbon + 15.9994 * oxygen

    print("The molecular weight of a hydrocarbon is {} grams.".format(molecular_weight))

main()
