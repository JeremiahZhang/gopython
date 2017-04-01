# -*- coding: utf-8 -*-

# This one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok,that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothing."

print_two("Jeremy", "Anifacc")
print_two_again("Jeremy", "Anifacc")
print_one("First!!!")
print_none()

""" 

1. def 函数定义
2. 使用 _ 来定义名称 名称定义是给学问
3. 检查定义是否正确
4. 是否有 return 值

"""