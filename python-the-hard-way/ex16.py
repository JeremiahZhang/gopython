# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# first print file contents

f = open(filename, "r") # opens file with name of "test.txt"
print (f.read(1)) # read only one characters
print (f.readline())# read the one line (include the first line)
print (f.read())  # read the remain of the file
f.close()

# trickery
f = open(filename, "r")
my_list = []
for line in f:
	my_list.append(line)

print (my_list)
f.close()

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."

target = open(filename, "w")

# origin_content = target.read()
# print "Here are the original contents: %s" % origin_content

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close

"""

1. file = open(filename, mode) # 打开文件, 打开方式可以定义
2. file.read()  读取文件, 全部内容
3. file.readline()  一行一行读取文件内容
4. file.truncate() 删除文件内容  
5. file.write() 写入文件内容

注：line 9-12 行, Python 是比较懒的 它记得自己读到哪儿, 
	下次再读的时候, 就继续在原来读到的位置后继续.

6. 最后, 请别忘记 close 关闭文件

7. 既然 open file 时 使用了 “w” 因此 没有必要再使用 file.truncate

because: "w" 本身就删除原有内容

 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.

"""