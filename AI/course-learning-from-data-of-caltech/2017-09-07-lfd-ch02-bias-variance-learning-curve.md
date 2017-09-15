---
layout: post
title: LFD第二章笔记:Bias-Variance-Learning-Curve
categories:
- MachineLearning
- LearningFromData
---

从书本的泛化误差[VC 分析](https://anifacc.github.io/machinelearning/learningfromdata/2017/08/31/lfd-ch02-generalization-bound-interpretion-test-set/), 我们了解假设集 $$\cal H$$ 的选择既要考虑在训练集上与目标函数 $$f$$ 相近---$$E_{in}$$ 要小, 又要考虑其泛化能力, 在输入空间中的其他数据上的识别或预测性能要好 --- $$E_{out}$$ 要小.

现实中, 我们不可能找到一个假设集中正好只含有目标函数. 这太理想, 比中500万的彩票还难. (哈, 趁早放弃, 踏实学习. 学过概率的都不会去买彩票, 这是理性, 有时候感性一下, 买张彩票, 相信自己能中, 简直痴心妄想.)  因为现实中的目标函数未知, 只能从"采集"到的数据中分析窥探其一二. 实际学习中, 我们通过训练确定的一个好的假设, 既要接近目标函数, 又要在其他数据上"奏效".

我们可利用 VC泛化边界来理解上面的"对立协调(trade-off)"情况: 如果假设集 $$\cal H$$ 太简单, 在训练集上的效果就差 $$E_{in}$$ 大; 如果假设集 $$\cal H$$ 太复杂, 则泛化能力不好, $$E_{out}$$ 大.

还有另一种方式来考察. 这就涉及本节需要讲述的内容:

- Bias and Variance 偏差与方差
- The Learning Curve 学习曲线

---

## 1.Bias and Variance

首先是 bias-variance 分析, 将 out-of-sample error (误差平方) 分解.

$$E_{out}(g^{(D)}) = \Bbb E_x \lbrack \lgroup g^{(D)}(x) - f(x) \rgroup ^2\rbrack$$

其中 $$g^{(D)}$$ 表示算法基于数据集(训练集) $$\cal D$$ 得到的最终假设; $$\Bbb E_x$$ 表示: 输入空间 $$\cal X$$ 数据 $$x$$, 学习得到最终假设在数据 $$x$$ 上的结果 $$g^{(D)}(x)$$ 与目标函数 $$f(x)$$ 误差平方的期望值. 这容易理解. 关键是下面的处理得到 bias 和 variance.

$$\begin{align}
\Bbb E_D \lbrack E_{out}(g^{(D)})\rbrack &= \Bbb E_D \left[ {\Bbb E_x \left[ \lgroup g^{(D)}(x) - f(x) \rgroup ^2\right]} \right] \\
  &= \Bbb E_x \left[ {\Bbb E_D \left[ \lgroup g^{(D)}(x) - f(x) \rgroup ^2\right]} \right] \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 \rbrack - 2 \Bbb E_D \lbrack g^{(D)}(x) \rbrack f(x)  + f(x)^2 \right] \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 \rbrack - 2 \bar g(x) f(x)  + f(x)^2 \right], where \ \Bbb E_D \lbrack g^{(D)}(x) \rbrack = \bar g(x) \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 \rbrack - \bar g(x)^2 + \bar g(x)^2 - 2 \bar g(x) f(x)  + f(x)^2 \right] \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack (g^{(D)}(x) - \bar g(x))^2 \rbrack + (\bar g(x) - f(x))^2  \right]
\end{align}$$

其中 $$\Bbb E_D \lbrack g^{(D)}(x) \rbrack = \bar g(x)$$, 从数据集D下得到的假设 $$g^{(D)}$$ 期望值以"均值函数"表示(大数定理是趋近的). 也可以这么理解: 有 K 个数据集 $$D_1, D_2, ..., D_K$$, 在这些数据集下, 我们得到最终的假设分别为 $$g_1, g_2, ..., g_K$$, 那么可令

$$\bar g(x) \approx \frac{1}{K} \sum_{k=1}^{K}g_k(x)$$

即 K 个数据集上得到的假设的平均值, 约等于期望值(大数定理).

本质上来讲, $$g(x)$$ 是个随机变量, 其随机性来自于数据集 D 的随机性; $$\bar g(x)$$ 就是这个随机变量的期望值 ( x 固定). 对于 数据集 D 而言, $$\bar g(x)$$ 是个常数.

**Bias**: 上式出现 Bias, 其定义为:

$$bias(x) = (\bar g(x) - f(x))^2$$

**Variance** 定义为

$$var(x) = \Bbb E_D \left[ (g^{(D)}(x) - \bar g(x))^2 \right]$$

所以有

$$\begin{align}
\Bbb E_D \lbrack E_{out}(g^{(D)})\rbrack &= \Bbb E_x \left[ bias(x) + var(x)\right] \\
  &= \ bias + \ var
\end{align}$$

