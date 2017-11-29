# -*- coding: utf-8 -*-
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6  					# 正常的除数 
print "Roosters", 100 - 25 * 3 % 4 			# 100 - 75%4(取余数) 

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6  	# 6 - 5 + 0 - 0 + 6 有float, 则结果为float
											# see # line 32
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 -7 

print "Is it true that (3 + 2) < (5 - 7)" 	# line 12 和 line 15 的功能是一样的.
print (3 + 2) < (5 - 7) 					# python 自动将 左右两边各自先计算 再比较

print "Is it true that 3 + 2 <= 5 -7?"  
print 3 + 2 <= 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "after dot there is only one"
print 6.0 - 5.0 + 4 % 2 - 1 / 4 + 6 

print "after dot there are two number"
print 6.00 - 5.0 + 4 % 2 - 1 / 4 + 6   	# line 32 and line 35 结果相同

print 7.0 / 4.0
print 1.0 / 3.0							# 一个浮点数, 结果就是浮点数表示

"""

1. python  	用来做数学计算 也就是简单的 复杂的需要用 scipy
2. python  	计算顺序: 括号 指数 乘 除 加 减
3. %	   	取余数符号
4. python 	计算时的小数点根据 数据是整型 还是 浮点型 来判定的

"""