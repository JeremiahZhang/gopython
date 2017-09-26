---
layout: post
title: LFD第四章笔记:Regularization
categories:
- MachineLearning
- LearningFromData
---
在书本[1]第4.1节中讲述 overfitting, 4.2节就讲述"治疗" overfitting 的一种办法: Regularization. 本节主要讲述 Regularization 的一些理论, 包括以下内容[1-2]:

- Constraint the Model
- Weight Decay
- Augmented Error

Regularization 的思路就是, 在已有模型(多项式举例)基础上, 施加约束条件, 使得模型对噪声的拟合更少更小些但不至于过度影响拟合真实信号, 从而是 out-of-sample 更好些, 不出现过拟合现象. 这一过程中, 会引出 Weight Decay 和 Augmented Error.

先来看看之前 overfit 案例, 经过 regularization 的效果

![01_reg](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_01_re.JPG)

## 0.前言

> Heuristics: 从 VC bound 视角来观察 regularization

$$E_{out}(h) \leq E_{in}(h) + \Omega({\cal H}) \ \text{for all} \ h \in {\cal H} \tag{4.1}$$

其中 $$ \Omega({\cal H}) $$ is a model complexity penalty. 这是在整个简单的假设集 $$\cal H$$ 之上的 penalty. 想想, 如果可以只使用一个假设 $$h$$, 会不会有效果, 或者效果更好呢? 即以 $$ \Omega(h) $$ 替代 $$ \Omega({\cal H}) $$.

Regularization 的本质就是制造一个假设集的复杂度 $$ \Omega(h) $$, 再最小化 $$E_{in}(h) + \Omega(h)$$ 的和.

> This avoids overfitting by constraining the learning algorithm to fit the data well using a simple hypothesis.[1]

避免 Overfitting 的方法是使用简单的假设, 让学习算法更好拟合数据. [这还是在之前线性拟合出现 overfit 的案例之上考虑].

使用 weight decay (之后会讲) 方法的 regularization 案例.

- 目标函数: $$f(x) = \sin(\pi x)$$
- 数据集: 2个点 N = 2, x 为[-1, 1] 区间内均匀分布产生2个值, 并得到 f(x). No noise.
- 模型: $$\cal H_1$$ 1阶多项式, 线性模型

结果展示见下图:

![02_weight_decay_example](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_02_weight_decay_example.JPG)

> Average hypothesis $$\bar g$$(red) with var(x) indicated by the gray shaded region that is $$\bar g(x) \pm \sqrt{var(x)}$$.[1]

Regularization 的 bias 增大一些, 但是 var=0.33 明显小于 no regularization 的 var=1.69. $$E_{out}$$ 在 no regularization 的情形下为 1.70, regularization 之后为 0.56.  牺牲一点点的 Bias 带来 var 的大量减少, 使得 out-of-sample error 减少.

> The need for regularization depends on the quantity and quality of the data. Given our meager data set, our choices were either to take a simpler model, such as the model with constant functions, or to constrain the linear model. It turns out that using the complex model but constraining the algorithm toward simpler hypotheses gives us more ﬂexibility, and ends up giving the best $$E_{out}$$. **In practice, this is the rule not the exception.** [1]

---

## 1.Constraint the Model

在书本[1] 4.1节 overfitting 内容中, 我们了解导致模型过拟合的主要原因有[3]:

- (1) 数据集样本数目 N : N 越小, overfit 增加.
- (2) stochastic noise: 增加, overfit 增加.
- (3) deterministric: 增加, overfit 增加.
- (4) excessive power: 增加, overfit 增加. [这里的 excessive power: 10阶多项式的 excessive power 就比 2阶多项式的大].

![01_reg](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_01_re.JPG)

上图中, 我们可看出 $$\cal H_2$$ 的拟合效果比 $$\cal H_{10}$$好. 那么我们退一步想, $$\cal H_2$$ 是不是也包含在 $$\cal H_{10}$$ 中呢? 答案是肯定的, 只要10阶中的3-10阶的系数为0, 就相当于 $$\cal H_2$$.

下面是一步步限制[4]:

> (1) Stepping back as constraint

- 样本特征 $$x \in \Bbb R$$
- Q阶多项式进行线性变化, + 线性回归模型
- 使用 $$\bf w$$ 表示 $$\bf \tilde w$$
- $$\cal H_2, H_{10}$$ 之间的关系. 如下

![3](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_03_contraint_01.JPG)

$$\cal H_2$$ 是在 $$\cal H_{10}$$ 里面, 只有添加一定限制条件, 如上图所示.

> (2) Regression with constraint

分别使用两模型作线性回归, $$\cal H_2, H_{10}$$ 的目标都是: 最小会 in-sample-error $$E_{in}(\bf w)$$, 不同的表示方法如下所示.

