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
