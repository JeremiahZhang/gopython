# Intro

`#`: 注释

- calculator
    - numbers
    - strings
    - unicode strings
    - lists
- 1st steps towards programming

---

# Calculator

## numbers

` +, -, *, /, //, %`

`2.7x` 下 `/` 除法的使用:

```
In [1]: 2 + 2
Out[1]: 4

In [2]: 50 - 5*6
Out[2]: 20

In [3]: 5/4   # int / int  -> int
Out[3]: 1

In [4]: 5/4.0 # int / float -> float
Out[4]: 1.25

In [5]: 5.0/4 # float / int -> float
Out[5]: 1.25

In [6]: (50 - 5.0*6) / 4
Out[6]: 5.0

In [7]: 20.0/4
Out[7]: 5.0

In [18]: 3 * 3.75 / 1.5
Out[18]: 7.5

In [19]: 7.0 / 2
Out[19]: 3.5
```

`2.7x`下 `//`(取整)

```
In [8]: 17 // 3
Out[8]: 5

In [9]: 17 / 3.0
Out[9]: 5.666666666666667

In [10]: 17 // 3.0 # explicit floor division discards the fractional part
Out[10]: 5.0

In [11]: 17 % 3
Out[11]: 2

In [12]: 5 * 3 + 2
Out[12]: 17
```

`**` 幂次

```
In [12]: 5 * 3 + 2
Out[12]: 17

In [13]: 5 ** 2
Out[13]: 25

In [14]: 2 ** 10
Out[14]: 1024
```

`=` 赋值

```
In [15]: width = 20

In [16]: height = 5 * 9

In [17]: width * height
Out[17]: 900
```

Python 命令行交互下, 上一行的 print output 值 会赋予 `_`, 注意不要用 `_` 幅值. 案例如下.

```
In [20]: tax = 12.5 / 100

In [21]: price = 100.50

In [22]: price * tax
Out[22]: 12.5625

In [23]: price + _   # _ = 12.5625
Out[23]: 113.0625

In [24]: round(_, 2) # _ = 113.0625
Out[24]: 113.06
```

其他参考:

