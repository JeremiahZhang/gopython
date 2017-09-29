# BP-NN #

- 矩阵方式 计算更快 matlaba fast matrix-based algorithm to compute the output from a neural network
- 2 assumptions of cost function
	+  均方误差 MSE 系数为什么有1/2 在GD计算中 求导后 正好2*1/2 将系数化为1 数学上的处理方便
	+  Cost Function 是 output `a`的函数 也就是 权值`w`与偏差bias`b`的函数
- BP Prepare
	+ an intermediate quantity: the error in the `j-th` neuron in the `l-th` layer 第l层 第j个神经元or节点处的误差 Backpropagation will give us a procedure to compute the error δlj
	+ BP 方程4骑士 t he four fundamental equations
	+ **Proof**
- BP Algo
	- BP
	- BP+GD learning 学习

> - Backpropagation is about understanding how changing the weights and biases in a network changes the cost function.
> - The backpropagation equations provide us with a way of computing the gradient of the cost function

## 图形+公式 回顾 ##

- denote
	+ 权重  
![weight](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/01-denote.JPG)
	+ 神经元  
![neurons](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/02-Neurons-denote.JPG)
	+ 公式   
		+ 神经元节点计算
![节点计算公式](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/03-formula-23.JPG)    
![matrix](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/04-formula-25.JPG)    
		+ 权重输入  
![权重输入](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/05-zl-the-weighted-input.JPG)  
		+ 代价函数 （利用代价函数 判断拟合或算法效果怎么样）  
![代价函数](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/06-formula-26.JPG)
			* 为什么是2为了数学上计算的方便
- BP中最重要的 error     
![errormetaphor](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/07-error-metaphor.JPG)
	+ 为什么会有error呢？自我解答： 每一个阶段都是数值上的模拟 不是最理想的 当然会出现error 要不 百分百准确了
- BP 4骑士方程（自取的 nickname）
	+ l层的error
	+ 倒推 前一层 前前一层等的 error
	+ cost function 对权重`w`的偏导
	+ cost function 对bias的偏导
	+ 证明 见纸质笔记  
![重要的4骑士方程](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/08-Eq-4-Knight-to-UnderstandBP.JPG)
- BP Algorithm step by step
	- input x 样本 x
	- 前向传播进行
	- 输出层output layer 节点error
	- backpropagate 后馈计算前面各层节点 error
	- output 代价函数梯度对 权重与bias
![BPALGO](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/09-BP-Algo.JPG)
- BP + GD 结合 进行 学习 （神经网络的学习等）
	- 训练集 training examples
	- 对每个训练样本 进行 for i in training examples
		- feedfordward 前向传播
		- output error 输出层节点误差
		- backpropagate 后馈得到各层节点误差
	- 梯度下降 更新权重（使用的是BP中的最后2个骑士方程）
![BP-GDlearning](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/BP-NN/10-BP-GD-Learning.JPG)

学习BP学习算法 明白BP算法的过程及其原理 作者讲得真不错

## BP the big picture

- 参考[backpropagation_the_big_picture](http://neuralnetworksanddeeplearning.com/chap2.html#backpropagation_the_big_picture) 

假设有一个权重产生一点变化 会影响最后的输出C  
但是这个整个过程计算是复杂的如

![1权重微小变化](https://dn-learnml.qbox.me/bp01w.png) 

权重微小变化引起 中间神经元激励 a的变化

![2中间神经元微小变化](https://dn-learnml.qbox.me/bp02w.png) 

![3后续中间神经元微小变化](https://dn-learnml.qbox.me/bp03.png) 

![4对输出的影响](https://dn-learnml.qbox.me/bp04.png) 

方程:

![5c输出影响方程](https://dn-learnml.qbox.me/bp05.png) 

![6激励影响方程](https://dn-learnml.qbox.me/bp06.png) 

表示

![7激励](https://dn-learnml.qbox.me/bp07.png) 

公式

![8激励传递影响](https://dn-learnml.qbox.me/bp08.png) 

![9于w关联](https://dn-learnml.qbox.me/bp09.png) 

输出C受的影响变化表示

![10c的变化](https://dn-learnml.qbox.me/bp10.png) 

![11所有传递过来的](https://dn-learnml.qbox.me/bp11.png) 

输出C对中间权重 w的偏导数

![12 偏导数](https://dn-learnml.qbox.me/bp12.png) 

![13 传递](https://dn-learnml.qbox.me/bp13.png) 

恩 其实BP算法就是求 将公式53 只是使用一种后馈的方式 更简洁方便求得相关偏导数 进行GD的计算

主要就是BP的4骑士方程了

## 后续

- 代码
	- [x] GD-NN python代码
	- [x] BP-NN python代码  

10/15/2015 7:44:07 PM 7 + 1蕃茄
Monday, 28. December 2015 02:33PM Python code
