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

# Loop
x = 0.5
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)

for i in [0, 1, 2, 4, 3]:
    print(i)

for odd in [1, 3, 5, 7, 9]:
    print(odd ** 2)

print("Range(10)")
print(list(range(10)))
