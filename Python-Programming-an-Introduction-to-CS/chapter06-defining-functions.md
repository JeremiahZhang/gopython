# 第六章 函数定义

- 目标:
    - Why programmers divide programs up into sets of cooperating functions?
    - Define new functions in Python.
    - The details of function calls and parameter passing in Python
    - Write programs that use functions to reduce code duplication and increase program modularity.
- 自己的碎碎念
    - 为什么要使用函数?
        - 避免重复
        - 方便协作
        - 高效率
        - 可迁移性更强
    - 自己定义函数:
        - call
        - 传递参数

---

## 1.The Function of Functions

第四章 `futval_graph2.py`:

```
# futval_graph2.py

from graphics import GraphWin
from graphics import Text
from graphics import Point
from graphics import Rectangle

def main():
   print("This program plots the growth of a 10-year investment!")

   principal = eval(input("Enter the initial principal: "))
   apr = eval(input("Enter the annualized interest rate: "))

   win = GraphWin("Investment Growth Chart", 320, 240)
   win.setBackground("white")
   win.setCoords(-1.75, -200, 11.5, 10400)

   Text(Point(-1, 0), "0.0K").draw(win)
   Text(Point(-1, 2500), "2.5K").draw(win)
   Text(Point(-1, 5000), "5.0K").draw(win)
   Text(Point(-1, 7500), "7.5K").draw(win)
   Text(Point(-1, 10000), "10.0K").draw(win)

   bar = Rectangle(Point(0, 0), Point(1, principal))
   bar.setFill("green")
   bar.setWidth(2)
   bar.draw(win)

   for year in range(1, 11):
       principal = principal * (1 + apr)
       bar = Rectangle(Point(year, 0), Point(year+1, principal))
       bar.setFill("green")
       bar.setWidth(2)
       bar.draw(win)

   input("Press <Enter> to quit.")
   win.close()

if __name__ == '__main__':
   main()
```

两处出现类似的代码:设置 `bar`, 在`for` loop 循环前和循环内. 缺点:

- 类似代码写了两次
- 如果以后要维护, 那么相同的维护需要在两个不同的地方进行. 麻烦呢!!!

> Failing to keep related parts of the code in sync is a common problem in program maintenance.

代码维护, 需要间接高效. 这时候函数的作用就体现出来:

- To reduce code duplication
- To make programs more understandable
- and easier to maintain.

---

## 2.Functions, Informally

我们可以将一个 `function` 看作为一个 `subprogram` 子程序. 这个想法可以有.

化繁为简.

## 3.Example

`futval_graph3.py`

---

## 4.Functions and Parameters: The Exciting Details

`function` 内使用的变量 都是 `local`型 局部变量.

函数定义形式:

```
def <name>(<formal_parameters>):
    <body>
```

形式参数: 形参 `forml_parameters` 只能在 function 内部使用.

函数调用形式:

```
<name>(<actual_parameters>)
```

`actual_parameters` or `arguments` 参数.

Python 函数调用步骤:

- The calling program suspends execution at the point of the call
- The formal parameters of the function get assigned the values supplied by the actual_parameters in the call
- The body of the function is executed.
- Control return to the point just after where the function was called.

有编程基础很容易理解.

---

## 5.Getting Results from a Function  

#### 5.1 Functions That Return values

`triangle2.py`

### 5.2 Functions That Modify Parameters  

> Python does not allow passing parameters by reference. (C++ & Ada ..., do allow variables themselves to be sent as parameters to function).

Python 函数中的变量 无法影响 Argument. 只有返回值 赋予 Argument 变量 才起作用.

```
# add_interest.py

def add_interest(balance, rate):
    new_balance = balance * (1 + rate)
    return new_balance

def test():
    amount = 1000
    rate = 0.05
    amount = add_interest(amount, rate)
    print(amount)

if __name__ == '__main__':
    test()
```

但 `list` 在其中, 就可以改变.

```
# add_interest3.py

def add_interest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def main():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    add_interest(amounts, rate)
    print(amounts)

if __name__ == '__main__':
    main()

---
$ python3 add_interest3.py
[1050.0, 2310.0, 840.0, 378.0]
```

因为 `amounts` 为 `list`, 可修改. 传递到 function 操作后, 内部值改变.

> In Python parameters are always passed by value. However, if the value of the variable is a mutable object(like a list or graphics object), then changes to the state of the object will be visible to the calling program.
