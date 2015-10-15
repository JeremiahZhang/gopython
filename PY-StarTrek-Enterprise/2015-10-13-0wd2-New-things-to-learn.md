# New Things to Learn #

- coding through [2.7.10 tutorial](https://docs.python.org/2/tutorial/)
- Something Learned
	- `if` statement
	- `for` statement
	- the `range()` function
		- `range(5, 10, step)` 值得注意的是取数乃是这样的 范围[ ) step 默认为1
		- `range()` 与list的结合 
			+ 简化为：`for i, v in enumerate(['Mary', 'had', 'a', 'litter', 'lamb']):`
	- `break` and `continue` statement
		- break 是哪里 打破 最近的 Loops
		- continue 又是继续的哪里 最近的 Loops
	- `else` 不要受制于 matlab 的`else` Python的`else`可用于Loops 
	- `pass` statement
	- Define functions 与c中的类似
		+ default argument values 
		+ Keyword arguments 这个比较鲜活

## 新知 ##
    
    def cheeseshop(kind, *arguments, **keywords):
		print '-- do you have any', kind, "?"
		print "-- I am sorry, we're all out of", kind
		for arg in arguments:
			print arg
		print '-' * 40
		keys = sorted(keywords.keys())
		for kw in keys:
			print kw, ":", keywords[kw]

	cheeseshop("limburger", "it's very runny, sir.", "It's really very, Very runny, sir.", shopkeeper = 'Michael Palin', client = 'John Cleese', sketch = 'cheese shop sketch')

- `*name01` 与 `**name02` 先后顺序
- 涉及 dictionary 还未细看 下一步着手 
- `keys = sorted(keywords.keys())`
- 看输出结果 

		-- do you have any limburger ?  
		-- I am sorry, we're all out of limburger  
		it's very runny, sir.  
		It's really very, Very runny, sir.  

		client : John Cleese   
		shopkeeper : Michael Palin  
		sketch : cheese shop sketch
	+ 明白
	+ 但是为什么呢？
		+ kind 参数 只能是第一个 "limburger"
		+ *arguments 参数 "it's very runny, sir.", "It's really very, Very runny, sir.
		+ **keywords 参数 其他剩余
	+ `keys = sorted(keywords.keys())` 不明白 进一步需要了解 Dic 再回来 看这个 confused codes
- When ?
- How to use them?

## Next##

- [] dictionary dive in 官方help and [问题](http://stackoverflow.com/questions/17677523/python-keyword-output-interpretation)
- [] 4.7.3 Arbitrary Argument Lists
- [] 4.7.4 Unpacking Argument Lists
- [] 4.7.5. Lambda Expressions
- [] 4.7.6. Documentation Strings
- [] 4.8 Intermezzo: Coding Style

----------

## SUM ##

- Coding 下去 
- 7个蕃茄学习 1个蕃茄整理
- 反思
	+ 代码练了 没有去完成一个项目 自定义的项目 发现还是不怎么入脑
	+ 那么的思考 完成一个 怎样有趣的项目 如同show me the code的 learn by doing
	+ 这么个循序渐进额可以

[今日代码](https://github.com/JeremiahZhang/pybeginner/tree/master/_src/om2py0w/0wex2)