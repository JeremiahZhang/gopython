# Using neural nets to recognize handwritten digits #

[学习章节](http://neuralnetworksanddeeplearning.com/chap1.html)

- 神经元
	- Perceptrons
	- Sigmoid Neurons
- 神经网络结构
- 神经网络学习 
	+ gradient descent
		+ Stochastic GD Applied in recognition
		+ Batch GD 

----------
## 神经网路 ##

- 什么是[人工神经网络](https://en.wikipedia.org/wiki/Artificial_neural_network)(artificial neural network，缩写ANN)？
- 它是用来干什么的？
- 如何使用它？

人工神经网络模拟人脑的神经网络 但是大大的简化了 所以称之为人工神经网络

来看看人脑神经网络

![NN-1](https://ilaif.files.wordpress.com/2015/02/neural-network.jpg)

简化

![NN-2](http://1.bp.blogspot.com/-ewmhj_UedLs/VEIhLPJsRkI/AAAAAAAAAAs/PGuuX9wn1mg/s1600/neuron.png)

ANN是用来干嘛的？

人类大脑可以处理负责的事物 我日常学习 做决策需要神经元的作用 有时 我做的决策比较好 有时不然 那么ANN模拟人脑 也可以进行“学习” “决策”
虽然达不到人类的效果 但是可以辅助人 

- 学习
- 决策 

## 神经元 ##

- Perceptrons
- Sigmoid

### Perceptrons ###

处理需要神经元 ANN中的常见神经元为以上两种

Perceptron 感知器 比较简单 如图所示

![perceptrons](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-Perceptrons.JPG)

公式:
![formula-1](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-formula1.JPG)
![formula-2](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-formula2.JPG)
b = - threshold

理解

- 每一个输入`x`都伴随着一个权重`w` 同时由一个阈值threshold来决定输出结果  
- 感知器神经元的`input` x 要么为0 要么为1 （二进制输入） 输出也是0 or 1
- 这可以用来做决策 yes(1) or no(0), life(1) or death(0)? etc
	+ 例子 我目前在广州 2015年12月12日孙燕姿正好要在天河体育馆开一场演唱会 假如以感知器来模拟我要不要去
		- input 1 x1 现在喜欢孙燕姿么？ 权值 我对燕姿的喜欢程度 影响份量 w1 = 4
		- input 2 x2 天气好我就去 不好就不去？ 权值 w2 = 2
		- input 3 x3 地铁直达不？ 权值 w3 = 2
		- 阈值为 threshold = 3 
		- 通过公式计算 x1`*`w1 + x2`*`w2 + x3`*`w3 > or <= threshold
		- 只要我现在喜欢孙燕姿（不论天气好坏还是地铁直达与否）or（天气好+地铁直达）那么 我肯定会去了
	+ logical 电路确定
		+ AND NAND OR 等

嗯 以上就是简单的感知器神经元 神经网络的每个神经元若采用感知器神经元 那么每一次的output都是如公式2决定 以下为3层神经网络
![Perceptrons-NN](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-Perceptrons-NN.JPG)

其实也就是说 上面神经网络中每个神经元通过公式2来决定输出的情况 那么 公式2就可当作是激活神经元的一个函数(activation function)。

Sigmoid神经元与Perceptron神经元的区别就在于这个激活神经元的激活函数activation function  
Perceptron的激活函数 为一个阶跃函数 公式 2

![Perceptron-PIC](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-Perceptron-PIC.JPG)

### Sigmoid ###

激活函数：

![formula-3](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-formula3.JPG)
![formula-4](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-formula4.JPG)
![Sigmoid-PIC](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-Sigmoid-PIC.JPG)

sigmoid神经元的输入可以是0-1间的任意数 而输出也是0 1了   
但可以人为设定 函数值output >= 0.5 的为1 < 0.5的则为0

### 两者差别 ###

![diff](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-diff.JPG)
![formula5](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-formula5.JPG)

权值或bias的微小变化 对 output 造成微小的影响 若是近线性的 就比较好反馈学习了  
在perceptron中 从激活函数-阶跃函数中 看出 输出结果是0 or 1 所以结果是阶跃or跳跃的 w或bias的影响造成的结果可能不是那微小的变化 而是“质”的变化   
在sigmoid神经元中 sigmoid函数比阶跃函数光滑了 输出△oupute近似是随△w与△b线性变化了 这样在学习过程中 可根据学习结果 来对w与b进行调整 学习了

为什么使用sigmoid 因为e的求导很特别 为了数学计算上的便利性

----------

## 神经网络结构 ##

- 输入层 神经元数目（节点数）为样本维数
- 中间层 层数与神经元数目根据学习来调整 一般采用启发式算法来优化决定
- 输出层 神经元数目根据需要检测的结果确定

![structure](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/NN-structure.JPG)

----------

## 神经网络学习  ##

### Gradient Descent ###

- 代价函数（cost function）
	- 要使代价函数最小（拟合最好or 权值与b在训练中效果比较好使得output结果误差较小or判别的准确率较高）在Ng的讲解中就可以理解了
	- 采用GD gradient descent 梯度下降法
- 什么是GD
	- 介绍
	- 公式  
![GD-formula](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/gd-formula.JPG)
		+ 其中`θ0`为bias b， `θ1`.为权重w 只是写法不同 `J()函数` 为 cost function
	- 落球寻找最小值的比喻非常好 加深理解  
![GD](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/GD.JPG)
		+ 当学习因子α过小 会造成小球经过低谷后又向上爬
		+ 当学习因子α过小 会造成小球下落过慢 （当然这里不考虑重力势能）
- Stochastic GD（随机选取样子中一些样本进行梯度计算 搜索w 与 b）
- Batch GD （使用所有样本计算梯度w 与 b）

通过GD 计算权重`w` 与bias `b`（不同教材中表示不一样 如NG的MachineLearning课程汇中用`θ0`表示权重与`θi`表示bias）知道Cost function 值最小（如果说是拟合函数的话 那么参数的拟合效果较好 误差最小）

详见 纸质笔记

10/14/2015 4:32:57 PM 3蕃茄

## 代码理解算法

[network.py](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/src/network.py) 代码结构

	- Class Network
		+ __init__ 初始化基本参数
			- 神经网络层数
			- 权重 w
			- b-biases 偏差
		+ feedforward # 前向计算 恩 计算各层每个神经元
			- 调用 sigmoid fun
		+ SGD		# 随机梯度下降
			- 调用 update_mini_batch
		+ update_mini_batch # 使用小样本 进行更新 权重和 biases偏差
			- 得调用 backprop 计算
		+ backprop # 嗯 这就是后馈 来进行 w 和 b 的更新 梯度下降嘛  [第二章有介绍](neuralnetworksanddeeplearning.com/chap2.html) 
			- cost_derivative
			- sigmoid_prime fun
		+ evaluate # 评估 训练结果
		+ cost_derivative # 代价函数的求导
	- sigmoid fun
	- sigmoid_prime fun # sigmoid 求导

恩 使用

	import network # 导入
	net = network.Network([784, 30, 10]) # 784 为第一层输入层 30为第二层 10为输出层
	net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

恩 记得在Andrew的课程中 学习因子eta的影响还是挺大的 Andrew老师 给出了自己一般如何选择 eta 的经验

理解了结构 主要是 w*a+b 这个矩阵形式处理 恩 看代码可以更好理解 NN 进入下一张 BP的复习 继续 GO

Thursday, 26. November 2015 01:42PM 



