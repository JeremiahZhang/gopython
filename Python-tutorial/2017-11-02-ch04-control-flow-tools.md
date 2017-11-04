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

## def function

```
def fib(n):     # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b

def main():
    n = int(raw_input("Please enter the number to write"
                        " Fibonacci series: "))
    fib(n)

if __name__ == '__main__':
    main()
```

上面的script, 我们可以保存为 `fib.py`, 然后我们可以查长 `docstring`:


```
>>> import fib
>>> fib.fib.__doc__
'Print a Fibonacci series up to n.'
```

Docstring 可参考 [4.7.6. Documentation Strings](https://docs.python.org/2.7/tutorial/controlflow.html#tut-docstrings)

> it’s good practice to include docstrings in code that you write, so make a habit of it.

function 也可以看作为一个对象.

```
In [1]: def fib(n):
   ...:     a, b = 0, 1
   ...:     while a < n:
   ...:         print a,
   ...:         a, b = b, a+b
   ...:         

In [2]: fib
Out[2]: <function __main__.fib>

In [3]: f = fib

In [4]: f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

`def fib(<形式参数>)`  
`fib(<实际参数>)`  

Python中函数中<形式参数>不能改变<实际参数>值.

> In programming language parlance, Python is said to pass all parameters by **value**.

没有`return` statment 的函数也返回一个特殊的值 `None`(a build-in name). 一起看看使用 `return` statement.

```
In [9]: def fib2(n):    # return Fibonacci series up to n
   ...:     """Return a list containing the Fibonacci series up to n."""
   ...:     result = []
   ...:     a, b = 0, 1
   ...:     while a < n:
   ...:         result.append(a)
   ...:         a, b = b, a+b
   ...:
   ...:     return result
   ...:

In [10]: f100 = fib2(100) # call it

In [11]: f100             # write the result
Out[11]: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

涉及内容:

- `return`
- `obj.methodname`
    - `result.append(a)` calls a method of the list object `result`.

---

## More on Defining functions

- 默认形式参数

```
In [12]: def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    ...:     while True:
    ...:         ok = raw_input(prompt)
    ...:         if ok in ('y', 'ye', 'yes'):
    ...:             return True
    ...:         if ok in ('n', 'no', 'nop', 'nope'):
    ...:             return False
    ...:         retries = retries - 1
    ...:         if retries < 0:
    ...:             raise IOError('refusenik user')
    ...:         print complaint
    ...:         

In [13]: ask_ok('no')
no
Yes or no, please!
no
Yes or no, please!
no
Yes or no, please!
no
Yes or no, please!
no
---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
<ipython-input-13-25b3fd463f14> in <module>()
----> 1 ask_ok('no')

<ipython-input-12-024ae5230278> in ask_ok(prompt, retries, complaint)
      8         retries = retries - 1
      9         if retries < 0:
---> 10             raise IOError('refusenik user')
     11         print complaint
     12

IOError: refusenik user

In [14]: ask_ok('Do you really want to quit?')
Do you really want to quit?no
Out[14]: False

In [15]: ask_ok('Ok to overwrite the file?', 2)
Ok to overwrite the file?yes
Out[15]: True

In [16]: ask_ok('Ok to overwrite the file?', 2, 'Come on, only yes or no')
Ok to overwrite the file?slsl
Come on, only yes or no
Ok to overwrite the file?no
Out[16]: False

```

- `in` keyword

```
In [17]: i = 5

In [18]: def f(arg=i):  # at the point of function definition
    ...:     print arg  # default value i = 5
    ...:     

In [19]: i = 6     # new value

In [20]: f()        # 不再改变
5

```

上面的例子, 再次提醒我们, **ython is said to pass all parameters by value**. 从上面的例子, 我们可以这么理解:

在定义 `f(arg=i)` 函数的时候, Python 将 `arg` 参数 指向 `5`(i 所指向的值).

以后, 如果 `f(arg=i)`函数无参数调用, 如`f()`, 那么默认的形式参数`arg=5`.

- **警告**: 形式参数使用 mutable object 时(list, dictionary, instances of most classes) 需要特别注意, mutable object是否改变. 比如下面的例子. **新知**

```
In [21]: def f(a, L=[]):
    ...:     L.append(a)
    ...:     return L
    ...:

In [22]: print f(1)
[1]

In [23]: print f(2)
[1, 2]

In [24]: print f(3)
[1, 2, 3]

In [25]: print f(1)
[1, 2, 3, 1]

```

如上面 local 参数 `L` 改变的例子, 我们可以通过下面的方法, 不至于引起 `L` list 的改变.

```
In [21]: def f(a, L=[]):
    ...:     L.append(a)
    ...:     return L
    ...:

In [22]: print f(1)
[1]

In [23]: print f(2)
[1, 2]

In [24]: print f(3)
[1, 2, 3]

In [25]: print f(1)
[1, 2, 3, 1]

```
