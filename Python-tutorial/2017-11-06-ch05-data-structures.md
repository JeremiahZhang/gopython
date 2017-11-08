# data structure

- More on lists

```
In [3]: help(list.append)
Help on method_descriptor:

append(...)
    L.append(object) -- append object to end


In [4]: a = [66.25, 123, 1, 3, -5]

In [5]: len(a)
Out[5]: 5

In [6]: a.append(-100)

In [7]: a
Out[7]: [66.25, 123, 1, 3, -5, -100]

In [8]: a[len(a):]
Out[8]: []

In [9]: help(list.extend)
Help on method_descriptor:

extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable


In [10]: b = [0, -2, -1]

In [11]: a.extend(b)

In [12]: a
Out[12]: [66.25, 123, 1, 3, -5, -100, 0, -2, -1]

In [13]: help(list.insert)
Help on method_descriptor:

insert(...)
    L.insert(index, object) -- insert object before index


In [14]: b.insert(0, 1)

In [15]: b
Out[15]: [1, 0, -2, -1]

In [16]: b.insert(len(b), -10)

In [17]: b
Out[17]: [1, 0, -2, -1, -10]

In [18]: help(list.remove)
Help on method_descriptor:

remove(...)
    L.remove(value) -- remove first occurrence of value.
    Raises ValueError if the value is not present.


In [19]: b.remove(0)

In [20]: b
Out[20]: [1, -2, -1, -10]

In [21]: b.remove(1)

In [22]: b
Out[22]: [-2, -1, -10]

In [23]: help(list.pop)
Help on method_descriptor:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.


In [24]: b
Out[24]: [-2, -1, -10]

In [25]: len(b)
Out[25]: 3

In [26]: b.pop(1) # remove -1 in list b and return the removed item
Out[26]: -1

In [27]: b
Out[27]: [-2, -10]

In [28]: b.pop() # default, remove the last item in list b, return the removed item
Out[28]: -10

In [29]: b
Out[29]: [-2]

In [30]: help(list.index)
Help on method_descriptor:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.


In [31]: a
Out[31]: [66.25, 123, 1, 3, -5, -100, 0, -2, -1]

In [32]: a.pop()
Out[32]: -1

In [33]: a.index(1)
Out[33]: 2

In [34]: a.pop()
Out[34]: -2

In [35]: a
Out[35]: [66.25, 123, 1, 3, -5, -100, 0]

In [36]: a.append(123)

In [37]: a
Out[37]: [66.25, 123, 1, 3, -5, -100, 0, 123]

In [38]: a.count(123)
Out[38]: 2

In [39]: a.count(66.25)
Out[39]: 1

In [40]: help(list.sort)
Help on method_descriptor:

sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

```

## more on lists

我们在Python 编译器中 使用`help(list)` 查看关于 `list` 的 help 文档.

`help(list.append)` 查看 list.method 的文档信息. 快捷方便.

```
In [1]: a = [1, 2, 3, -1, -4, -5]

In [2]: a
Out[2]: [1, 2, 3, -1, -4, -5]

In [3]: a.reverse()

In [4]: a
Out[4]: [-5, -4, -1, 3, 2, 1]

In [5]: a.sort()

In [6]: a
Out[6]: [-5, -4, -1, 1, 2, 3]
```

新知: list 的使用

- using list as stacks 堆栈
- 使用 list 排队
- Functional programming tools

```
In [9]: # using lists as stacks

In [10]: stack = [3, 4, 5]

In [11]: stack.append(6)

In [12]: stack.append(7)

In [13]: stack
Out[13]: [3, 4, 5, 6, 7]

In [14]: stack.pop()
Out[14]: 7

In [15]: stack.pop()
Out[15]: 6

In [16]: stack
Out[16]: [3, 4, 5]

In [17]: stack.pop()
Out[17]: 5

In [18]: stack
Out[18]: [3, 4]

In [19]: # using lists as queues

In [20]: from collections import deque

In [21]: queue = deque(["Eric", "John", "Michael"])

In [22]: queue.append("Terry")       # Terry arrives

In [23]: queue.append("Graham")      # Graham arrives

In [24]: queue
Out[24]: deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

In [25]: queue.popleft()            # The first to arrive now leaves
Out[25]: 'Eric'

In [26]: queue.popleft()            # the second to arrive now leaves
Out[26]: 'John'

In [27]: queue
Out[27]: deque(['Michael', 'Terry', 'Graham'])
```

新知:

