# chapter 01

## 1.1 电脑: 万能机

电脑就是一个机器, 上面配有程序软件.

电脑比喻为一个系统: 输入-系统(电脑)-输出.

> A modern computer can be defined as "a machine that stores and manipulates information under the control of a changeable program."

- 电脑为机械:
    - 有输入才有输出
- 电脑需要程序
    - 程序就是一个个指令, 指导机器工作

其实所有电脑都一样, 都是一台万能机, 上面有程序指导其完成人类需要完成的任务.

## 1.2 程序的力量

- 没有程序, 计算机就是一台机器而已.
- 编程是计算机科学的基础. (搞懂电脑的基础)
- 不懂编程的使用者就是计算机的奴隶, 而程序员则掌控计算机.
- 编程有趣. (创建自己的作品, 多有意思啊!) 权当编程为一种兴趣.
- 学习编程, 发展有效解决问题的能力, 分析复杂系统的能力.
- 编程, 拓宽你的能力圈.

## 1.3 计算机科学 CS

类比: 计算机之于 CS, 犹如 telescopes are to astronomy.

- Q
    - What processes can we describe?
    - What can be computed?
- 方法论
    - Design an algorithm: a solution
    - Analysis of algorithms.  the process of examining algorithms and problems mathematically.
    - Experimentation. 有些问题复杂, 无法分析, 这时候得依靠试验.
- 一些领域
    - networking
    - human-computer interaction
    - AI
    - computational science
    - databases
    - software engineering
    - web and multimedia Design
    - management information systems
    - computer security.

## 1.4 硬件基础

![01](https://dn-learnml.qbox.me/image/programming/ppai2cs_01_01_functional_view_of_computer.JPG)

- Input devices
- CPU: central processing unit
    - brain
    - basic operations are carried out
- Memory: stores programs and data
    - CPU <---> main memory (RAM: Random Access Memory, 断电则里面数据全无)
    - Second memory: 用于永久存储.
- Output devices

运作: CPU 读取程序(存放在 Second memory), 加载到 main memory, 供 CPU 处理.

循环往复.

- fetch
- decoded
- executed

---

## 1.5 编程语言

程序只不过是告诉计算机如何工作的一条条指令而已. 计算机只能理解 machine code, 不同类型的 CPU 拥有各自的 machine code. 大多编程语言都有各自的 syntax 和 semantics (这样做, 人类好理解), 这些编程语言为高级语言.  

- 编程语言
    - a precise form: syntax
    - a precise meaning: semantics

![02](https://dn-learnml.qbox.me/image/programming/ppai2cs_01_02_compile.JPG)

要让计算机理解高级语言, 就需要编译器 compiler, 将高级语言(源代码 source code)编译成计算机读懂的 machine code(这样计算机就可以理解, 计算机不理解之前人类理解的, 两者理解方式不一样).  计算机硬件只能理解低级别的语言 --- 机器语言, 我们人类不是那么容易理解 机器语言(如果你想学习, 也是可以理解的), 更容易理解高级语言(Python, Java, C++, Perl, Scheme or BASIC).

**编译**: 编译器就是将 高级语言(source code) 翻译(编译) 成 机器语言(machine code). 这个过程, 一次完成, 就不用在下一次运行 program 的时候再做一次.

编译器 compiler 也是一个程序, 相对比较复杂.

![03](https://dn-learnml.qbox.me/image/programming/ppai2cs_01_03_interpreting.JPG)

**解释器**: An interpreter is a program that simulates a computer that understands a high-level language.

编译和解释哪里存在不同呢???

- compiling: 一次性完成, 后面无需再次进行.
- interpreting: 程序每一次运行, 都得进行一次.

这么说: 有些高级语言使用 compiler, 有些使用 interpreter 咯, 那么每次运行时间就存在差异咯???

高级语言具有可移植性. 不同的CPU 机器语言不一样, 不过高级语言需要翻译成机器语言. 编译器就可以针对不同的CPU, 将其翻译成对应可读懂的机器语言.

## 1.5 The magic of Python

- Genie: Python interpreter 所以 Python 相对于 C(使用 Compiler) 速度相对慢.

---

```
@Anifacc
```
