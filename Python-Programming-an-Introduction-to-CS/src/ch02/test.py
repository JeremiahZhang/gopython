#!/usr/bin/env python3

print("The answer is", end=" ")
print(3 + 4)

# x = eval(input("Enter a number: "))

x = 1
y = 2

sum, diff = x+y, x-y

print(sum, diff)

# exchange
print("Before exchange: x = {}, y = {}".format(x, y))
temp = x
x = y
y = temp

print("After exchange: x = {}, y = {}".format(x, y))

# The simple way

x, y = y, x

print("Using the simple way to exchange! \n")
print("x = {}, y = {}".format(x, y))