## Functional programming tools

build-in functions `filter(), map(), reduce()` with `lists`

- `help(filter)` 新知

```
In [31]: def f(x): return x % 3 == 0 or x % 5 == 0

In [32]: filter(f, range(2, 25))
Out[32]: [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
```

上面的代码非常简洁. Pythonic 新知

- `help(map)`

```
In [34]: def cube(x): return x ** 3

In [35]: map(cube(x): range(1, 5))
  File "<ipython-input-35-466325d53d99>", line 1
    map(cube(x): range(1, 5))
               ^
SyntaxError: invalid syntax


In [36]: map(cube(x), range(1, 5))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-36-f951a477175a> in <module>()
----> 1 map(cube(x), range(1, 5))

NameError: name 'x' is not defined

In [37]: map(cube, range(1, 5))
Out[37]: [1, 8, 27, 64]

In [38]: def nope(): pass

In [39]: map(nope, range(1, 5))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-39-0d6b82f01e90> in <module>()
----> 1 map(nope, range(1, 5))

TypeError: nope() takes no arguments (1 given)

In [40]: def nope(x): pass

In [41]: map(nope, range(1, 5))
Out[41]: [None, None, None, None]

In [42]: nap(cube, range(1,3), range(3, 10))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-42-554412d43854> in <module>()
----> 1 nap(cube, range(1,3), range(3, 10))

NameError: name 'nap' is not defined

In [43]: map(cube, range(1,3), range(3, 10))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-43-bd6c139a662a> in <module>()
----> 1 map(cube, range(1,3), range(3, 10))

TypeError: cube() takes exactly 1 argument (2 given)

In [44]: help(map)


In [45]: map(rang(1, 3))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-45-e47dc18e3ff4> in <module>()
----> 1 map(rang(1, 3))

NameError: name 'rang' is not defined

In [46]: map(range(1, 3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-46-1c9b33bb6e2f> in <module>()
----> 1 map(range(1, 3))

TypeError: map() requires at least two args

In [47]: map(fun, range(1, 3))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-47-dbf011180104> in <module>()
----> 1 map(fun, range(1, 3))

NameError: name 'fun' is not defined

In [48]: seq = range(8)

In [49]: seq
Out[49]: [0, 1, 2, 3, 4, 5, 6, 7]

In [50]: def add(x, y): return x+y

In [51]: map(add, seq, seq)
Out[51]: [0, 2, 4, 6, 8, 10, 12, 14]
```

- `help(reduce)`

```
In [54]: help(reduce)

Help on built-in function reduce in module __builtin__:

reduce(...)
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.

In [55]: def add(x,y): return x+y

In [56]: reduce(add, range(1, 11)) # 1+2+3...+10
Out[56]: 55

In [57]: reduce(lambda x, y: x+y, range(1, 11))
Out[57]: 55

---

In [59]: def sum(seq):
    ...:     def add(x,y): return x+y
    ...:     return reduce(add, seq, 1)
    ...:

In [60]: sum(range(1, 11))
Out[60]: 56

In [61]: sum([])
Out[61]: 1

In [62]: a = range(1, 11)

In [63]: a
Out[63]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [64]: sum(a)
Out[64]: 56

```

> 莫用上面的方法, python 本来就用 `sum(list)` 函数供使用. 如下面.

```
In [1]: sum(range(1, 11))
Out[1]: 55
```

---

## List comprehensions

列表式推导. 简洁. Pythonic

新知: 一般用于建立 `list`. 常用场景.

1. 所建立的list中元素为其他序列中元素的某种计算结果.
2. list 中元素为 其他序列中 元素满足一定条件下的计算结果.

比如

```
In [1]: squares = []

In [2]: for x in range(10):
   ...:     squares.append(x**2)
   ...:     

In [3]: squares
Out[3]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

In [4]: a = [x**2 for x in range(10)]

In [5]: a
Out[5]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

In [6]: b = map(lambda x: x**2, range(10))

In [7]: b
Out[7]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

其中 列表推导 `a=[x**2 for x in range(10)]` 最简洁, 读者也容易理解.

新知: 我们可以看到, list comprehension 和 'for' 语句一起使用. 通常还会和`if`语句使用, 以及 `for, if` 合并使用.

```
In [8]: [(x, y) for x in [1,2,3] for y in [3, 1, 4] if x!=y]
Out[8]: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

In [9]: # It's equivalent to

In [10]: combs = []

