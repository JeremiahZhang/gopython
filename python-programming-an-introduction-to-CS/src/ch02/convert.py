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

def main2():

    celsius = [x for x in range(0, 101, 10)]
    fahrenheit = []

    for cel_temp in celsius:
        fah_temp = 9.00 / 5.00 * cel_temp + 32.00
        fahrenheit.append(fah_temp)

    print(celsius)
    print(fahrenheit)

def main3():
    print("This is a program to convert ")
    print("Fahrenheit temperature to Celsius.")

    # input
    fahrenheit = eval(input("What is the Fahrenheit temperature? Enter a number:_>"))
    # process
    celsius = (fahrenheit - 32) * 5.00 / 9.00
    # output
    print("The temperature is {0:.5f} degrees Celsius.".format(celsius))
# main()
# main2()
main3()
