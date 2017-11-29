# -*- coding: utf-8 -8-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly: "
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

""" 

1. 注释每一行代码
2. 倒读代码,
3. 变量在函数中的使用：
	- 1 argument 形式 	line 3
	- 2 赋值形式： 		line 13-16
	- 3 直接输入： 		line 10
	- 3. math: 			line 19
	- 5. 混合： 		line 22
4. 函数中的参数最好不要超过 5个

"""