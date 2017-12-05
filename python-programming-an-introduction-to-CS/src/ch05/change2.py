# change2.py
#   A program to calculate the value of some change in dollars.
#   This version represents the total cash in cents.

def main():
    print("Change Counter\n")

    print("Please enter the count of each coin type.")

    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("The tatal value of your change is ${0}.{1:0>2}"
          .format(total//100, total%100))

if __name__ == '__main__':
    main()
