# -*- coding: utf-8 -*-

""" 

1. python keywords and example
2. python data type
3. string escape sequences
4. string formats
5. operators
6. reading code

"""

# 1 Look the main keywords using python

# import keyword # keyword module
# print keyword.kwlist

"""
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 
'while', 'with', 'yield']

all 31 keywords

"""

## and, not, or 

print (True and False)
print (True or False)
print (not True)

## as

"""

as is used to create an alias while importing a module.
It means giving a different name (user-defined) to 
a module while importing it.

import x as y
with x as y: pass

"""

import math as myAlias
print myAlias.cos(myAlias.pi)

## assert

""" 
assert is used for debugging purpose.

while programming, sometimes we wish to know the internal state
or chceck if our assumptions are true. assert helps us to do
this and find bugs more conveniently. 

assert is followed by a condition.

If the condition is true, nothing happens. But if the condition is false, 
AssertionError is raised. For example:
"""

# a = 4
# assert a > 5

"""
Traceback (most recent call last):
  File "ex37.py", line 66, in <module>
    assert a > 5
AssertionError
"""

## break, continue

"""
**break** and **continue** are used inside 
**for** and **while** loops to alter their normal behavior.

**break** will end the smallest loop it is in and control 
flows to the statement immediately below the loop. 

**continue** causes to end the current iteration of 
the loop, but not the whole loop.
"""

for i in range(1, 7):
    if i == 3:
        break
    print(i)

for i in range(1, 7):
    if i == 3:
        continue
    print(i)

# while True: break
# while True: continue

## class

"""
class is used to define a new user-defined class in Python.
"""

# clsss person(object)

## def

"""define a function"""

# def x(): pass

## del

"""
del is used to delete the reference to an object. 
Everything is object in Python. 
We can delete a variable reference using del
"""

# del X[Y] # del from a dictionary

a = 5
b = 5

del a

a = ['x', 'y', 'z']
del a[1]
print a

## if else elif
"""
if, else, elif are used for 
conditional branching or decision making.
"""

def if_example(a):
    if a == 1:
        print "One"
    elif a == 2:
        print "Two"
    else:
        print "something else"

if_example(2)
if_example(4)
if_example(1)

## except, raise, try

"""
except, raise, try are used with exceptions in Python.

IOError
ValueError
ZeroDivisionError
ImportError
NameError
TypeError 
etc.

try...except blocks are used to catch exceptions in Python
"""

def reciprocal(num):
    try:
        r = 1.0/num
    except:
        print "excetions caught"
        return
    return r

print(reciprocal(10))

print(reciprocal(0))

# num = 0

# if num == 0:
#     raise ZeroDivisionError('Cannot divide')

## finally

"""
finally is used with try…except block to 
close up resources or file streams.
"""

# try:
#     Try-block
# except exception1:
#     Exception1-block
# except exception2:
#     Exception2-block
# else:
#     Else-block
# finally:
#     Finally-block

## for used for looping

names = ['Jean', 'Monica', 'Jerry']
for i in names:
    print "Hello, " + i

## from import

import sys
# from math import cos

## global

"""
global is used to declare that a variable inside 
the function is global (outside the function).
"""

global_var = 10

def read_1():
    print global_var

def write_1():
    global global_var
    global_var = 7

def write_2():
    global_var = 5

read_1()

write_1()
read_1()

write_2() # local can't write into global
read_1()

## in

a = [i for i in range(1, 6)]
if 5 in a:
    print "Yes"

print (10 in a)

for i in 'hello':
    print i

## is 

""" 
*is* is used in Python for testing object identity. 
"""
print(1 is 1)
print("*" * 10)

"""
We know that there is only one instance of True, 
False and None in Python, so they are identical.
"""

print([] == [])
print([] is [])
print({} == {})
print({} is {})

print("*" * 10)
""" list and dict are mutalbe
but string and tuple are immutable
"""

print(" " == " ")
print(" " is " ")
print(() == ())
print(() is ())

print("*" * 10)

## lambda

"""
lambda is used to create an anonymous function 
(function with no name). It is an inline function 
that does not contain a return statement. 
It consists of an expression that is 
evaluated and returned. 
"""
a = lambda x: x*2
for i in range(1, 6):
    print a(i)

## pass

"""
pass is a null statement in Python. Nothing happens 
when it is executed. It is used as a placeholder.

先占着坑
以后来填
如下:
w未来要写这个function, 就直接写入
"""

def func_1(args):
    pass

class example:
    pass

## return

"""
return statement is used inside a function to 
exit it and return a value.
"""

def func_return():
    a = 10
    return a

def no_return():
    a = 10

print func_return()
print no_return() # None

## while loop

i = 5
while i:
    print i
    i += -1

## with

"""
**with** statement is used to wrap the execution of 
a block of code within methods defined by the 
context manager.
"""

# with open('example.txt', 'r') as my_file:
#     my_file.read()

## yield

"""
yield is used inside a function like a return 
statement. But yield returns a generator.
Generator is an iterator that generates one item 
at a time. A large list of value will take up 
a lot of memory. Generators are useful in this 
situation as it generates only one value 
at a time instead of storing all the values 
in memory. 
"""
print("x"*10)
g = (2**x for x in range(10))
print(next(g))
print(next(g))
print(next(g))

def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print i