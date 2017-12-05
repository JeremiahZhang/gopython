# ful_value.py
"""
This program calculates the future value of
n years.

Please enter your principal: 2000
Please enter the annualized interset rate: 0.1
Please enter the number of years of investment: 7
   Year     Value
--------------------
    0     $2000.00
    1     $2200.00
    2     $2420.00
    3     $2662.00
    4     $2928.20
    5     $3221.02
    6     $3543.12
    7     $3897.43
"""

def main():
    print("This program calculates the future value of")
    print("n years.")
    print()

    # Input
    principal = eval(input("Please enter your principal: "))
    apr = eval(input("Please enter the annualized interset rate: "))
    year = eval(input("Please enter the number of years of investment: "))

    print("{0:^10}{1:^10}".format("Year", "Value"))
    print("{0:^20}".format("-"*20))
    # Processing
    for i in range(0, year+1):
        if i == 0:
            principal = principal
        else:
            principal = principal * (1 + apr)

        print("{0:^10}${1:<10.2f}".format(i, principal))

if __name__ == '__main__':
    main()
