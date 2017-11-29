# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)   # 打开被copy的文件
indata = in_file.read()		# 被copy 文件的内容读取

print "The input file is %d bytes long" % len(indata) # 被copy文件中的内容大小

# print "Does the output file exist? %r" % exists(to_file) # 看 to_file 文件存在不
# print "Ready, hit Enter to continue, CTRL-C to abort." 
# raw_input()

print "Now we are going to copy %r to %r" % (from_file, to_file)

out_file = open(to_file, 'w') # 如果文件不存在, 则建立新文件
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

"""

1. open file
2. read file
3. 查看文件存在不？
4. open file
5. write file

""" 