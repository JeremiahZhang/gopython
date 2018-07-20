# Tuples

- Like lists
- Immutable
- Things not to do with Tuples
- A tale of two sequences
- Assignment
- With dictionaries
- Comparable
- Sorting lists of tuples
- sorted()
- List comprehension

## Pythonic module

```
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

# Code: http://www.py4e.com/code3/soft.py
```

## Assignment

```
In [1]: m = ['have', 'fun']

In [2]: x, y = m

In [3]: x
Out[3]: 'have'

In [4]: y
Out[4]: 'fun'

In [5]: (x1, y1) = m

In [6]: x1
Out[6]: 'have'

In [7]: y1
Out[7]: 'fun'

In [8]: x, y = y, x

In [9]: x
Out[9]: 'fun'

In [10]: y
Out[10]: 'have'

In [11]: addr = 'monty@python.org'

In [12]: addr
Out[12]: 'monty@python.org'

In [13]: add.split('@')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-0bcd07e86304> in <module>()
----> 1 add.split('@')

NameError: name 'add' is not defined

In [14]: addr.split('@')
Out[14]: ['monty', 'python.org']

In [15]: uname, domain = addr.split('@')

In [16]: uname
Out[16]: 'monty'

In [17]: domain
Out[17]: 'python.org'
```

## Dictionaries and tuples

```
In [18]: d = {'a':10, 'b':1, 'c':22}

In [19]: d.items()
Out[19]: dict_items([('a', 10), ('b', 1), ('c', 22)])

In [20]: t = list(d.items())

In [21]: t
Out[21]: [('a', 10), ('b', 1), ('c', 22)]

In [22]: print(t)
[('a', 10), ('b', 1), ('c', 22)]

In [23]: t.sort()

In [24]: t
Out[24]: [('a', 10), ('b', 1), ('c', 22)]
```

## Wow Method

```
In [25]: for (key, val) in list(d.items()):
    ...:     print(val, key)
    ...:
10 a
1 b
22 c

In [26]: d
Out[26]: {'a': 10, 'b': 1, 'c': 22}

In [27]: l = list()

In [28]: for key, val in d.items():
    ...:     l.append((val, key))
    ...:

In [29]: l
Out[29]: [(10, 'a'), (1, 'b'), (22, 'c')]

In [30]: l.sort(reverse=True)

In [31]: l
Out[31]: [(22, 'c'), (10, 'a'), (1, 'b')]
```

## Using tuples as keys in dictionaries

```
directory[last,first] = number

for last, first in directory:
    print(first, last, directory[last,first])
```

example:

```
In [32]: directory = dict()

In [33]: directory[jeremy, zhang] = 15066668888
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-33-9b6928f355cb> in <module>()
----> 1 directory[jeremy, zhang] = 15066668888

NameError: name 'jeremy' is not defined

In [34]: directory['jeremy', 'zhang'] = 15066668888

In [35]: for last, first in directory:
    ...:     print(first, last, directory[last, first])
    ...:
zhang jeremy 15066668888
```

## Debugging

- Reading
- Running
- Ruminating
- Retreating

## Summary

- Tuple syntax
- Immutability
- Comparability
- Sorting
- Tuples in assignment statements
- Sorting dictionaries by either key or value
