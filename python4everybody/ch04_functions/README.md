# Functions

```
>>> type(32)
<class 'int'>
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('hello world')
11
>>>
```

```
>>> int(32)
32
>>> int('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
```

```
>>> int(3.99999)
3
>>> int(-2.3)
-2
```

```
>>> float(32)
32.0
>>> float('3.14159')
3.14159
```

```
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
```

## random number

```
>>> import random
>>> for i in range(10)
  File "<stdin>", line 1
    for i in range(10)
                     ^
SyntaxError: invalid syntax
>>> for i in range(10):
...     x = random.random()
...     print(x)
...
0.7902628190974068
0.07016905248471739
0.5792428780259563
0.8926899914678336
0.9090663201506247
0.6717350629220712
0.6353684409293695
0.3761610733514441
0.8963068116516231
0.6601149165917466
>>>
```

```
>>> random.randint(5,10)
6
>>> random.randint(5,10)
6
>>> random.randint(5,10)
10
>>> random.randint(5,10)
7
>>>
```

`choice`:

```
>>> t = [1, 2, 3]
>>> random.choice(t)
1
>>> random.choice(t)
3
>>>
```

# math functions

```
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865476
```

## adding new functions

```
>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.")
...     print('I sleep all night and I work all day.')
...
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```

## flow of execution

## parameters and arguments

```
>>> def print_twice(bruce):
...     print(bruce)
...     print(bruce)
...
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
```

```
>>> print_twice('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam
```

## Fruitful functions and void functions

```
>>> golden = (math.sqrt(5) + 1) / 2
>>> math.sqrt(5)
2.23606797749979
>>> golden
1.618033988749895
```

```
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
```
