# Strings

## A string is a sequence

```
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
```

## Getting the length of a string using `len`

```
>>> length = len(fruit)
>>> last = fruit[lenght]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lenght' is not defined
>>> last = fruit[length]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

>>> last = fruit[length-1]
>>> print(last)
a
```

## Traversal through a string with a loop

```
>>> index = 0
>>> while index < len(fruit):
...     letter = fruit[index]
...     print(letter)
...     index += 1
...
b
a
n
a
n
a

>>> for char in fruit:
...     print(char)
...
b
a
n
a
n
a
```

## String slices

```
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> print(s[6:])
Python
>>> print(len(s))
12

>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[3:3]
''

>>> fruit[:]
'banana'
```

## Strings are immutable

```
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

```
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
```

## Looping and counting

```
def loop_count():
    word = 'banana'
    count = 0
    for letter in word.lower():
        if letter == 'a':
            count += 1

    print('Count of a:', count)
```

```
def count(word, letter):
    total = 0
    for i in word.lower():
        if i == letter:
            total += 1

    return total

def main():
    word = 'I LOVE PYTHON'
    letter = 'o'
    total = count(word, letter)
    print('count of {0} is {1}.'.format(letter, total))

if __name__ == '__main__':
    main()
```

## The `in` operator

```
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
>>> 'na' in 'banana'
True
>>> 'an' in 'bana'
True
>>>
```

## String comparison

```
def main():
    word = input('Enter a word: ')
    word = word.lower()
    if word == 'banana':
        print('All right, bananas.')
    elif word < 'banana':
        print('You word, ' + word + ', comes before banana.')
    else:
        print('You word, ' + word + ', comes after banana.')

if __name__ == '__main__':
    main()
```

## string methods

```
>>> stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
>>> help(str.lstrip)
Help on method_descriptor:

lstrip(...)
    S.lstrip([chars]) -> str

    Return a copy of the string S with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead.
```

```
>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA

>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1
>>> word.find('na')
2
>>> word.find('na', 3)
4

>>> line = '  Here we go  '
>>> line.strip()
'Here we go'

>>> line = 'Have a nice day'
>>> line.startswith('Have')
True
>>> line.startswith('h')
False

>>> line = 'Have a nice day'
>>> line.startswith('h')
False
>>> line.lower()
'have a nice day'
>>> line.lower().startswith('h')
True
```

## Parsing strings

```
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ',atpos)
>>> print(sppos)
31
>>> host = data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>>
```

## Format operator

```
>>> camels = 42
>>> '%d' % camels
'42'

>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'

>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'

>>> '%d %d %d' % (1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string

>>> '%d' % 'dollars'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %d format: a number is required, not str
>>>
```

## Debugging

```
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Code: http://www.py4e.com/code3/copytildone2.py
```

问题:

```
> hello there
hello there
> # don't print this
> print this!
print this!
>
Traceback (most recent call last):
  File "copytildone.py", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
```

解决:

```
if line.startswith('#'):
```

or

```
if len(line) > 0 and line[0] == '#':
```
