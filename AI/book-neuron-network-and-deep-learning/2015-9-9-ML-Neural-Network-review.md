# NN #

- Why
	- 复杂的分类问题
		- Can not use Logistic Regression with many ploynomial terms
		- 特征比较多的时候呢？100个特征，一两个特征的可以用Logistic Regression
- Example
	- Problems where n is large - computer vision
- NN是模拟人脑的神经元及其处理
- Artificial neural network
	- layers
		- 输入层：dataset数据
		- 隐含层：
			- activation of unit
			- activative function： sigmoidal function
			- matrix of parameters
		- 输出层
	- 分类
		- 2 分类
		- k 分类 k>2
	- learning
		- cost function（所提公式比较复杂）
			- first half
			- second half（正则项）
		- learning by forward propagation
		- learning by propagation
- BP Algorithm
	- minimize cost function
		- gradient descent
		- advanced optimization algorithm
	- back propagation
		- 误差
		- 从最后向前推导每一层每个节点误差，用以计算代价函数对每个参数的偏导数
- gradient checking
- Random initialization

## 算法流程 ##

- 确定NN的结构
	- 输入节点数
	- 中间层数，中间层节点数
	- 输出层节点数：分类问题的类别个数
- 训练NN
	- 随机初始化权重（Small values near 0）
	-  Implement forward propagation to get hƟ(x)i for any xi
	-  Implement code to compute the cost function J(Ɵ)
	-  Implement back propagation to compute the partial derivatives
	-  Use gradient checking to compare the partial derivatives computed using the above algorithm and numerical estimation of gradient of J(Ɵ)
		-  当确定之后，需要关掉gradient checking
	- Use gradient descent or an advanced optimization method with back propagation to try to minimize J(Ɵ) as a function of parameters Ɵ

----------

## 实例练习 ##

> Implement the backpropagation algorithm for neural
networks and apply it to the task of hand-written digit recognition

- NN
	- Visualizing Data
	- model representation
	- feedforward and cost function
	- regularized cost function
- BP
	- sigmoid function gradient
	- random initialization
	- backpropagation
	- gradient checking
	- regularized NN
	- learning parameters using fmincg
- visualizing the hidden layer
- 准确率
	- 训练好θ之后
	- 进行分析预测查看准确率

----------

- 简单回顾了Andrew Ng的神经网络
- 但是还没有很好理解后馈的神经网络尤其是cost function
- 下一步继续深入研究神经网络

9/9/2015 10:43:00 PM 1  
9/10/2015 3:36:54 PM 2