# 第三章: 数值计算

- 目标:
    - To understand the concept of data type.
    - To be familiar with the basic numeric data types in Python.
    - To understand the fundamental principles of how numbers are represented on a computer.
    - To be able to use the Python math library.
    - To understand the accumulator program pattern.
    - To be able to read and write programs that process numerical data.
- Sum:
    - The way a computer represents a particular kind of information is called a data type. The data type of an object determines what values it can have and what operations it supports.
    - Data types for representing numeric values, int and float(Python)
        - 整数: int
        - 分数: float
    - mathematical operations:
        - addition: `+`
        - subtraction: `-`
        - multiplication:  `*`
        - division: `/`
        - integer division: `//`
        - remainder: `%`
        - exponentiation: `**`
        - absolute value: `abs(x)`
    - python `math` library: `import math`
    - bits 和 数值 overflow, python 的解决方案.
    - Python 的混合数值类型中 , 是将 整数型数据 int 转化为 float 型数据.
    - `int(), float(), round()`

---

## 1.Numeric data types

> The information that is stored and manipulated by computer programs is generically referred to as **data**. Different kinds of data will be stored and manipulated in different ways.

- 能用整数 int 的就用它.
- Python 中 `/` 总是返回浮点数 float.
- 除法:
    - python2: `a / b`
        - if a, b 都是 int 类型数值, 那么 结果返回 int 值.  对应 Python3 的整除运算 `//`.
        - if a, b 中, 有一个是 float 类型, 那么 返回 float 类型值. 对因 Python3 中的 除法运算 '/'.
    - Python3 中的除法 '/' 总是返回 float 类型数值.

## 2.Math library

- `import math`
    - `pi`: 圆周率
    - `e`: 自然数, 2.71828....
    - `sin(x)`: 三角函数 正弦 sin
    - `cos(x)`: 三角函数 余弦 cos
    - `tan(x)`: 三角函数 正切 tan
    - `asin(x)`: 反函数
    - `acos(x)`: 反函数
    - `atan(x)`: 反函数
    - `log(x)`: lnx
    - `log10(x)`: log_{10}(x)
    - `exp(x)`: e^x
    - `ceil(x)`: the smallest whole number >= x 大于等于 x 的最小整数.(天花板)
    - `floor(x)`: <= x 的最大整数.(地板)

## 3.阶乘

> n!

程序编织, 初始化变量. fact = 1.

> Whenever you use the accumulator pattern, make sure you include the proper initialization.

---

## 4.计算机计算的局限

> Computer representations of numbers (the actual data types) do note always behave exactly like the numbers that they stand for.

> Computer memory is composed of electrical "switches", each of which can be in one of two possible states, basically on or off.

计算机内存或存储的本质.

涉及到 bits.

- 1 bit: 2种可能
- 2 bits: 2^2 = 4 种可能
- 3 bits: 2 ^ 3 = 8
- ...
- n bits: 2^n

现在的计算CPU, 不是 32 bits 就是 64 bits.

- 32 bits CPU : 2 ^ 32 种 可能值
    - (+) or (-): 2 ^ 32 / 2 = 2 ^ 31
        - (`-2 ^ 31`) ~ `(2 ^ 31) -1`
        - 因为 中间 还有个 0, 所以要 -1
- 64 bits CPU : 2 ^ 64 种 可能值
    - + or - : 2^64 / 2 = 2 ^ 63
        - `(-2 ^ 63)` ~ `(2 ^ 63) - 1`

其中 `2 ^ 31 - 1 = 2147483647 (2.1 billion)`, `12! ~= 4.8 million` and `13! ~= 6.2 billion`. 所以 在32位的计算机上, Java 程序 只能计算 12的阶乘.

> But after thath the representation `overflows` and the results are garbage.

因此 Java 程序 无法计算 13! 阶乘.

Python 的方案: (并未完全明白)

> Fortunately, Python has a better solution for large , exact values. A Python int is not a fixed size, but expands to accommodate whatever value it holds. The only limit is the amount of memory the computer has available to it.

> When the value is small, Python can just use the computer's underlying int representation and operations.

> When the value gets larger, Python automatically converts to a representation using more bits.

> Of course, in order to perform operations on larger numbers, Python has to break down the operations into smaller units that the computer hardware is able to handle. Sort of like the way you might to do long division by hand.

> These operations will not be as efficient (they require more steps), but they allow our Python ints to grow to arbitrary size. And that's what allows our simple factorial program to compute some whopping large results. This is a very cool feature of Python.

---

## 5.Type of conversions and rounding.

> 类型转换, 和 圆整.

`x = 5.0 * 2`

将 float 浮点数 int, 比较危险, 因为将小数部分去掉.
而 将 int 转化为 float 则不会出现这样的问题.  

rounding:

```
>>> import math
>>> math.pi
3.141592653589793
>>> a = math.pi
>>> round(a, 2)
3.14
>>> round(a, 3)
3.142
>>> print(round(a, 2))
3.14
>>> print(round(a, 3))
3.142
```

Remember:

> Floats are always approximations; we get something that's very close to what we requested.
