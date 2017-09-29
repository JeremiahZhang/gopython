# Linear regression #

- [单变量线性回归](http://www.holehouse.org/mlclass/01_02_Introduction_regression_analysis_and_gr.html)  
- [多变量线性回归](http://www.holehouse.org/mlclass/04_Linear_Regression_with_multiple_variables.html)

## 1-单变量 ##

- 数据只包括一个特征值
- modeling:
	- 类似根据已知数据来拟合函数，有一个拟合函数，拟合函数又包括看书θo，θ1等
- cost function
	- 拟合函数中的参数θo，θ1等需要建立cost function来求解
	- Min cost function
	- 使用梯度下降法来寻找使得其值最下的参数θo，θ1....
	- 学习因子的影响
		- 太大，容易造成跌宕，不容易找到min
		- 太小，搜索太慢
		- 取值参考方法

## 2-多变量（多特征） ##

- 同上cost function
- 求解方法
	- 梯度下降
	- Normal equations method 矩阵解法
		- 不需要学习因子
		- 求解速度快
		- 但是比较复杂，又起来特征数比较多的情况下
	- 不可逆的情况解决
		- 处理数据特征：将相关性特征去除
		- 太多特征的话，删除一些特征

ppt文档学习回顾

9/9/2015 8:29:11 PM 
