# -*- utf-8 -*-

print "Mary had a little lamb." # 输出字符串
print "Its fleece was white as %s." % 'snow' # 字符串输出形式
print "." * 10 # ten dot 十个点

end1 = "C" # 字符
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.
# try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, # 连接字符串
print end7 + end8 + end9 + end10 + end11 + end12

"""
1. line 22中最后 , 的作用是将 下一行 line 23 的输出连接在一起
	- 有, 则结果为 Cheese Burger 在一行显示
	- 没有 , 则结果为 
		Cheese
		Burger
		以两行显示
2. 字符串的连接

"""