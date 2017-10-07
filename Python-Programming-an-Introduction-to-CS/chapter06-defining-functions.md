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

  