- [9.4. decimal — Decimal fixed point and floating point arithmetic — Python 2.7.14 documentation](https://docs.python.org/2.7/library/decimal.html#decimal.Decimal)
- [9.5. fractions — Rational numbers — Python 2.7.14 documentation](https://docs.python.org/2.7/library/fractions.html#fractions.Fraction)
- [5. Built-in Types — Python 2.7.14 documentation](https://docs.python.org/2.7/library/stdtypes.html#typesnumeric)

---

## strings

```
In [25]: 'spam eggs'
Out[25]: 'spam eggs'

In [26]: 'doesn\'t'   # 一层 ' \' ' 下 \ 可逃逸
Out[26]: "doesn't"

In [27]: "doesn't"
Out[27]: "doesn't"

In [28]: '"yes," he said'
Out[28]: '"yes," he said'

In [29]: "\"YES, \" he said."  # 一层 " \" " 下 \ 可逃逸
Out[29]: '"YES, " he said.'

In [30]: '"Isn\'t," she said.'  # 两层 ' " \' " ' 下, \ 不可逃逸
Out[30]: '"Isn\'t," she said.'
```

上面的输出[25-30] 方便机器读取. 方便人类读取则使用 `print`.

```
In [30]: '"Isn\'t," she said.'
Out[30]: '"Isn\'t," she said.'  # 机器读取方便

In [31]: print '"Isn\'t," she said.'
"Isn't," she said.   # 人类可读, 方便

In [32]: two_lines = 'First line. \nSecond line.'

In [33]: two_lines
Out[33]: 'First line. \nSecond line.' # 机器可读

In [34]: print(two_lines)   # 人类可读
First line.
Second line.
```

若不想在`''` 让 `\` 逃逸, 在 strings 前加上 `r`, 成为 *raw strings*.

```
In [35]: print 'C:\some\name'     # 逃逸
C:\some
ame

In [36]: print(r'C:\some\name')   # 未逃逸
C:\some\name
```

`"""..."""` or `'''...'''` 多行打印 print, 使用  `\` 换行.

```
In [37]: print """\
    ...: Usage: thingy [OPTIONS]
    ...:      -h                    Display this usage message
    ...:      -H hostname           Hostname to connect to
    ...: """

Usage: thingy [OPTIONS]
     -h                    Display this usage message
     -H hostname           Hostname to connect to
```

使用 `+`, `*` 连接字符. 尽量不要使用.

```
In [38]: 3 * 'P' + 'ython'
Out[38]: 'PPPython'

In [39]: 'PPP' 'ython'
Out[39]: 'PPPython'

In [40]: prefix = 'PPP' # 采用赋值形式, 再连接, 不可行, 关注错误提示

In [41]: prefix 'ython'
  File "<ipython-input-41-11afabb1aa63>", line 1
    prefix 'ython'
                 ^
SyntaxError: invalid syntax

In [42]: prefix + 'ython'  # 使用 + 则可以连接
Out[42]: 'PPPython'

# 这个是最新发现 可以使用, 原来是这样处理多行的strings.

In [43]: text = ('Put several string within parentheses'
    ...:         ' to  have them joined together.')

In [44]: text
Out[44]: 'Put several string within parentheses to  have them joined together.'
```

字符 string 可 索引(indexed), 切片(sliced)等.

```
In [45]: word = 'Python'

#  P   y   t   h   o   n
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

In [46]: word[0]
Out[46]: 'P'

In [47]: word[1]
Out[47]: 'y'

In [48]: word[5]
Out[48]: 'n'

In [49]: word[-1]
Out[49]: 'n'

In [50]: word[-2]
Out[50]: 'o'

In [51]: word[-6]
Out[51]: 'P'

In [52]: word[0: 2]  # 左闭右开 word[0, 1]
Out[52]: 'Py'

In [53]: word[2: 5]  # 左闭右开 word[2, 3, 4]
Out[53]: 'tho'

In [54]: word[:2] + word[2:]
Out[54]: 'Python'

In [55]: word[:4] + word[4:]
Out[55]: 'Python'

# 特别的地方
In [56]: word[42]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-56-8054ffcdbeba> in <module>()
----> 1 word[42]

IndexError: string index out of range

# 注意这里
In [57]: word[2:42]
Out[57]: 'thon'

In [58]: word[42:]
Out[58]: ''
```

`len()` 获取字符串长度

```
In [61]: len(word)
Out[61]: 6
```

深入请参考:

- [5.6. Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange](https://docs.python.org/2.7/library/stdtypes.html#typesseq)
- [5.6.1. String Methods](https://docs.python.org/2.7/library/stdtypes.html#string-methods)
- [7.1.3. Format String Syntax](https://docs.python.org/2.7/library/string.html#format-string-syntax)
- [5.6.2. String Formatting Operations](https://docs.python.org/2.7/library/stdtypes.html#string-formatting-operations)

输入

```
help(str)     # 命令行中 查看 string 帮助文档
```

---

## Unicode strings

```
In [65]: u'Hello World !'
Out[65]: u'Hello World !'

In [66]: u'Hello\u0020World !'
Out[66]: u'Hello World !'

In [67]: u'Hello\u0020World \u0021'
Out[67]: u'Hello World !'
```

- `u`: indicates that a Unicode string is supposed to be created    
- `\u0020` : 空格   
- `\u0021` : `!` 感叹号.  

> For experts, there is also a raw mode just like the one for normal strings. You have to prefix the opening quote with ‘ur’ to have Python use the Raw-Unicode-Escape encoding. It will only apply the above \uXXXX conversion if there is an uneven number of backslashes in front of the small ‘u’.

```
In [68]: ur'Hello\u0020World \u0021'
Out[68]: u'Hello World !'

In [69]: ur'Hello\\u0020World \u0021'
Out[69]: u'Hello\\\\u0020World !'
```

> The raw mode is most useful when you have to enter lots of backslashes, as can be necessary in regular expressions.

`unicode()`

```
In [70]: u"abc"
Out[70]: u'abc'

In [71]: str(u"abc")
Out[71]: 'abc'

In [72]: u"äöü"
Out[72]: u'\xe4\xf6\xfc'

In [73]: str(u'\xe4\xf6\xfc')
---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
<ipython-input-73-50734c757496> in <module>()
----> 1 str(u'\xe4\xf6\xfc')

UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)

In [74]: str(u"äöü")  # 出错
---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
<ipython-input-74-8d9efc4228c3> in <module>()
----> 1 str(u"äöü")

UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)

In [75]: u"äöü".encode('utf-8')  # Convert Unicode string into utf-8
Out[75]: '\xc3\xa4\xc3\xb6\xc3\xbc'

In [76]: unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8') # utf-8 convert to Unicode encode
Out[76]: u'\xe4\xf6\xfc'

In [78]: print(u'\xe4\xf6\xfc')
äöü
```

默认 encoding 为 ASCII 编码, **The default encoding is normally set to ASCII, which passes through characters in the range 0 to 127 and rejects any other characters with an error.**

---

## [lists](https://docs.python.org/2.7/tutorial/introduction.html#lists)

lists:  

- indexed
- sliced
- mutable type

```
In [1]: square = [1, 4, 9, 16, 25]

In [2]: square
Out[2]: [1, 4, 9, 16, 25]

In [3]: square[0]
Out[3]: 1

In [4]: square[-1]
Out[4]: 25

In [5]: square[1:3
   ...: ]
Out[5]: [4, 9]

In [6]: square + [26, 49, 64, 81, 100]
Out[6]: [1, 4, 9, 16, 25, 26, 49, 64, 81, 100]
```

mutable:

```
In [7]: cubes = [1, 8, 27, 65, 125]

In [8]: cubes[3] = 64

In [9]: cubes
Out[9]: [1, 8, 27, 64, 125]
```

list 增加 items:

```
In [10]: cubes.append(6**3)

In [11]: cubes
Out[11]: [1, 8, 27, 64, 125, 216]

In [12]: cubes.append(7 ** 3)

In [13]: cubes
Out[13]: [1, 8, 27, 64, 125, 216, 343]
```

Assignment to slices:  

```
In [14]: letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

In [15]: letters
Out[15]: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

In [16]: letters[2:5] = ['C', 'D', 'E']

In [17]: letters
Out[17]: ['a', 'b', 'C', 'D', 'E', 'f', 'g']

In [18]: letters[2:5] = []

In [19]: letters
Out[19]: ['a', 'b', 'f', 'g']

In [20]: letters[:] = []

In [21]: letters
Out[21]: []
```

`len()` of lists:

```
In [22]: letters = ['a', 'b', 'c']

In [23]: len(letters)
Out[23]: 3
```

lists 内嵌:

```
In [24]: a = [1, 2, 3]

In [25]: b = [3, 4, 5]

In [26]: x = [a, b]

In [27]: x
Out[27]: [[1, 2, 3], [3, 4, 5]]

In [28]: x[0][1]
Out[28]: 2
```

# First Steps towards programming

```
# Fibonacci series
In [29]: a, b = 0, 1

In [30]: while b < 10:
    ...:     print b
    ...:     a, b = b, a+b
    ...:     
1
1
2
3
5
8

```

- 多重赋值
- while 循环: `<, >, ==, <=, >=, !=`

---

2017-11-01
