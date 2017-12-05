# epact.py
#   A program to prompt the user for a 4 digit year and then
#   output the value of the epact.
#   It shows how to calculate the date of Easter
#   for any year in the modern calendar. 

def main():
    print("Please enter 4-digit year.")

    year = eval(input("Please enter here _> "))

    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    print("The value of the epact is {}.".format(epact))

main()
