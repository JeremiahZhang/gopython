# step by step #

- [x] dictionary dive in 官方help and [问题](http://stackoverflow.com/questions/17677523/python-keyword-output-interpretation)
	+ `dict{}` 
		+ 其中 key 顺序无关紧要
		+ 也有长度
		+ 排序好玩
	+ `key` 的熟悉
		+ dict.viewkeys
		+ dict.viewvalues
		+ 可删 
> 对dictionary熟悉了 只是在什么时候用 就不太清楚了

- [x] 4.7.3 Arbitrary Argument Lists
- [x] 4.7.4 Unpacking Argument Lists
- [x] 4.7.5. Lambda Expressions
- [x] 4.7.6. Documentation Strings
- [x] 4.8 Intermezzo: Coding Style
	- 使用4-space来缩进 而非tabs 得改
	- wrap lines 代码行长度不要超过79character 
		+ 就像matlab代码中 有一条竖线来提醒 要将代码控制在竖线左边
		+ 好读代码
	- [x] 空白行分割 函数 class 在函数内部等等
	- [x] comment 注释
	- 使用docstrings 在 4.7.6中提到
		+ 第一行 summary 精简
		+ 第二行 空行
		+ 第三行 writting
	- [x] 在 `=` `+` etc operators 与 `,` 之后使用空格
		- 这个已成习惯
			- 如 `a = 1`, `b = a`
		- 只是在用一个结构中 不需要就需注意了
			- `a=f(1,2)+g(3,4)`.
	- [] Name your classes and functions consistently
		- Always use self as the name for the first method argument 
	- [] Don’t use fancy encodings if your code is meant to be used in international environments. Plain ASCII works best in any case

代码在此 [2015-10-14 codes](https://github.com/JeremiahZhang/pybeginner/tree/master/_src/om2py0w/0wex3)

10/14/2015 10:40:03 PM 4+1蕃茄 but 3h