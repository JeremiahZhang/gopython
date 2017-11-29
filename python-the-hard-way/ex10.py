# -*- coding:utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat  
print fat_cat

# print "I love you\'re"
# print "Jesus\"love"
# print "Hello\a how are you"
# print "Fine\bthanks"
# print "What's \f that"

# print "Carrige\rxx__"
# print "Horizon\tTab"

while False:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i

print "\\"
print "\'"
print "\""
print "\a"
print "ab" + "\b" + "c" # 相当于删除ab 中的b（Backspace键盘上的）
print "Hello\fworld"
print "halo\nJesus"
# print u"\N{DAGGER}" # 不能输出
print "123456\rxx_xx" # xx_xx 取代\r前面的数,不足的则保留 xx_xx6
print "123\rxx_xx"
print "\t* hello" 	# tabbed 类似按tab键
print u"\u041b" 	# 16 bit Unicode 符号
# print u"\U000001a9"	# 32 bit unicode 符号
print "\043"		# 8进制值的 符号
print "\x23"		# 16进制值的 符号

print "%r" % "\\" 

'''

1 

error:
print u"\N{DAGGER}" # 不能输出
print u"\U000001a9"	# 32 bit unicode 符号

提示信息为：
UnicodeEncodeError: 'gbk' codec can't encode character u'\u01a9' in 
position 0: illegal multibyte sequence

2 
笨办法中的所有练习可以结合起来,解决问题, 这就是经验和能力的体现。

'''