Out-of-sample error $$E_{out}(g^{(D)})$$ 是基于数据集训练得到的最终假设 $$g^{(D)}(x)$$ 与目标函数 $$f(x)$$. 其样本 $$x$$ 来自于输入空间. 因为最终假设确定后, 目标函数也"确定"(虽然我们不知道它到底是什么), 这样在整个输入空间求误差平方的期望值.

$$\Bbb E_D \lbrack E_{out}(g^{(D)})\rbrack$$: 不同的训练集 D 会产生各自的最终假设 $$g^{(D)}$$, 再求上面期望的期望, 就得到

$$\begin{align}
\Bbb E_D \lbrack E_{out}(g^{(D)}) \rbrack &= \Bbb E_x \left[ bias(x) + var(x)\right] \\
  &= \Bbb E_x [bias(x)] + \Bbb E_x [var(x)]\\
  &= \ bias + \ var
\end{align} \tag{1}$$

其中 $$bias = \Bbb E_x [bias(x)], var = \Bbb E_x [var(x)]$$.

上面推演的前提: 数据没有噪声的影响. 如果有噪声影响, 那么结果会怎么样呢?

参见问题 problem 2.22:

> When there is noise in the data, $$ E_{out}(g^{(D)}) = \Bbb E_{x,y} \lbrack (g^{(D)} - y(x))^2\rbrack, y(x) = f(x) + \epsilon$$. If $$\epsilon$$ is a zero mean noise random variable with variance $$\sigma^2$$, show that the bias variance decomposition becomes:

> $$\Bbb E_D[E_{out}(g^{(D)})] = \sigma^2 + \ bias + \ var$$

按上文的分析来分解:

$$\begin{align}
\Bbb E_D[E_{out}(g^{(D)})] &= \Bbb E_D \lbrack \Bbb E_{x,y}[(g^{(D)}(x) -y(x))^2]\rbrack \\
  &= \Bbb E_{x, y} \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 - 2g^{(D)}(x)y(x) + y(x)^2\rbrack \right] \\
  &= \Bbb E_{x,y} \left[ \Bbb E_D \left[ g^{(D)}(x)^2 - 2g^{(D)}(x)f(x) + f(x)^2 - 2g^{(D)}(x) \epsilon + 2f(x) \epsilon + \epsilon^2 \right] \right] \\
  &= \Bbb E_{x,y} \left[ \Bbb E_D \left[ g^{(D)}(x)^2 - 2g^{(D)}(x)f(x) + f(x)^2 \right] - \Bbb E_D [2g^{(D)}(x)\epsilon] + \Bbb E_D [2f(x)\epsilon] + \Bbb E_D [\epsilon^2] \right] \\
  &= \Bbb E_{x,y} \left[ \Bbb E_D \left[ g^{(D)}(x)^2 - 2g^{(D)}(x)f(x) \right] \right] + \Bbb E_{x,y} \left[ - 2 \bar g(x) \Bbb E_D[\epsilon] + 2 f(x) \Bbb E_D[\epsilon] + \Bbb E_D [\epsilon^2] \right] \\
  &= bias \ + \ var + \Bbb E_{x,y} \left[ \Bbb E_D [\epsilon^2] \right] \\
  &= bias \ + \ var + \Bbb E_D \left[ \Bbb E_{x,y}[\epsilon^2] \right] \\
  &= bias \ + \ var + \sigma^2
\end{align}$$

因为 $$\Bbb E_D[\epsilon] = 0, \Bbb E_{x,y}[(\epsilon-0)^2] = \sigma^2$$

所以得到上面的分解结果.

上式(1), 在多个数据集D上计算期望, 对实践有什么意义呢? 单纯为了将其分解为 bias 和 variance 嘛? 现实中, 我们不是只要考虑 out-of-sample error $$E_{out}(g^{(D)})$$ 就行了么? 考察其期望, 是否更能理解 out-of-sample error? 期望: 看平均表现.

**Bias-variance decomposition**

上面推演将 out-of-sample error 分解为 bias 和 variance. 两种极端情况距离, 请参考书籍P64内容-Very small model 和 Very large model.

(1) 从 bias 定义来看, bias(x) 是衡量输入空间内 $$\bar g(x)$$ 和目标函数 $$f(x)$$ 的误差. (2) 从 variance 定义来看, var(x) 是衡量数据集D得到的最终函数在输入空间上的结果 $$g^{(D)}(x)$$ 与均值 $$\bar g(x)$$ 的差距. 我们可以将 variance 作为学习模型的"非稳性(instability)"的度量. 数学上的"方差", 观察差异程度.

书中 **Example 2.8** 举例讲述 bias 和 variance, 简单易懂.

- 目标函数 $$f(x) = \sin(\pi x)$$
- 数据集D样本个数 N = 2
- 输入空间 X 的 x: [-1, 1] 随机均匀分布产生随机数, 得到$$(x_1, y_1), (x_2, y_2)$$
- 2个学习模型:
  - $${\cal H_0}: h(x) = b, b = \frac{y_1 + y_2}{2}$$, 两训练样本确定, 就可得到假设
  - $${\cal H_1}: h(x) = ax + b$$, 通过两个训练样本的直线.
