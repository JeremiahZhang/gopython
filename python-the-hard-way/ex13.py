# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "argv[0] is: ", argv[0]
print "argv[1] is: ", argv[1]
print "argv[2] is: ", argv[2]
print "argv[3] is: ", argv[3] 

"""

1. 几个变量 在 是shell 中输入的就得几个变量.
2. script.py 整体是个变量
3. line 5 就像把argv 一个个分开, 赋予自己设定的变量中

    - 命令行中 **python ex13.py I Love Coding** 
    - 脚本名称 ex13.py 是一个参数, I, Love, Coding 分别是另外3个参数
    argv[0] = ex13.py
    argv[1] = I
    argv[2] = Love
    argv[3] = Coding

"""