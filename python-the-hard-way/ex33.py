# -*- coding: utf-8 -*-

"""
 while loop 
 
1. 尽量少用, 用 for loop 更好
2. 仔细检查 while loop 确保 有 False 结束, 莫要死循环
3. 若有疑问, 就将测试变量的起始和最后的结果打印出来,
看看发生什么.

"""

i = 0
numbers = []

while i <= 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += 2
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num