![4](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_03_contraint_02.JPG)

> (3) Regression with looser constraint

进一步, 我们将 $$\cal H_{10}$$ 的限制放宽一些, 就得到 $$\cal H^{\prime}_2$$, 其与 $$\cal H_2, H_{10}$$ 的关系如下所示, 这个也容易理解.

![5](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_03_contraint_03.JPG)

> (4) Regression with softer constraint

最后, 将 $$\cal H_{10}$$ 的限制放得更温柔一些 (**softer constraint**) , 可得到 $$\cal H(C)$$. 如下所示. 这个也可以理解, 将 s.t. 限制条件放得更宽.

![6](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_03_contraint_04.JPG)

regularized hypothesis 的 $${\bf w}_{reg}$$ 就初始于假设集 $${\cal H}(C)$$.

---

## 2.Weight Decay

在 [LFD第三章笔记:非线性转换(特征转换)](https://anifacc.github.io/machinelearning/learningfromdata/2017/09/18/lfd-ch03-nonlinear-transformation/) 中, 我们了解通过非线性转换, 可以将非线性特征变换 为 "线性"特征. $$\Phi: {\cal H \rightarrow Z}$$.

![7](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_04_legendre_polynomial.JPG)

Polynomial models 线性模型(在 $$\cal Z$$ 空间中来看的话)的一种特殊形式. 书[1]中又用 Legendre Polynomial transform[2] 来说明, 参见上图. (为什么用 Legendre Polynomial 呢? 我的想法是: $$L_1, L_2, \cdots , L_Q$$ 相互正交, 则 $$Z^T Z$$ 可逆.)

在线性回归中, 通过最小化 $$E_{in}(\bf w)$$ 得到权重值. 参见下图[2].

![8](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_05_regression_fitl.JPG)

原特征空间 $$\cal X$$ 经过变化, 到新特征空间 $$\cal Z$$. 其最小化目标明确, 并得到 $${\bf w}_{lin} = (Z^T Z)^{-1} Z^T {\bf y}$$ 的解析式.

前提: 使用 Legendre Polynomial Transfrom, 则 $$Z^T Z$$ 的可逆矩阵存在.  

如果加上 Softer Constraint, 得到 Regularized Regression 问题的矩阵形式.

$$\begin{cases}
\min_{ {\bf w} \in \Bbb R^{Q+1} } E_{in}({\bf w}) = \frac{1}{N} ({\bf Z w - y})^T ({\bf Z w - y})
 \\
s.t. \ {\bf w^T w} \leq C \ (\text{the same as} \sum_{q=0}^Q w_q^2 \leq C) \end{cases}$$

在这种情况下, 得到的权重就是: $$\bf w_{reg}$$. 那么如何解? 书中采用图形结合法[4]:

![9](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_06_solu.JPG)

- 红色线为 $${\bf w^T w} = C$$
- 蓝色线为 $$E_{in}$$

我们要在红色区域内包含轮廓上找到最好的权重.

- w 在红色球面内, 使用梯度下降法: 在蓝色 $$E_{in}$$ 的 $$-\nabla E_{in}({\bf w})$$ 寻找
- 球面 $$\bf w^T w$$ 的法向量为 $$\bf w$$ (如三维中, 一个球面的法向量就是其半径方向的向量)
- 如果 w 寻找的方向 $$-\nabla E_{in}({\bf w})$$ 与 法向量 normal vector $$\bf w$$ 平行, 相当于, 找到这个最佳权重. (因为如果 $$-\nabla E_{in}({\bf w})$$ 与 法向量 normal vector $$\bf w$$ 不平行, 其在球面切平面上还有分量, 会继续沿着梯度方向 search 最佳值.)

因此我们可以得到

$$- \nabla E_{in}({\bf w}_{reg}) = \frac{2 \lambda}{N} {\bf w}_{reg}, \lambda > 0$$

$$\nabla E_{in}({\bf w}_{reg}) + \frac{2 \lambda}{N} {\bf w}_{reg} = 0$$

$$\frac{2}{N}(Z^T Z {\bf w}_{reg} - Z^T {\bf y}) + \frac{2 \lambda}{N}  {\bf w}_{reg} = 0$$

得到: ridge regression in Statistics[4]
$$ {\bf w}_{reg} \leftarrow (Z^T Z + \lambda I)^{-1} Z^T {\bf y}$$

其中, 解

$$\nabla E_{in}({\bf w}_{reg}) + \frac{2 \lambda}{N} {\bf w}_{reg} = 0$$

等价于最小化 增广误差(augmented error)

$$E_{aug}({\bf w}) = E_{in}({\bf w}) + \frac{\lambda}{N} {\bf w^T w}$$

最小化增广误差, 然后就得到权重 $${\bf w}_{reg}$$. 前提: $$\lambda \geq 0$$.

其中 $$+ \frac{\lambda}{N} {\bf w^T w}$$ 称为 "weight-day"

不同的 $$\lambda$$ 对结果的影响如下图所示[2]:

![10](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_07_lambda.JPG)

不得过度使用 $$\lambda$$, 大的 $$\lambda$$ 等价于 prefer shorter w, 等价于 effectively smaller C.

> A larger C allows larger weights and
is a weaker soft-order constraint; this corresponds to smaller $$\lambda$$., i.e., less emphasis on the penalty term $$\bf w^Tw$$ in the augmented error.

> For a particular data set, the optimal value $$C^{\ast}$$ leading to minimum out-of-sample error with the soft-order constraint corresponds to an optimal value  $$\lambda^{\ast}$$ in the augmented
error minimization. If we can find $$\lambda^{\ast}$$ , we can get the minimum $$E_{out}$$.

找到最佳 $$C^{\ast}$$, 即找到最佳 $$\lambda^{\ast}$$, 从而 $$E_{out}$$ 最小.参见下图, $$\lambda, E_{out}$$ 的关系.

![11](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_08_lambda_aster.JPG)

---

## 3.Augmented Error

增广误差:

$$E_{aug}({\bf w}) = E_{in}({\bf w}) + \frac{\lambda}{N} {\bf w^T w} \tag{4.6}$$

如果直接最小化该误差, 就没有限制条件. 但是有上面推演, 有前提: $$\lambda \geq 0$$. 也就是需要根据 $${\bf w^T w} \leq C$$ 限制 w 的解. 从 VC 分析来理解, 假设集 $${\cal H}(C)$$ 复杂度越小越好, 即 如果C 减小($$\lambda$$ 增加), 则假设集 $${\cal H}(C)$$ 泛化性能增加.

一个假设 $$h \in \cal H$$ 的增广误差为:

$$E_{aug}(h, \lambda, \Omega) = E_{in}(h) + \frac{\lambda}{N} {\Omega(h)} \tag{4.7}$$

> for weight decay, $${\Omega(h)} = {\bf w^T w}$$, which penalizes large weights[1].

$$\lambda$$ is the _regularization parameter_.

式子 4.7 类似与之前得到的 VC bound(式子4.1).

> 使用不同的 constraint , 效果不一样哦.

![13](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_10_variance_weight.JPG)

- N = 30
- 噪声水平: $$\sigma^2 =0.5$$
- 阶数: $$Q_f = 15$$

> more noise needs more medicine [2]

噪声水平不同的结果参见下图.

![12](https://dn-learnml.qbox.me/image/ai/lfd_ch04_re_09_noise_reg.JPG)

左图, stochastic noise 越大, $$\lambda$$ 也变大. 右图, deterministic noise 越大, $$\lambda$$ 也变大. 同时, 可以发现, $$E_{out}$$也增大. 如果存在噪声, 则需要调节 regularization parameter $$\lambda$$.

**Regularization & VC dimension**.

> Regularization (for example
soft-order selection by minimizing the augmented error) poses a problem for
the VC line of reasoning.[1]

 Regularization 中, $$\lambda$$ 增大, 学习算法改变, 但是 假设集并没有改变, 那么其 VC 维数 $$d_{vc}$$ 不变.

 但从另外一个角度来看, $$\lambda$$ 增大, 相应的限制条件(softer constraint)中 C 减小, 假设集有效数目则变小, 泛化性能变好, 尽管模型的 VC 维数并没有变化. [相应, 存在 "有效VC维数"]

 > For linear perceptrons, the VC dimension equals the number of fee parameters d + 1, and so an eﬀective number of parameters is a good surrogate for the VC dimension in the VC bound. The eﬀective number of parameters will go down as , increases, and so the eﬀective VC dimension will reﬂect better generalization with increased regularization.

---

## Sum

本节, 了解 "治愈" overfit 的技术: regularization, 关于其理论内容.

- 在线性回归基础上加入 softer constriant 内容
- 加入 weight decay
- 得到 augaugmented error
- 最小化 得出 最佳权重 $$w_{reg}$$

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 1 & Chapter 3 The Linear Model
2. [Learning From Data: Lecture-Slides L12](http://www.cs.rpi.edu/~magdon/courses/LFD-Slides/SlidesLect11.pdf)
3. [台大机器学习基石-L13_handout.pdf](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/13_handout.pdf)
4. [台大机器学习基石-L14_handout.pdf](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/14_handout.pdf)

---

## ChangeLog

```
@Anifacc
read:  4:50
note:  3:12
all:   8: 02
2017-09-23 beta1.0 WX
```