- 产生好多组训练集 D, 计算 bias 和 variance.

如下图所示, 不同的数据集, 产生的假设.

![hypothesis](https://dn-learnml.qbox.me/image/ai/lfd_ch02_ex28_hypothesis.JPG)

得到的 bias 和 variance 图形显示如下.

![bias-variance](https://dn-learnml.qbox.me/image/ai/lfd_ch02_ex28_bias_variance.JPG)

上图中的直线为 average hypothesis $$\bar g(x)$$, 阴影部分区域为 $$\bar g(x) \pm \sqrt{var(x)}$$

模型 $${\cal H_1}$$ 的平均假设 $$\bar g$$ 拟合目标函数的bias 为0.21, 偏差比模型$${\cal H_0}$$的0.50小, 但是前者的 variance 为1.69 远远大于后者的0.25; 前者 out-of-sample error 为1.90, 而后者为0.75. 综合来看, $${\cal H_0}$$ 虽然简单, 但比复杂模型 $${\cal H_1}$$ 拟合的好些, 其 var 值减小, 是以 bias 增大为代价.

实际中, 我们是不知道目标函数, 而且训练样本数目也不可能就那么2个, 也不可能获得多种不同的数据集.

> We have one data set, and the simpler model results in a better out-of-sample error on average as we fit our model to just this one data. However, the var
term decreases as N increases,  so if we get a bigger and bigger data set, the bias term will be the dominant part of $$E_{out}$$, and $$\cal H_1$$ will win.

学习算法在 bias-variance 分析中扮演的角色(VC 分析中不考虑学习算法):

1. VC 分析单单依赖于与学习算法 $$\cal A$$ 独立的假设集 $$\cal H$$. 在 Bias-variance 分析中, 两者都要考虑. 相同的假设集(模型) $$\cal H$$, 不同的学习算法会得到不同的最终假设 $$g^{(D)}$$. 而 $$g^{(D)}$$ 恰恰是 bias-variance 分析的基石, 从而导致产生不同的 bias 和 var 值.
2. 上述的 bias-variance 分析以误差平方度量为基础, 但是学习算法自身并不需要以最小化误差平方为基础. 我们可以使用任何一个准则获得基于数据集D的最终假设 $$g^{(D)}$$. 但是, 一旦我们的学习算法产生最终假设  $$g^{(D)}$$, 我们就得使用误差平方来计算 bias 和 variance.

遗憾的是, 上述 bias-variance 分析在实际中无法计算, 原因是目标函数未知. 这就是个理论工具, 对于研究创造新的模型有帮助. Bias 和 variance 分析的两个目标: (1) 降低 variance 同时 bias 的增加不怎么显著; (2) 降低 bias, 同时 variance 的增加不显著. 有许多方法来达到这两个目标, 比如 Regularization. 未来会讲述.

---

## 2.The Learning Curve

>  The learning curves summarize the behavior of the in-sample and out-of-sample errors as we vary the size of the training set.

![learning_curve](https://dn-learnml.qbox.me/image/ai/lfd_ch02_learning_curve_init.JPG)

什么是学习曲线(learning curve)? 如上图所示, 简单模型和复杂模型的学习曲线. $$E_{in}, E_{out}$$ 的期望值 $$\Bbb E_{D}[E_{in}(g^{(D)})], \Bbb E_{D}[E_{out}(g^{(D)})]$$随数据集中样本数目 N 的变化而变化的曲线.

自己看图观察上图中左右两个学习曲线图(简单模型-复杂模型)的区别. (1) 简单模型随 N 的增加, 其误差期望值收敛速度比复杂模型的快;(2) 两幅图中 $$E_{in}$$ 都随着 N 的增加而增加, $$E_{out}$$ 都随着 N 的增加而减小. (3) 至于收敛的最终值, 因为没有在同一幅图中显示, 我不知道该是否 复杂模型的收敛值比简单模型的小.(猜测: 不一定. 看具体的模型. 不能一概而论, 陷入教条.)

下图是学习曲线和 VC 分析, Bias-Variance 分析的结合图.

![vc_bias_var_analysis](https://dn-learnml.qbox.me/image/ai/lfd_ch02_learning_curve_vc_bias_var.JPG)

在学习曲线的 VC分析中, 我们可以观察到 generalization error 和 in-sample error的表示. 在学习曲线的 Bias-Variance 分析中, 我们观察到 bias 和 variance 的表示(理想表示, 前提:  **since it assumes that, for every N, the average learned hypothesis g has the same performance as the best approximation to f in the learning model**).

---

## 3.Sum

本节精度, 主要了解(1)Bias and Variance 偏差与方差, 如何得到, 以及案例讲述; (2)The Learning Curve 学习曲线, 什么是学习曲线及图解分析.

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 2 Training VS Testing

## ChangeLog

```
@Anifacc
read 1:27
note 3:33
all 5:00
2017-09-07 ~ 2017-09-08 beta1.0 WX
```
