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
