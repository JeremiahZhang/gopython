# data structure

- More on lists

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
