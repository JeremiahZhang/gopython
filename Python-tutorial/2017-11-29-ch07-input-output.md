# input and output

```
In [1]: s = 'hello, world'

In [2]: str(s)
Out[2]: 'hello, world'

In [3]: repr(s)
Out[3]: "'hello, world'"

In [4]: str(1.0/7.0)
Out[4]: '0.142857142857'

In [5]: repr(1.0/7.0)
Out[5]: '0.14285714285714285'

In [6]: x = 10 * 3.25

In [7]: y = 200 * 200

In [8]: s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'

In [9]: print s
The value of x is 32.5, and y is 40000...

In [10]: # the repr() of a string adds string quotes and backslashs:

In [11]: hello = 'hello, world\n'

In [12]: hellos = repr(hello)

In [13]: print hellos
'hello, world\n'

In [14]: # The argument to repr() may be any Python object:

In [15]: repr((x, y, ('spam', 'eggs')))
Out[15]: "(32.5, 40000, ('spam', 'eggs'))"

In [16]: # Here are 2 ways to write a table of squares and cubes

In [17]: for x in range(1, 11):
    ...:     print repr(x).rjust(2), repr(x*x).rjust(3),
    ...:     # Note trailling comma on previous line
    ...:     print repr(x**3).rjust(4)
    ...:
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

In [18]: for x in range(1, 11):
    ...:     print '{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3)
    ...:
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

In [19]: print 1, 2, 3
1 2 3

In [20]: print 1,2,3
1 2 3

In [21]: x2 = 'I love Python Programming'

In [22]: x2.ljust(10)[:10]
Out[22]: 'I love Pyt'

In [23]: string1 = '12'

In [24]: string1.zfill(5)
Out[24]: '00012'

In [25]: '-3.14'.zfill(7)
Out[25]: '-003.14'

In [26]: '3.1415926'.zfill(5)
Out[26]: '3.1415926'

In [31]: help(str.rjust)
Help on method_descriptor:

rjust(...)
    S.rjust(width[, fillchar]) -> string

    Return S right-justified in a string of length width. Padding is
    done using the specified fill character (default is a space)


In [32]: # str.format()

In [33]: help(str.format)
Help on method_descriptor:

format(...)
    S.format(*args, **kwargs) -> string

    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').


In [34]: print '{0} and {1}'.format('spam', 'eggs')
spam and eggs

In [35]: print '{1} and {0}'.format('spam', 'eggs')
eggs and spam

In [36]: print '{1} and {1}'.format('spam', 'eggs')
eggs and eggs

In [37]: print 'This {food} is {adj}.'.format(
    ...:        food='spam', adj='absolutely horrible')
This spam is absolutely horrible.

In [38]: print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')
The story of Bill, Manfred, and Georg.

In [39]: # !s == str(), !r == repr()

In [40]: import math

In [41]: print 'The value of PI is approximately {}.'.format(math.pi)
The value of PI is approximately 3.14159265359.

In [42]: print 'The value of PI is approximately {!r}.'.format(math.pi)
The value of PI is approximately 3.141592653589793.

In [43]: # {0:.3f} or {:} ...

In [44]: print 'the value of PI is approximately {0:.3f}.'.format(math.pi)
the value of PI is approximately 3.142.

In [45]: # : used for number of the characters wide

In [46]: table = {'Sjored': 4127, 'Jack': 4098, 'Dcab': 7678}

In [47]: for name, phone in table.items():
    ...:     print '{0:10} ===> {1:10d}'.format(name, phone)
    ...:
Dcab       ===>       7678
Sjored     ===>       4127
Jack       ===>       4098

In [48]: # If you have a really long format string that you don't

In [49]: # want to split up, then you can do:

In [50]: print ('Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};' )
Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};

In [51]: print ('Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};' \)
  File "<ipython-input-51-a06c8b9278b6>", line 1
    print ('Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};' \)
                                                         ^
SyntaxError: unexpected character after line continuation character


In [52]: print ('Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};'
    ...:        'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjored: 4127;Dcab: 7678

In [53]: print 'Jack: {Jack:d}; Sjored: {Sjored:d}; Dcab: {Dcab:d}'.format(**table)
Jack: 4098; Sjored: 4127; Dcab: 7678
```

# open, read, write into file

```
>>> f = open('workfile', 'w')
>>> print f
<open file 'workfile', mode 'w' at 80a0960>
```

and so on.

2017-11-29