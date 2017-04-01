# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10 # 字符串 + %d：数字
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) 
# 字符串 + % operator 使用 %s：字符
print x
print y

print "I said: %r." % x		# 输出 字符串 + % operator 使用
print "I also said: '%s'." % y	

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # 字符串 + % operator

print joke_evaluation % hilarious	# 字符串 + logic

w = "This is the left side of..."	# 字符串
e = "a string with a right side."

print w + e 	# 字符串连接