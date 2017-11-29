# -*- coding: utf-8 -*-

# 0 说明 与 注释

"""

1. 这里存放的是文档, or 函数的说明
	一般在 def 函数下 会有 doc 文档说明
	可以通过 func.__doc__ 调用

2. "#" 加井号是用来注释的
	python 不会将 "#"
	后面的看看作为 代码, 但是 python 也会读
	"# 后面的内容 

3. # -*- coding: utf-8 -*-
	Defining Python Source Code Encodings

4. pydoc sys
	使用 pydoc 查看 obj function 等的说明

"""

# 1 variables and strings
## 变量 存储数据: 字符, 数字等
## 字符串由字母组成, 汉字也可以, 得用 "" 或 '' .

## halo world
print "Halo World!"
print("Halo world!")
## variables
msg = 'Halo world!'
print msg
print(msg)
print "First Program is", msg

## Concatenation 字符串连接
first_name = "Jeremy"
last_name = "Anifacc"
full_name = first_name + " " + last_name

## format %r %d 格式输出
### 不同的数据形式要对应不同的格式
### 其他 转义字符 的使用 \r \t \n \' \'' \\ 等等
print "%s is the first paragraph that every programming language would say" % msg

# 2 math 

a = 1
b = 2
sum_a_b = a + b
print "the sum of %d and %d is %d" % (a, b, sum_a_b)

# 3 User input 用户交互
## 让用户与计算机交互, 任何输入被保存为 string 形式
## Prompting for a value, 存储为 string
name = raw_input("what's your name?>>>")
print "Halo, " + name + "!"
## Prompting for numerical input, string ---> int
age = raw_input("How old are you?>>>")
age = int(age)
print "Your age is %d" % age

pi = raw_input("What' the value of pi?>>>")
pi = float(pi)
print "The value of pi is %f" % pi

# 4 Command line 参数传递
from sys import argv

script, first_parameter = argv
print "The script name is %s" % script
print "The parameter transferred is %s" % first_parameter

# 5 Functions 函数定义
## 5.1 简单的函数
def greet_user():
	"""
	Display a simple greeting.
	"""
	print "Halo! Python"

greet_user()

## 5.2 参数传递
def greet_user_2(username):
	"""
	Display a personalize greeting.
	"""
	print "Halo, %s !" % username

greet_user_2(name)

## 5.3 函数中设置默认参数
def make_lunch(material="egg"):
	"""
	Using material to make lunch
	"""
	print "Have a nice %s lunch!" % material

make_lunch()
make_lunch('tomato')

## 5.3 return 函数返回值
def add_numbers(x, y):
	"""
	add two numbers and return the sum
	"""
	return x + y

sum = add_numbers(4, 5)
print sum

# 6. Files 文件读写
## 文件的 读 和 写
## read mode "r" "w" "a"
## 6.1 读文件, 并存下每一行
file_name = 'test.txt'
with open(file_name) as file_object: 	# with open() as f
	lines = file_object.readlines()		# 这是小技巧,不用 close()

for line in lines:
	print line,

## 6.2 写入文件, 覆盖掉以前的内容
file_name = 'journal.txt'
with open(file_name, 'w') as file_object:
	file_object.write("I love programming!")

## 6.3 在文件基础上继续写入内容, 不会覆盖掉以前内容
file_name = 'journal.txt'
with open(file_name, "a") as file_object:
	file_object.write("\nI love python programming!")

## 6.4 copy file in one line
# from sys import argv
# import shutil

# script, from_file, to_file = argv


# f = open(to_file, "w+")
# f.truncate()
# print "The content of to_file: %r" % (f.read())
# f.close()

# shutil.copy(from_file, to_file) # This is one line

# f = open(to_file, "r")
# print "The content of to_file now: %r" % (f.read())
# f.close()