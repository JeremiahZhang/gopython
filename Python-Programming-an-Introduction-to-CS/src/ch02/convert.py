# -*- coding: utf-8 -*-

# convert.py
#   a program to convert Celsius temperatures to Fahrenheit
# by Jeremy Anifacc

def main():
    print("This is a program to convert ")
    print("Celsius temperature to Fahrenheit.")

    for i in range(5):
        celsius = float(input("What is the Cesisus temperature? Enter a number _> "))
        fahrenheit = 9.00 / 5.00  * celsius + 32.00
        print("The temperature is {0:.2f} degrees Fahrenheit.".format(fahrenheit))

main()
