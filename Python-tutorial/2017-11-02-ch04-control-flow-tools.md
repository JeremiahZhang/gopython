# control flow

- `if` statement
- `for` statement
- `range()` function
- `break`, `continue`, statement, `else` Clauses on Loops
- `pass` statement
- Defining functions
- Coding style

## if

```
In [2]: x = int(raw_input("Please enter an integer: "))
Please enter an integer: 42

In [3]: if x < 0:
   ...:     x = 0
   ...:     print("Negative changed to zero")
   ...: elif x == 0:
   ...:     print("Zero")
   ...: elif x == 1:
   ...:     print("Single")
   ...: else:
   ...:     print("More")
   ...:
More
```

## for

```
In [4]: words = ['cat', 'window', 'defenestrate']

In [5]: for w in words:
   ...:     print w, len(w)
   ...:
cat 3
window 6
defenestrate 12

In [6]: for w in words[:]:
   ...:     if len(w) > 6:
   ...:         words.insert(0, w)
   ...:

In [7]: words
Out[7]: ['defenestrate', 'cat', 'window', 'defenestrate']
```

先 copy lists, 再在 loop 中修改会好些.

## range()

```
In [8]: range(10)
Out[8]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [9]: range(5, 10)
Out[9]: [5, 6, 7, 8, 9]

In [10]: for i in range(5):
    ...:     print(i)
    ...:
0
1
2
3
4

In [11]: range(-10, -100, -30)
Out[11]: [-10, -40, -70]

In [12]: help(range)
Help on built-in function range in module __builtin__:

range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

In [14]: a = ['Mary', 'had', 'a', 'little', 'lamb']

In [15]: for i in range(len(a)):
    ...:     print i, a[i]
    ...:
0 Mary
1 had
2 a
3 little
4 lamb
```

[enumerate](https://docs.python.org/2.7/library/functions.html#enumerate) 更快捷.

```
In [17]: seasons = ['spring', 'summer', 'fall', 'winter']

In [18]: list(enumerate(seasons))
Out[18]: [(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]

In [19]: list(enumerate(seasons, start=1))
Out[19]: [(1, 'spring'), (2, 'summer'), (3, 'fall'), (4, 'winter')]

In [16]: help(enumerate)
Help on class enumerate in module __builtin__:

class enumerate(object)
 |  enumerate(iterable[, start]) -> iterator for index, value of iterable
 |
 |  Return an enumerate object.  iterable must be another object that supports
 |  iteration.  The enumerate object yields pairs containing a count (from
 |  start, which defaults to zero) and a value yielded by the iterable argument.
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |
 |  Methods defined here:
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |
 |  next(...)
 |      x.next() -> the next value, or raise StopIteration
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
```

`enumerate()`:

```
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

关于 `yield` 参考

```
In [1]: def simple_generator():
   ...:     yield 1
   ...:     yield 2
   ...:     yield 3
   ...:

In [2]: for value in simple_generator():
   ...:     print value
   ...:
1
2
3

In [3]: our_generator = simple_generator()

In [4]: next(our_generator)
Out[4]: 1

In [5]: next(our_generator)
Out[5]: 2

In [6]: next(our_generator)
Out[6]: 3

In [7]: next(our_generator)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-7-7e48a609051a> in <module>()
----> 1 next(our_generator)

StopIteration:
```

- [5.2.10. Yield expressions](https://docs.python.org/2.7/reference/expressions.html#yield-expressions)
- [python - What does the "yield" keyword do? - Stack Overflow](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
- [Improve Your Python: 'yield' and Generators Explained](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)
- [The Python yield keyword explained | Python Tips](https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/)

循环, 参考

- [5.6. Looping Techniques](https://docs.python.org/2.7/tutorial/datastructures.html#looping-techniques)

---

## break

`break` statement 用来跳出`for` 或 `while` 循环.

```
In [1]: for n in range(2, 10):
   ...:     for x in range(2, n):
   ...:         if n % x == 0:
   ...:             print("{} = {} * {}".format(n, x, n/x))
   ...:             break
   ...:     else:
   ...:         print("{} is a prime number".format(n))
   ...:         
2 is a prime number
3 is a prime number
4 = 2 * 2
5 is a prime number
6 = 2 * 3
7 is a prime number
8 = 2 * 4
9 = 3 * 3
```

如上面的例子, 如果 `n = 4`, for 循环下去, 找到 n = 2 * 2, break, 就跳出循环. 开始下一阶段 `n = 5`.

上面 `else` clause(语句)是在`for x in range(2, n)` 循环结束的时候, 才会执行的语句.

**在这里, 我们可以一直有这样一个观点: 就是 else 肯定是跟在 if 语句后面的.** 看看上面的例子, 就知道. `else` 语句还可以跟在 `for` 或者 `while` 语句后面. 比如下面的例子.

```
In [2]: t = 0

In [3]: while t < 3:
   ...:     print(t)
   ...:     t += 1
   ...: else:
   ...:     print("The while loop is ended")
   ...:     
0
1
2
The while loop is ended
```

这可以用来调试, 看看 `while` 是否会停止.

初学者刚入门, 以为 `else` 常与 `if` 语句联合在一起. Tutorial 提到 `else` 和 `try` 语句更常见. 这就是可能就是所练习和经验问题.

关于 `try` statement 详见:  [8.3. Handling Exceptions](https://docs.python.org/2.7/tutorial/errors.html#handling-exceptions)

---

## continue

`continue` statement continues with the next iteration of the loop. 即开始下一步的迭代. 比如

```
In [7]: for num in range(2, 10):
   ...:     if num % 2 == 0:
   ...:         print("Hallo world")
   ...:         print("Find an even number {}".format(num))
   ...:         continue
   ...:     print("Find a number {}".format(num))
   ...:     
Hallo world
Find an even number 2
Find a number 3
Hallo world
Find an even number 4
Find a number 5
Hallo world
Find an even number 6
Find a number 7
Hallo world
Find an even number 8
Find a number 9
```

我们会发现,

- (1) 如果 `num = 2`, 执行`continue`,
- (2) 则是直接回到 `for num in range(2, 10):`
- (3) 此时 `num = 3`, `if` 条件语句判断 行不通,
- (4) 则执行 `prin("Find a numer {}".format(num))`, 即得出上面的一系列结果.
- (5) 循环回到第(2)步, 直到循环结束, 停止.

---

## pass

> The `pass` statement does nothing. It can be used when a statement is required syntactically(句法上正确) but the program requires no action. For example:

```
In [8]: while True:
   ...:     pass
   ...:
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-8-cccdd40a5a4c> in <module>()
----> 1 while True:
      2     pass

KeyboardInterrupt:
```

(1) 从上面的例子看出, `while True: pass` 一直循环, 直到 `ctrl+C` 结束.

(2) 也可以使用用来建立最小的 classes:

```
In [9]: class MyEmptyClass:
   ...:     pass
   ...:
```

(3) 可以用做`占位符`, 未来再做填补. 先聚焦在更抽象级别, 后面再填补具体细节.

```
In [10]: def initlog(*args):
    ...:     pass    # Remember to implement this!
    ...:
```

---
