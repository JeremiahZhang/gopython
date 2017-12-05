# errror 与 exception

- syntax error
- exceptions: [6. Built-in Exceptions — Python 2.7.14 documentation](https://docs.python.org/2.7/library/exceptions.html#bltin-exceptions)

如何处理 exception, 如下.


```
>>> while True:
...     try:
...         x = int(raw_input("please enter a number:"))
...         break
...     except ValueError:
...         print "Oops! That was no valid number. Try again..."
...
please enter a number:ss
Oops! That was no valid number. Try again...
please enter a number:ss
Oops! That was no valid number. Try again...
please enter a number:10
```

看如果 exceptions 中的 error 类型不对应, 则直接报error. 如下所显示.

```
>>> while True:
...     try:
...         x = int(raw_input("please enter a number:_> "))
...         break
...     except TypeError:
...         print "Oh no."
...
please enter a number:_> ss
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
ValueError: invalid literal for int() with base 10: 'ss'
>>>
```

不过我们可以使用多个(TypeError, ValueError):

```
>>> while True:
...     try:
...         x = int(raw_input("enter a number:"))
...         break
...     except (TypeError, ValueError):
...         print "Please enter a number _>"
...
enter a number:ss
Please enter a number _>
enter a number:ss
Please enter a number _>
enter a number:12
```

`try except` 多层 `except`

```
import sys

try:
    f = open("fibo.py")
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
```

`try... excepte` + `else`

```
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
```

自己定义 exception clause 变量哦

```
>>> try:
...     raise Exception('spam', 'ryb', 'low level people')
... except Exception as instance:
...     print type(instance)
...     print instance.args
...     print instance
...     x, y, z = instance.args
...     print 'x = ', x
...     print 'y = ', y
...     print 'z = ', z
...
<type 'exceptions.Exception'>
('spam', 'ryb', 'low level people')
('spam', 'ryb', 'low level people')
x =  spam
y =  ryb
z =  low level people
>>>
```

> If an exception has an argument, it is printed as the last part (‘detail’) of the message for unhandled exceptions.

> Exception handlers don’t just handle exceptions if they occur immediately in the try clause, but also if they occur inside functions that are called (even indirectly) in the try clause. For example:

```
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as detail:
...     print 'Handling run-time error:', detail
...
Handling run-time error: integer division or modulo by zero
```

# Raise exceptions

处理

```
>>> try:
...     raise NameError('HITHERE')
... except NameError:
...     print 'an exception flew by!'
...     raise
...
an exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HITHERE
>>> raise
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must be old-style classes or derived from BaseException, not NoneType
```

自定义 exceptions

```
>>> class MyError(Exception):
...     def __init__(self, value):
...         self.value = value
...     def __str__(self):
...         return repr(self.value)
...
>>> try:
...     raise MyError(2*2)
... except MyError as e:
...     print 'My exception occurred, value: ', e.value
...
My exception occurred, value:  4
>>>
>>>
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyError: 'oops!'
```

```
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
```

# 定义 clean-up Actions

`finally` clause

```
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print 'goodby, world!'
...
goodby, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

> A finally clause is always executed before leaving the try statement, whether an exception has occurred or not.

```
>>> def divide(x, y):
...     try:
...          result = x / y
...     except ZeroDivisionError:
...          print 'division by zero!'
...          break
...     else:
...          print 'result is', result
...     finally:
...         print 'executing finally clause'
...
  File "<stdin>", line 6
SyntaxError: 'break' outside loop
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print 'division by zero!'
...     else:
...         print 'result is', result
...     finally:
...         print 'executing finally clause'
...
>>> divide(2, 1)
result is 2
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide('2', '1')
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

# Predefined Clean-up Actions

新知:

```
for line in open('myfile.txt'):
    print line,
```

打开文件, 没有关闭. 对简单脚本问题不大, 对与大型应用, 则会造成麻烦. 什么麻烦呢?!!

如何解决:

```
with open('myfile.txt') as f:
    for line in f:
         print line,
```

使用 `with open('...') as f`, 执行完上面的语句, f 文件总是关闭的. 这就是一大好处.