# -*- coding: utf-8 -*-

# A comment, 目的 便于解读程序
# 任何 # 之后内容, python 都会忽略将其看作为代码

print "I could have code like this." # 这个注释是被忽略

# 使用 # 号 可以使 代码不运行 
# print "This won't run"

print "This will run."

"""

1. 中文注释后, 不加 # -*- coding: utf-8 -*- powershell 会报错

    > SyntaxError: Non-ASCII character '\xe7' in file ex2.py on line 1, 
    but no encoding declared; see http://python.org/dev/peps/pep-0263/ 
    for details

    加了之后, powershell 不会报错

2. # 后的注释, python 还是会以某种方式解读, 
    要不然不会出现 1 中的错误咯

3. 新技能get: 倒过来读代码, 快捷发现错误
    a handy error-checking technique

"""