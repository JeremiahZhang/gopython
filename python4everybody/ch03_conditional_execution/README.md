# conditionals

- Boolean expressions

```
>>> 5 == 5
True
>>> 5 == 6
False

>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

comparison operators:

```
      x != y               # x is not equal to y
      x > y                # x is greater than y
      x < y                # x is less than y
      x >= y               # x is greater than or equal to y
      x <= y               # x is less than or equal to y
      x is y               # x is the same as y
      x is not y           # x is not the same as y
```

- Logical operation

```
and
or
not

>>> 17 and True
True
```

- conditional execution

1 

```
if x > 0 :
    print('x is positive')
```

2

```
if x < 0 :
    pass          # need to handle negative values!
```

- Alternative execution

```
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
```

- Chained conditionals

```
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')
```

- Nested conditionals

```
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```

简化:

```
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')
```

```
if 0 < x and x < 10:
    print('x is a positive single-digit number.')
```

- Catching exceptions using try and except

```
>>> prompt = "What...is the airspeed velocity of an unladen swallow?\n"
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10:
>>>
```

- Short-circuit evaluation of logical expressions

```
>>> x = 6
>>> y = 2
>>> x >= 2 and (x/y) > 2
True
>>> x = 1
>>> y = 0
>>> x >= 2 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>

>>> x = 1
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```
