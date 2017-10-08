# 第7章: 决策结构 Decision Structures

- 目标
    - 理解: one-way `if` statement
    - 理解: two-way `if-else` statement
    - 理解: multi-way `if-elif-else` statement  
    - The idea of exception handling and be able to write simple exception handling code that catches standard Python run-time errors.(新知)
    - Boolean expressions 概念 和 `bool` data type.
    - 能 Read, write, and implement algorithms that employ decision structures, including those that employ sequences of decisions and nested decision structures.

---

## 1.Simple Decision

`Control Structures` 中的`Decision Structures`: which are statements that allow a program to execute different sequences of instructions for different cases, effectively allowing the program to "choose" an appropriate course of action.

```
if <condition>:
    <body>
```

`<expr> <relational-operator> <expr>`:

| Python | Meaning     |
| :------------- | :------------- |
| <     | 小于         |
| <=    | 小于等于      |
| ==    | 等于         |
| >=    | 大于等于      |
| >     | 大于         |
| !=    | 不等于       |

`=` 与 `==` 是不同的. `=` 用于赋值, 而 `==` 用于条件句中, 判断使用.

比较strings, 顺序为 `lexicographic`: strings are put in alphabetic order according to the underlying Unicode values. 按 Unicode 中 字符 数值大小来比较大小.

```
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> math.__name__
'math'
>>> __name__
'__main__'
>>>
```

看下一代码:

```
if __name__ == "__main__":
    main()
```

> This guarantees that `main` will automatically run when the program is invoked directly, but it will not run if the module is imported.

---

## 2.Two-way Decisions

```
if <condition>:
    <statements>
else:
    <statements>
```

---

## 3.Multi-way Decisions  

```
if <condition1>:
    <case1 statements>
elif <condition2>:
    <case2 statements>
elif <condition3>:
    <case3 statements>
...
else
    <default statements>
```

---

## 4.Exception Handling  

`quadratic5.py`

```
try:
    <body>
except <ErrorType>:
    <handler>
```

`quadratic5.py`

---

## 5.Study in Design: Max of three

> Whenever you write a decision, you should ask yourself two crucial question. 1, when the condition is true, are you absolutely certain that executing the body of the decision is the right action to take? (2) The converse of the first: are wu certain that this condition is true in all cases where x1 is the max?

书中列举寻找最大数的方法, 一些总结.

- 解决问题的方法不止一种, 当我们想出一种方法的时候, 我们要问问自己:"有没有其他更好的办法?"
    - strive for clarity
    - simplicity
    - efficiency
    - scalability(可扩展性)
    - elegance
    - **Good algorithms and programs are like poems of logic. They are a pleasure to read and maintain.**
- Be the computer.
- Generality is good. **It is not unusual that consideration of a more general problem can lead to a better solution for some special case.**
- Don't reinvent the wheel. 不要重复造轮子.

---

## Sum

- Basic control structures for making decision.
    - if
    - if-else
    - if-elif-else
- Boolean expressions:
    - `<, <=, !=, ==, >, >=`
- Exception handling: `try-except`
- Careful thought should be given to produce a correct, efficient, and understandable program.

---
