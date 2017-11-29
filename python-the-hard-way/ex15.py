# -*- coding: utf-8 -*-

from sys import argv

# 使用 argv 形式来打开文件，并阅读 
script, filename = argv # pass the para to argv and unpackage to script and filename

txt = open(filename) # open file 

print "Here's your file %r: " % filename # output information
print txt.read() # read content of filename.txt file

txt.close()

# 使用 raw_input 形式来打开文件, 并阅读
print "Type the filename again: " 	# output information
file_again = raw_input("> ")		# input file name

txt_again = open(file_again)		# open file again

print txt_again.read()				# print content of file

txt_again.close()

"""

1. 使用 python 打开 需要注意路径 比如
	path = 'C:\\users\\we\\ex15_sample.txt'
	f = open(path)
	f.read()
	f.close()

2. 路径问题, 就到设计到模块 os

"""