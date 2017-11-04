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

### 1 默认形式参数

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

---

### 2 Keyword Argument 关键字参数

```
In [29]: def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue')
    ...: :
    ...:     print "-- This parrot wouldn't", action,
    ...:     print "if you put", voltage, "volts through it."
    ...:     print "-- Lovely plumage, the", type
    ...:     print "-- It's", state, "!"
    ...:     

In [30]: parrot(1000)
-- This parrot wouldn't voom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

In [31]: parrot(voltage=1000)
-- This parrot wouldn't voom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

In [32]: parrot(voltage=10000000, action="V00000M")
-- This parrot wouldn't V00000M if you put 10000000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

In [33]: parrot(action='vooooooooom', voltage=100000)
-- This parrot wouldn't vooooooooom if you put 100000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

In [34]: parrot('a million', 'bereft of life', 'jump')
-- This parrot wouldn't jump if you put a million volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's bereft of life !

In [35]: parrot('a thousand', state='pushing up the daisies')
-- This parrot wouldn't voom if you put a thousand volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's pushing up the daisies !
```

上面的形式参数方式正确, 下面案例显示显示错误:

```
In [36]: parrot()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-36-563b49e6b32c> in <module>()
----> 1 parrot()

TypeError: parrot() takes at least 1 argument (0 given)

In [37]: parrot(voltage=5.0, 'dead')
  File "<ipython-input-37-01dca0be3920>", line 1
    parrot(voltage=5.0, 'dead')
SyntaxError: non-keyword arg after keyword arg


In [38]: parrot(110, voltage=220)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-38-9bcd7eaed44e> in <module>()
----> 1 parrot(110, voltage=220)

TypeError: parrot() got multiple values for keyword argument 'voltage'

In [39]: parrot(actor='John Cleese')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-39-8d2ac8bc1850> in <module>()
----> 1 parrot(actor='John Cleese')

TypeError: parrot() got an unexpected keyword argument 'actor'
```

任何程序, 出现报错, 先将显示的错误信息看清楚, 看自己能不能解决. **常识**.

- **新知**:
    - `*name` : receives a tuple containing the positional arguments beyond the formal parameter list.
    - `**name`: receives a dictionary containing all keyword arguments except fo those corresponding to a formal parameter.


```
In [41]: def cheeseshop(kind, *arguments, **keywords):
    ...:     print "-- Do you have any", kind, "?"
    ...:     print "-- I'm sorry, we're all out of", kind
    ...:     for arg in arguments:
    ...:         print arg
    ...:
    ...:     print "-" * 40
    ...:
    ...:     keys = sorted(keywords.keys())
    ...:     for kw in keys:
    ...:         print kw, ":", keywords[kw]
    ...:         

In [42]:     cheeseshop("Limburge", "It's very runny, sir",
    ...:                "It's really very, VERY runny, sir.",
    ...:                shopkeeper="Michael Palin",
    ...:                client="John Cleese",
    ...:                sketch="Cheese Shop Sketch")
-- Do you have any Limburge ?
-- I'm sorry, we're all out of Limburge
It's very runny, sir
It's really very, VERY runny, sir.
----------------------------------------
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch
```

看出上面例子有什么特别之处么? 如果我们要用很多形式参数时, 在定义函数式, 就可以使用 `*name`, `**name`, 但要注意格式.

### 3 Arbitrary Argument Lists

**新知**: 还不明白.

> Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the variable number of arguments, zero or more normal arguments may occur.

```
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

尝试:

```
In [44]: def test(kind, who, *args):
    ...:     print "what's this:", kind
    ...:     print "Who are you? ", who
    ...:     print args
    ...:     

In [45]: test('hallo world', 'Jeremy', 2, 1)
what's this: hallo world
Who are you?  Jeremy
(2, 1)

In [55]: test('hallo world', 'Jeremy', 2, 1, name='jeremy_anifcc', age=18)
what's this: hallo world
Who are you?  Jeremy
(2, 1)
{'age': 18, 'name': 'jeremy_anifcc'}

```

### 4 unpacking argument lists

> The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments.

**新知**: `*` operator unpack the arguments out of a list or tuple.

```
In [46]: range(3, 6)
Out[46]: [3, 4, 5]

In [47]: args1 = [3, 6]

In [48]: range(*args1)
Out[48]: [3, 4, 5]

In [49]: args2 = (3, 6)

In [50]: range(*args2)
Out[50]: [3, 4, 5]
```

**新知**:

- 观上例, `*args` 是形式参数, 则 pack arguments. `tuple`
- `*args` 是实际参数, 则 unpack arguments. 针对 `tuple, list`
- `**args` 类似. 针对 `dictionary`

```
In [51]: def parrot(voltage, state='a stiff', action='voom'):
    ...:     print "-- This parrot wouldn't", action
    ...:     print "if you put", voltage, "volts through it."
    ...:     print "E's", state, "!"
    ...:     

In [52]: d = {"voltage": "four million", "state": "bleedin' demised", "action": "VO
    ...: OM"}

In [53]: parrot(**d)
-- This parrot wouldn't VOOM
if you put four million volts through it.
E's bleedin' demised !
```

### 5 lambda expression lambda 表达式

**新知**:简洁 pythonic 用 `lambda` keyword.

`lambda a, b: a+b`

- using a lambda expression to return a function.

```
In [56]: def make_incrementor(n):
    ...:     return lambda x: x + n
    ...:

In [57]: f = make_incrementor(42)

In [58]: f(3)
Out[58]: 45

In [59]: f(1)
Out[59]: 43

In [60]: f(0)
Out[60]: 42
```

- pass a small function as an argument:

```
In [61]: pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

In [62]: pairs.sort(key=lambda pair: pair[1])

In [63]: pairs
Out[63]: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

Pythonic, 简洁, 精简. **新知**.

### 6 Documentation Strings

```
In [4]: def my_function():
   ...:     """Do nothing, but document it.
   ...:     
   ...:     No, really, it doesnot do anything.
   ...: Let us see this line.
   ...:     How it will be.
   ...:     """
   ...:     pass
   ...:

In [5]: print my_function.__doc__
Do nothing, but document it.

    No, really, it doesnot do anything.
Let us see this line.
    How it will be.
```

Documentation 注意: **新知** or 代码风格

- 第一行: 精简的摘要总结
    - For brevity, it should not explicitly state the object’s name or type, since these are available by other means 不要出现 对象 的名字或类型
- 第二行 空行
- 下面的行: 描述对象的调用约定, 缺点
    - describing the object’s calling conventions, its side effects, etc.

---
