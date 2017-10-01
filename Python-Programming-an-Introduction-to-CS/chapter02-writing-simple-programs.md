## 第二章: 编写程序

- 学习目标:
    - 软件开发流程, 思路 or 方法论
    - 程序通用过程: Input-Process-Output, 类似系统论中的`输入-系统-输出`
    - Understand the rules for forming valid Python identifiers and expressions
    - Python statements: input output,
        - assign values to variable
        - get information entered from the keyboard
        - perform a counted loop

---

## 1.软件开发流程

> Computers are very literal, and they must be told what to do right down to the last detail.

- 1.Analysis: **Analyze the Problem**. Studying the problem to be solved. 分析问题. 充分所需解决的问题. 尽可能去理解问题, 直到我们真正理解所面对的问题, 要不然我们怎么能解决呢? 开始编织程序前, 先彻底理解问题.
- 2.Specify: **Determine Specifications**. Describe excatly what your program will do. 明确具体要求.
- 3.Design: **Create a Design**. Writing and algorithm in pseudocode. Formulate the overall structure of the program.
- 4.Implement: **Implement the Design**. Translate the design into a computer language and put it into the computer.
- 5.Debugging: **Testing/Debugging**: Finding and fixing errors in the program.
- 6.Maintenance: **Maintenance**: Keeping the program up to date with evolving needs.

---

## 2.Elements of programs

> Programs manipulate data.

> All data has to be stored on the computer in some digital format, and different types of data are stored in different ways.

- Elements
    - identifiers: names
    - expressions
- Output statements
    - print 输出
- Assignment statements
    - <varibable> = <expr>
    - **simultaneous assignment** <var>, <var>, ..., <var> = <expr>, <expr>, ..., <expr>
- Loop  
    - Definite loop: counted loop
        - control structure

```
for <var> in <sequence>:
    <body>
```
- Remeber
    - 不同数据存储方式不一样.
    - A variable must always be assigned a value before it can be used in an expression.(变量在使用前, 赋值先)
    - The values of variables can be change; that's why they're called variables
    - Python 赋值, 内部的作用机制不同. **garbage collection**

一般语言:

![](https://dn-learnml.qbox.me/image/programming/ppai2cs_02_01_variable_box.png)

Python:

![](https://dn-learnml.qbox.me/image/programming/ppai2cs_02_02_variable_python.png)

---

## 总结

- 软件开发流程(解决问题流程, 编程流程)
    - 分析问题, 只有在充分理解问题的基础上, 才能开始编程解决问题.
    - 程序定义: 确定我们的程序到底要做什么.
    - 设计程序: 先写个程序的伪代码,
    - 代码编程: 将伪代码实现为程序代码
    - 调试: 编织好代码, 调试下, 有没有bug, 反馈改进.
    - 维护: 不断更新迭代.
    - (非常重要, 和解题一样, 有趣)
- 大多程序遵循: input - process - output
- 程序组成: statements:(identifiers + expressions)
    - Identifiers: names
    - expressions: the fragments of a program that produce data.(程序碎片, 构成程序)
        - literals:(文字) a representation of a specific value
        - variables: an identifier that stores a value
        - operators: `+ - * / **`
- Definite loop(有限循环)

---

## exercise

### Review Questions

> True or False

1. F
2. T
3. F
4. T
5. F
6. T
7. T
8. F
9. T
10. F

> Multiple Choice

1. c
2. a  
3. d
4. c
5. b  
6. a, b, d  
7. b  
8. a, d  
9. a  
10. d  

---

## Change log

```
@anifacc
2017.10.01
```
