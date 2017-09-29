# Improving the way neural network Note

第三章的学习笔记 主要内容:

- [x] 1 better cost functions
	- [the cross-entropy cost function](http://neuralnetworksanddeeplearning.com/chap3.html#the_cross-entropy_cost_function)
- [ ] 4 regulariztion methods 
	- L1
	- L2
	- dropout
	- artificial expansion of the trainning data
	> make our networks better at generalizing beyond the training data
- [ ] a better method for initializing the weights in the network
- [ ] a set of heuristics to help choose good hyper-parameters for the network
- [ ]  several other techniques

这么多技术怎么办

> The philosophy is that the best entree to the plethora of available techniques is in-depth study of a few of the most important. 

> Mastering those important techniques is not just useful in its own right, but will also deepen your understanding of what problems can arise when you use neural networks. That will leave you well prepared to quickly pick up other techniques, as you need them.

嗯 这么多资料怎么办 找到一本 dive in 

## 1.0 the cross-entropy cost function

### toy example

人类错误明显的时候 学习较快 而人工神经元却不是的  
神经元学习1: 初始权重 w 偏移 b 不同 学习因子eta为0.15

Chapter03_001_costfunction.jpg
Chapter03_002_costfunction.jpg

神经元学习2: 初始权重 w 偏移 b 不同 学习因子eta=0.15

Chapter03_003_costfunction.jpg
Chapter03_004_costfunction.jpg

前150步 神经元的学习慢

解释: 

- 代价函数(Toy example)

Chapter03_005_costfunction.jpg

其中a是神经元输出 y是目标理想输出 x=1， y=0  
代价函数值的变化 主要与以下两个偏导数有关 C对w和C对b的偏导数

Chapter03_006_costfunction.jpg

计算下可以得到以上两个式子  这2个偏导数的值主要看sigmoid函数的导数了

Chapter03_007_costfunction.jpg

当神经元输出越靠近1的地方 曲线越平坦 其导数的变化率是非常小的 也就是 sigmoid函数的导数小 从而式55 和 56 两个偏导数小 从而导致学习慢下来了

so 看【神经元学习2: 初始权重 w 偏移 b 不同 学习因子eta=0.15】中的初始迭代就非常的慢

> This is the origin of the learning slowdown. What's more, as we shall see a little later, the learning slowdown occurs for essentially the same reason in more general neural networks, not just the toy example we've been playing with.

在大多神经网络中 多是如此原因

### 交叉熵 代价函数 cross-entropy cost function

那么如何解决上面的问题呢？  
将代价函数 quadratic cost 改变为 cross-entropy

Chapter03_008_costfunction.jpg

#### 其特点

- 1 非负的 恩是的 观察一下 ln 函数图像 a = 0-1 而
- 2 如果 实际输出a 和 理想输出 y 非常接近 代价函数是趋近0的
	- y = 0, a-->0 看 C
	- y = 1, a -->1 看 C 

> These are both properties we'd intuitively expect for a cost function

好处呢 就是 避免在训练后期 学习速度变慢

> But the cross-entropy cost function has the benefit that, unlike the quadratic cost, it avoids the problem of learning slowing down. 

来看 C对 权重 w 和 偏移 b 的导函数

Chapter03_009_costfunction.jpg

这里 又因为 Chapter03_010_costfunction.jpg 得 

Chapter03_011_costfunction.jpg

这是一个非常好的表达式 偏导数值(变化率)由 输出误差 控制 

- 当误差大时 神经元学习也快 当误差小 学习也慢
- 这就避免了 上面 有 sigmiod导数 引起的学习慢的问题(在二次代价函数中)   

同样 对于 b 的偏导数 也是类似的

Chapter03_012_costfunction.jpg

再来看 使用 cross-entropy 代价函数后 其代价函数随迭代次数变化的情况:

Chapter03_013_costfunction.jpg

Chapter03_014_costfunction.jpg

这里 学习因子 eta = 0.005 和 起初的 0.15是不同的  
那么不同的代价函数一定要使用相同的学习因子么 实际中 代价函数也不一定非得使用相同的学习因子 eta 这如同 苹果和橘子放在一起比较了   
作者选用学习因子 使得观察代价函数的变化更直观些

> In particular, when we use the quadratic cost learning is slower when the neuron is unambiguously wrong than it is later on, as the neuron gets closer to the correct output; while with the cross-entropy learning is faster when the neuron is unambiguously wrong. Those statements don't depend on how the learning rate is set.

无关乎 学习因子的设置

- 多层神经网络的代价函数（上面的是单个的）

Chapter03_014_costfunction.jpg

什么时候使用 cross-entropy 来替代 quadratic cost: 大多时候使用 cross-entropy 以下是 why

> When should we use the cross-entropy instead of the quadratic cost? In fact, the cross-entropy is nearly always the better choice, provided the output neurons are sigmoid neurons. To see why, consider that when we're setting up the network we usually initialize the weights and biases using some sort of randomization. It may happen that those initial choices result in the network being decisively wrong for some training input - that is, an output neuron will have saturated near 11, when it should be 00, or vice versa. If we're using the quadratic cost that will slow down learning. It won't stop learning completely, since the weights will continue learning from other training inputs, but it's obviously undesirable.

#### 练习

- 公式问题 还好 只要将 y=0 or 1 带入就知道行不行了
-  [Binary entropy function](https://en.wikipedia.org/wiki/Binary_entropy_function) 还是挺好理解的 作者讲解之后 

在一些问题中 比如逻辑回归问题中（y在0-1之间） 但对于所有样本 a=y 时cross entropy直最小, 此种情况下 cross-entropy 可写成二进制形式

#### 问题

式 68-70 的证明 见纸质笔记

### 应用 MNIST digits

why 

- So why so much focus on cross-entropy?   

> Part of the reason is that the cross-entropy is a widely-used cost function, and so is worth understanding well. 

> But the more important reason is that ==**neuron saturation**== is an important problem in neural nets, a problem we'll return to repeatedly throughout the book. 

> And so I've discussed the cross-entropy at length because it's a good laboratory to begin understanding neuron saturation and how it may be addressed.

### more

- cross-entropy 理论[由来](https://en.wikipedia.org/wiki/Cross_entropy#Motivation)  [书籍推荐](https://books.google.ca/books?id=VWq5GG6ycxMC) 暂且先放着

- 问题？ 因为训练样本x无法通过cost function来选择

## [softmax layers of neurons](http://neuralnetworksanddeeplearning.com/chap3.html#softmax)

- 输出层的激活函数不同 之前用的sigmoid函数 现在使用 softmax函数如下

Chapter03_016_costfunction.jpg

- 练习
	- 单调性 证明见纸质笔记
	- Non-locality of softmax 因为随其他的zj变化
	-  inverting the softmax layer：两边对e的对数`ln`	就可以了

> In fact, it's useful to think of a softmax output layer with log-likelihood cost as being quite similar to a sigmoid output layer with cross-entropy cost.

> log-likelihood cost : c = -ln(a)

- 问题和练习证明未做

Wednesday, 13. January 2016 10:45AM 

## [overfitting_and_regularization](http://neuralnetworksanddeeplearning.com/chap3.html#overfitting_and_regularization) 




 

