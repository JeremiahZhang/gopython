# 那42行

## 现象 ##

- 根据 [极简Python上手导念](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart) 中的一页解说了 Python 代码
	- ![42 coder](http://wiki.woodpecker.org.cn/moin/ZqQuickIntoPy?action=AttachFile&do=get&target=coffeeghost-q-in-py.png)
- 会解说了 但是如何去运用 将其功能化呢？
- 这42行代码：
	+ 包含80%左右的 py 代码常见情景
		+ 常见情景是什么？
			+ main 函数 调用 循环 print 等等
	+ 是不是类似 欧式几何 中 那些 定义 公设 公理 
		+ 用**常见情景**（定义 公设 公理） 去 实现（证明）其他功能（命题）呢？


----------

## 问题 ##

任务是 将那42行 功能化  

- 那么如何去功能化？ （ 用怎么去证明其他命题思路去想）

## 分析 ##

- 什么功能化？
	+ 总要确定命题 才能证明吧
	+ 寻找 探寻
- 如何实现？
	+ 参考 运用 那 42行代码

## 方案 ##

- 构思功能
- 去实现功能
- 教程
	+ 功能设计
	+ 技术要点
	+ 实现难点
	+ 涉及知识
	+ etc

----------

## 执行  

- 构思功能 
	+ 到底是什么功能呢？
	+ 视野不广 去扩宽
	+ 知识不够 去学习
	+ github 是个好地方 小程序功能去找 find this repo [Show me the code](https://github.com/Show-Me-the-Code/python)
	+ OK show me the code as Linus says
	+ 题目：[0000](https://github.com/JiYouMCC/python-show-me-the-code/tree/master/0000)
	> 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
- 构思过程
	+ 思维导图
- 执行
	+ code [the code](https://github.com/JiYouMCC/python-show-me-the-code/blob/e0c7c1c37ccba38671078e0b0ff6238992a11499/0000/0000.py)
	+ Python Image Library install
	+ choose and install [Pillow 3.0.0](https://pypi.python.org/pypi/Pillow/2.2.1) 由此参考回答[Installing PIL with pip](http://stackoverflow.com/questions/20060096/installing-pil-with-pip)对于小白的我 这个需要使用命令行 我用babun

			$ pip install Pillow
		+ 安装之后如何使用呢？因为只有`from PIL import Image`是没有用的 error 显示找不到图片 搜了好多 最后在此处 [The Image Module](http://effbot.org/imagingbook/image.htm) 发现答案 【先从help -> google key word is very important】
		+ 没有在当前工作目录中 放入所用的图片【掉入的坑 好久才爬出来 适当休息】
			+ 图像是在当前工作目录中的
			+ save 的也是
			+ 关于Image可以在[这里](http://effbot.org/imagingbook/image.htm)找到help
	+ run successed as below
		+ ![narresult](https://raw.githubusercontent.com/JeremiahZhang/pybeginner/master/_src/om2py0w/0wex1/nar_result.png)
+ 收获
	+ 库的安装 使用 及其查询
		+ PIL Python Image Library Pillow
		+ the image module
	+ help 文档检索为先
+ 总
	+ 在运行别人的代码
	+ 发现问题 自己理解
	+ 但是如何去自行编码独立完成呢？ 需要一步步积累

代码：[https://github.com/JeremiahZhang/pybeginner/tree/master/_src/om2py0w/0wex1](https://github.com/JeremiahZhang/pybeginner/tree/master/_src/om2py0w/0wex1 "今日代码")

10/11/2015 3h