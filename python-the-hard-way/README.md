# 2017-03-16 

跟着 dive into python 到达第五章 class， 发现许多看不懂，就此，先转到

- 自己之前的学习程度与教程：[Jeremiah‘s Python Star Trek · GitBook](https://www.gitbook.com/book/jeremiahzhang/omooc2py/details)
- Learn Python the hard way 学过一遍

自己还是在学，得一边用一边学，那么就从engineering vibration 的代码开始 [vibrationtoolbox/vibration_toolbox](https://github.com/vibrationtoolbox/vibration_toolbox) ，进入实际应用中，学习实战。

---

# 2017-03-29

学编程, 不求速成, 至少给自己7年时间, 慢慢来. 现在再过一遍 [Learn Python the Hard Way][0].

    system: win
    editor: ST2
    shell: Powershell
    Python Version: 2.7.13 |Anaconda 4.3.0

## Exercise

- [ex01 - 第一个程序关于-print][1], 最简单的 Python 脚本, 如同 "Hello World"
    - [PEP 263 -- Defining Python Source Code Encodings | Python.org](https://www.python.org/dev/peps/pep-0263/#abstract) 
- [ex02 - # 号是用来注释][2]
- [ex03 - 数学计算][3], 可以将 Python 当作计算器用哦
- [ex04 - 变量和命名][4], 变量定义. 命名是门学问, 好的命名, 让代码如同小说一般呢, 愿有如此境界
- [ex05 - 变量和 Print][5], 如何输出字符串？这里就是一种方法, 其他方法可参考[Fancier Output Formatting](https://docs.python.org/2.7/tutorial/inputoutput.html#fancier-output-formatting)
- [ex06 - 字符串和文本表达][6], 延伸阅读：
    -  输出格式：[Fancier Output Formatting](https://docs.python.org/2.7/tutorial/inputoutput.html#fancier-output-formatting)
    -  字符串格式化操作：[string formatting operations](https://docs.python.org/2.7/library/stdtypes.html#string-formatting-operations)
    -  有效字符连接：[Efficient String Concatenation in Python](https://waymoot.org/home/python_string/)
- [ex07 - 更多 print 输出][7] 值得注意的是 **print** 中 **,**的使用
- [ex08 - print print 2.0][8] **%s** 和 **%r** 的区别
- [ex09 - print print print 3.0][9]
    - 文档说明 """ 这里放置文档脚本 """
    - %r 格式操作符, debugging 时可看原始格式 debug
- [ex10 - 转义字符 escape sequence][10]
    - **\t** 相当于 tab
    - **\n** 换行
    - 更多参考：[List of Python Escape sequence characters with examples - LinuxConfig.org](https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples)
    - 【问题】：\U 和 \N{name}的使用, 见代码中的 说明
- [ex11 - 与用户交互][11] bulid in function 
    - [raw_input()](https://docs.python.org/2/library/functions.html#raw_input)
    - [Python raw_input Example (Input From Keyboard)](https://www.cyberciti.biz/faq/python-raw_input-examples/)
- [ex12 - 继续交互raw_input + pydoc][12] 
    - [25.1. pydoc — Documentation generator and online help system — Python 2.7.13 documentation](https://docs.python.org/2/library/pydoc.html)
        - The pydoc module automatically generates documentation from Python modules. 
        - 直接在shell 中键入 **pydoc pydoc** 查看说明 
        - 键 **q** 退出 pydoc, 好到 shell 中
    - 尝试 **pydoc open**
    - **pydoc file** 文件打开与写入等
    - **pydoc os** + **pydoc sys**
    - 这可以作为查看不懂函数or module or package等的方法
- [ex13 - from sys import argv][13] 命令行中键入参数, 传递到脚本中, unpackage, 再赋予变量便于在script中使用
    - 命令行中 **python ex13.py I Love Coding** 
    - 脚本名称 ex13.py 是一个参数, I, Love, Coding 分别是另外3个参数  
        - argv[0] = ex13.py  
        - argv[1] = I  
        - argv[2] = Love  
        - argv[3] = Coding  
- [ex14 - 参数输入 argv & raw_input()][14]
- [ex15 - 读取文件 open() 初级使用][15]
- [ex16 - 文件 打开 读取 写入][16]
- [ex17 - more files copyfile][17]
    - make it one line long: use [10.10. shutil — High-level file operations — Python 2.7.13 documentation](https://docs.python.org/2/library/shutil.html)
    - [my example]([15]:    https://github.com/JeremiahZhang/Alpha2Omega/blob/master/py_DiveIntoPython/ex17_one_line.py)
- [ex18 - 函数定义： def name variables: code --> function][18]
- [ex19 - 函数和变量 Functions and Variables - 变量在函数定义中的使用][19] 
- [ex20 - 函数和文件 Functions and Files][20]
    - [seek function](http://stackoverflow.com/questions/11696472/seek-function)
    - 命令行中键入: **pydoc file.seek** 可查看对应说明
- [ex21 - 函数返回值 Return][21]
- [ex22 - 回顾 what do you know so far][22]
    - List the symbol which you have learn 
    - momerize them 
    - 适当休息 利用好大脑
    - 学会自学
    - 会总结嘛
- [ex23 - explore source code][23]
- [ex24 - more practices][24]
- [ex25 - even more practices][25]
    - 句子 拆分 为 单词
    - 排序等
    - 可以以此例子为基础, 写一个文本统计词频的脚本
- [ex26 - debug someone's script][26]
    - 作为程序员要谦卑, 虚心学习, 仔细查验, 再下结论
- [ex27 - 逻辑记忆 布尔运算][27]
    - ```AND```
    - ```OR```
    - ```NOT```
    - 混合式等
- [ex28 - 布尔运算实现][28]
- [ex29 - what if - only if not else][29]
- [ex30 - if - elif - else][30]
- [ex31 - raw_input + if choose to make decisions][31]
- [ex32 - for loop and list][32]
    - 创建 list
        - ``` elements = []```
        - ``` elements = [i for i in range(6)]```
        - ```elements = list(i for i in range(6))```
- [ex33 - while 循环][33]
- [ex34 - List 获取][34]
- [ex35 - 分支和函数][35]
- [ex36 - 设计和Debugging][36]
- [ex37 - Python 一些符号 数据类型等][37]
    - 1. python keywords and example
        - [32.6. keyword — Testing for Python keywords — Python 2.7.13 documentation](https://docs.python.org/2/library/keyword.html) 
        - [List of Keywords in Python Programming](https://www.programiz.com/python-programming/keyword-list)
    - 2. python data type
        - [Python Variables and Data Types](https://www.programiz.com/python-programming/variables-datatypes) 
    - 3. string escape sequences
    - 4. string formats
    - 5. operators
    - 6. 参见 [Python THW EX37](https://learnpythonthehardway.org/book/ex37.html)
    - 建议去好好读他人代码 并自己注释 print 等 直到不用 print 就知晓结果, 如果有错, 就告诉原作者.
- [ex38 - list 相关 doing things to list][38]
    - when to use lists:
        - If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
        - If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
        - If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.
    - 每个程序是现实世界的模拟.
    - [OOP: Object-oriented programming - Wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming)
    - Real life:[Python Success Stories | Python.org](https://www.python.org/about/success/#web2-0)
        - [Invent with Python](http://inventwithpython.com/) 
        - [Django Book: How to Tango with Django: A Python Django Tutorial](http://www.tangowithdjango.com/)
    - [Tutorials that show real life applications and usage of Python.：learnprogramming](https://www.reddit.com/r/learnprogramming/comments/1rr976/tutorials_that_show_real_life_applications_and/)
- [ex39 - 字典][39]
- [ex40 - class][40]
- [ex41 - Object Oriented][41]
    - [script reading code](https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/oop_test.py)
- [ex42 - Is-A, Has-A, Objects, and Classes][42] 
    - [Python Tutorial: Object Oriented Programming](http://www.python-course.eu/object_oriented_programming.php) 
- [ex43 - Basic Object-Oriented Analysis and Design][43]
    - Process: TOP-DOWN
        - Write or draw about the problem
        - Extract key concepts from 1 and research them
        - Create a class hierarchy and object map for the concepts.
        - Code the classes and a test to run them
        - Repeat and refine
    - Bottom UP
        - Take a small piece of the problem; hack on some code and get it to run barely
        - Refine the code into something more formal with classes and automated tests.
        - Extract the key concepts you're using and try to find research for them.
        - Write a description of what's really going on.
        - Go back and refine the code, possibly throwing it out and starting over.
        - Repeat, moving on to some other piece of the problem.
- ex44 - Inheritance Versus Composition
    - [class][44_extra] 
        - [Encapsulation](https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/encapsulation.py)
        - Interitance 
            - [Implicit Inheritance][44a]
            - [Override][44b]
            - [Alter Before or After][44c]
            - [以上三者合成 All Three Combined][44d]
        - [composition][44e]
    - 异
        -  Inheritance 有父子继承关系
        -  Composition 无夫子继承关系
    - 同
        - 相似性, 相互独立 
    - 建议：
        - 少用多层继承：Avoid multiple inheritance at all costs, as it's too complex to be reliable.
        - 使用 composition 来包装代码如模块：Use composition to package code into modules that are used in many different unrelated places and situations.
        - Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.
        - 不要局限于以上, 个人经验嘛
    - PS Python Code style
        - PEP 8 关于代码风格规范[PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
            - [import](https://www.python.org/dev/peps/pep-0008/#imports) 
            - [Module level dunder names](https://www.python.org/dev/peps/pep-0008/#module-level-dunder-names)
            - [Whitespace in Expressions and Statements](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)
        - 自己再加个 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [ex45 - You Make a Game](https://learnpythonthehardway.org/book/ex45.html)
    - Function Style: 尽量简洁
    - Class Style
    - Code Style
    - Good Comments
    - 任务: 自己写个小游戏, 熟悉class, 形成自己的代码风格, 并纠正他人代码中的一些不足之处.
    - 构思自己的小游戏,俺准备玩一下VI三表的游戏
        - 正在构思中... ```class Waiting(object): pass ```
- [ex46 - 项目框架练习 A Project Skeleton][46]
    - Python package 安装没有过多纠结, 用时再研究, 因为使用 Anaconda 4.3.0 下的python, 有些包已经装好
    - [建立项目框架](https://learnpythonthehardway.org/book/ex46.html)
- [ex47 - 自动化测试练习 Automated Test][47]
    - 自动化测试, 在 ex46 的练习上继续进行自动化测试
        - 每一个 module 都需要测试, 需要在 ```tests/``` 放入 test file, 并且要有对应命名```ModuleName_tests.py```, 要不然 nosetests 不运行哒
        - keep test cases(functions) short 
        - 代码简洁
        - 测试不行啦, 有时候需要推倒重来
- [ex48 - Advanced User Input 其实是继续自动化测试][48]
    - 顺便理解 ```if __name__ == "__main__"``` [Python Tutorial: if __name__ == '__main__' - YouTube](https://www.youtube.com/watch?v=sugvnHA7ElY)
        - 脚本1运行时 __name__ = __main__
        - 那么 import module 中的 __name__ 就不是 __main__啦
    - 按照前一个练习的 skeleton 来填写代码
    - ```$ nosetests``` 可以测试是否出错
- [ex49 - making sentence][49]
    - [x] import modules
    - [ ] nosetests other people script
    - [ ] learn nose read documention
        - [ ] assert_raises
- [ex50 - Make a website][50]
    - 作者使用 web.py web框架来开发
    - 俺准备试验 Django 来开发一个website, C.S.Lewis 路益士的网站. 
    - 俺就参考 [Tango with Django 1.9](http://www.tangowithdjango.com/) 搭配 [Django 官方文档](https://docs.djangoproject.com/en/1.11/)

---

# Halo, for you

程序员并不是那么神奇, 不会犯错

> Remember that everyone makes mistakes. Programmers are like magicians who fool everyone into thinking they are perfect and never wrong, but it's all an act. They make mistakes all the time.

有错就改, 则为上上策. 不断进步.

---

# Time log

    @Anifacc
    2017-03-29 ex1-ex11
    2017-03-30 ex12-ex15
    2017-03-31 ex16-ex20
    2017-04-01 ex21-ex28
    2017-04-02 ex29-ex32
    2017-04-04 ex33-ex37
    2017-04-05 ex38-ex41
    2017-04-06 ex42-ex45
    2017-04-07 ex46-ex47
    2017-04-08 ex48-ex49
    2017-04-09 ex50
    2017-04-10 ex50
    
---

[0]:    https://learnpythonthehardway.org/book/
[1]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex1.py
[2]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex2.py
[3]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex3.py
[4]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex4.py
[5]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex5.py
[6]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex6.py
[7]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex7.py
[8]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex8.py
[9]:    https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex9.py
[10]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex10.py
[11]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex11.py
[12]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex12.py
[13]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex13.py
[14]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex14.py
[15]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex15.py
[16]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex16.py
[17]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex17.py
[18]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex18.py
[19]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex19.py
[20]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex20.py
[21]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex21.py
[22]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex22.py
[23]:   https://learnpythonthehardway.org/book/ex23.html
[24]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex24.py
[25]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex25.py
[26]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex26.py
[27]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex27.md
[28]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex28.py
[29]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex29.py
[30]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex30.py
[31]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex31.py
[32]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex32.py
[33]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex33.py
[34]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex34.py
[35]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex35.py
[36]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex36.md
[37]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex37.py
[38]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex38.py
[39]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex39.py
[40]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex40.py
[41]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex41.py
[42]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex42.py
[43]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex43.py
[44_extra]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex44_extra.py
[44a]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex44a.py
[44b]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex44b.py
[44c]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex44c.py
[44d]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex44d.py
[44e]:   https://github.com/JeremiahZhang/gopython/blob/master/PY-The-Hard-Way/ex44e.py
[46]:   https://github.com/JeremiahZhang/gopython/tree/master/PY-The-Hard-Way/projects/skeleton
[47]:   https://github.com/JeremiahZhang/gopython/tree/master/PY-The-Hard-Way/ex47/skeleton
[48]:   https://github.com/JeremiahZhang/gopython/tree/master/PY-The-Hard-Way/ex48/skeleton
[49]:   https://github.com/JeremiahZhang/gopython/commit/109660e99512768be3cee70a1ebe08ae236ae77b
[50]:   https://github.com/JeremiahZhang/gopython/tree/master/PY-The-Hard-Way/web_projects/gothonweb