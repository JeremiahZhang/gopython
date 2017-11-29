# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # %r 可带入数字
print formatter % ("one", "two", "three", "four") # %r 可带入字符
print formatter % (True, False, True, False) # %r 可带入 布尔值
print formatter % (formatter, formatter, formatter, formatter) # % formatter还是字符串
print formatter % ( \
					"I had this thing.", \
					"That you could type up right.", \
					"But it didn't sing.", \
					"So I said goodnight.", \
					) # %r 带入字符串

"""

1. 所放的错误： 在 line 11 以下, 字符串最后, 都忘记用 , 号分隔开了
2. \ 表示换行 （自己添加的）
3. %r 如何使用
4. 最后line 9 的输出结果为：

	'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
	
	是这的形式的, 为什么呢？

	str() 是给人读的 is meant to return representations of values which are fairly human-readable
	repr() 表示成解释器可读形式 is meant to generate representations which can be read by the interpreter
			这个输出的基本就是所有字符形式
			hello = 'hello, world\n'
			hellos = repr(hello)
			print hellos
			输出： 'hello, world\n'
		包括了 \n
"""