In [11]: for x in [1,2,3]:
    ...:     for y in [3,1,4]:
    ...:         if x != y:
    ...:             combs.append((x, y))
    ...:             

In [12]: combs
Out[12]: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

上面, 请注意在`for, if`的顺序.

常用场景

```
In [13]: vec = [-4, -2, 0, 2, 4]

In [14]: # create a new list with the values doubled

In [15]: [x**2 for x in vec]
Out[15]: [16, 4, 0, 4, 16]

In [16]: # filter the list to exclude negative numbers

In [17]: [x for x in vec if x >=0]
Out[17]: [0, 2, 4]

In [18]: # apply a function to all the elements

In [19]: [abs(x) for x in vec]
Out[19]: [4, 2, 0, 2, 4]

In [20]: # call a method on each element

In [21]: freshfruit = ['  banana', '  loganberry', 'passion fruit  ']

In [22]: [weapon.strip() for weapon in freshfruit]
Out[22]: ['banana', 'loganberry', 'passion fruit']

In [23]: help(str.strip)


In [24]: # create a list of 2-tuple like (number, square)

In [25]: [(x, x**2) for x in range(6)]
Out[25]: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

In [26]: # the tuple must be parenthesized, otherwise an error is raised

In [27]: [x, x**2 for x in range(6)]
  File "<ipython-input-27-adb9f7a8642f>", line 1
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax


In [28]: # flatten a list using listcomp with two 'for'

In [29]: vec = [[1,2,3], [4,5,6], [7,8,9]]

In [30]: [num for elem in vec for num in elem]
Out[30]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

看,还可以内嵌复杂函数

```
In [31]: from math import pi

In [32]: [str(round(pi, i)) for i in range(1, 6)]
Out[32]: ['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

---

## nested 列表式推导

```
In [1]: matrix = [
   ...:     [1, 2, 3, 4],
   ...:     [5, 6, 7, 8],
   ...:     [9, 10, 11, 12],
   ...: ]

In [2]: matrix
Out[2]: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

In [3]: [[row[i] for row in matrix] for i in range(4)]
Out[3]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

In [4]: for row in matrix:
   ...:     print row,
   ...:
[1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]

In [5]: transposed = []

In [6]: for i in range(4):
   ...:     transposed.append([row[i] for row in matrix])
   ...:

In [7]: transposed
Out[7]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

In [8]: transposed = []

In [9]: for i in range(4):
   ...:     transposed_row = []
   ...:     for row in matrix:
   ...:         transposed_row.append(row[i])
   ...:

In [10]: for i in range(4):
    ...:     transposed_row = []
    ...:     for row in matrix:
    ...:         transposed_row.append(row[i])
    ...:     transposed.append(transposed_row)
    ...:

In [11]: transposed
Out[11]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

In [12]: help(zip)
Help on built-in function zip in module __builtin__:

zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.


In [13]: zip(*matrix)
Out[13]: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## `del` statement

新知： 善用

```
In [14]: a = [x for x in range(6)]

In [15]: a
Out[15]: [0, 1, 2, 3, 4, 5]

In [16]: del a[0]

In [17]: a
Out[17]: [1, 2, 3, 4, 5]

In [18]: len(a)
Out[18]: 5

In [19]: del a[2:4]

In [20]: a
Out[20]: [1, 2, 5]

In [21]: del a[:]

In [22]: a
Out[22]: []

In [23]: # del entrire variables

In [24]: del a

In [25]: a
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-25-60b725f10c9c> in <module>()
----> 1 a

NameError: name 'a' is not defined

---

In [26]: a = (1, 2)

In [27]: a
Out[27]: (1, 2)

In [28]: a[0]
Out[28]: 1

In [29]: del a[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-cc06cab42bbe> in <module>()
----> 1 del a[0]

TypeError: 'tuple' object doesn't support item deletion

In [30]: # tuple unmutable
```

## tuple

```
In [1]: t = 12345, 54321, 'Hello world!'

In [2]: t[0]
Out[2]: 12345

In [3]: t
Out[3]: (12345, 54321, 'Hello world!')

In [4]: u = t, (1, 2, 3, 4, 5)

In [5]: u
Out[5]: ((12345, 54321, 'Hello world!'), (1, 2, 3, 4, 5))

In [6]: # Tuples are immutable

In [7]: # but they can contain mutable objects:

In [8]: v = ([1, 2, 3], [3, 2, 1])

In [9]: v
Out[9]: ([1, 2, 3], [3, 2, 1])
```
