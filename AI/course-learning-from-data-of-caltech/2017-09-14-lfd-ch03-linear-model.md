---
layout: post
title: LFD第三章笔记:线性模型
categories:
- MachineLearning
- LearningFromData
---

如果遇到机器学习问题, 首先看看能不能用线性模型来解决. 线性模型相对简单, 且学习效果不错. 根据书中第三章3.3.1-3.3.3节以及第一章内容, 将线性模型笔记统一整理到本文中, 主要涉及以下内容.

- 线性分类 linear classification
  - 感知器算法 PLA perceptron learning algorithm
- 线性回归 linear regression
  - 最小二乘法 ordinary least squares(OLS)
- 逻辑回归 logistic regression
  - 梯度下降法 Gradient Descent  

关于学习模型, 书本 P5 提到

> The hypothesis set and learning algorithm are referred to informally as the learning model.

假设集和学习算法是要我们选择, 它们用来解决学习问题的工具, 统称为学习模型.

以信用卡为例, 根据最终目标的不同, 我们需要使用不同的学习模型.

- (1) 根据申请人信息, 接受或拒绝给其发放信用卡. 二分类问题: 接受 or 拒绝(+1, -1).
- (2) 根据申请人信息, 确定给他的信用额度. 线性回归问题, 最终要确定额度值(实数).
- (3) 根据申请人信息, 判断申请人违约的概率. 最终数值在区间 [0,1] 内.

![credit_example](https://dn-learnml.qbox.me/image/ai/lfd_ch03_credit_example.JPG)

根据不同要求, 则选择不同的假设集和学习算法(线性学习模型)来解决问题. 让我们来看一看下面三个线性模型.

---

## 1.线性分类

针对上面第一个问题(1). 令其输入空间$${\cal X} = \Bbb R^d$$ 为 d 维的欧式空间. 输出空间 $${\cal y} = \{ +1, -1\}$$, 二分类问题. 在信用卡的第一个问题中, 输入空间中的向量 x 的元素(特征)可以是: 月薪, 居住时间, 负债等与申请人信用有关的数据. 那么输出空间 +1 可以表示接受该申请人申请, 发放信用卡. -1 表示拒绝申请, 不给其发放信用卡. 我们可以对申请人的信息经过处理, 再根据其是否满足(阈值)要求, 判断是否通过申请.

我们可以定义这样的假设集:

- 如果 $$\sum_{i=1}^d w_i x_i > threshold $$, 则接受申请.
- 如果 $$\sum_{i=1}^d w_i x_i < threshold $$, 则表示拒绝.

那么我们可以将其转化为下面简介形式.

$$h(x) = sign \left( \left( \sum_{i=1}^d w_i x_i \right) + b\right), \tag{1.1}$$

其中 $$x_1, ..., x_d$$ 为向量 x 中的元素. $$h(x) = +1$$表示接受申请, $$h(x)=-1$$表示拒绝申请. $$b = - threshold$$

我们也可以写成如下形式.

$$h(x) = sign \left( \sum_{i=0}^d w_i x_i \right)$$

其中, $$x_0 = 1, w_0 = b$$.

上面假设集的模型就是通常所说的感知器模型(**Perceptron**). 它非常有用, 在神经网络中会发挥重要作用.

对于此模型, 我们用感知器学习算法(**perceptron learning algorithm**, 这个名词我猜测是在模型基础之上对其命名)来确定最终假设.

令权重向量$$\vec w = [w_0, w_1, ..., w_d]^T$$, 特征向量 $$\vec x = [x_0, x_1, ..., x_d]^T$$.

现在输入空间变为

$${\cal X} = \{1 \} \times \Bbb R^d = \{ [x_0, x_1, ..., x_d]^T \mid x_0 = 1, x_1 \in \Bbb R, ..., x_d \in \Bbb R \}$$

因此:

$$h(\vec x) = sign(\vec w^T \vec x) \tag{1.2}$$.

这里, 用向量形式表示输入空间的向量, 与权重向量.

PLA 算法通过下下面的迭代方法得到权重:

$$\vec w(t+1) \leftarrow \vec w(t) + y(t) \vec x(t) \tag{1.3}$$

PLA的具体流程[2]:

```
# PLA

1: Initialize at step t = 0 to w(0).

2: for t = 0, 1, 2, ... do
3:    the weight vector is w(t)
4:    From training dataset(x_1, y_1), ...(x_N, y_N) pick any misclassified example.
            Call the misclassified example (x*, y*)
            sign(w(t)^T x*) != y*;

5:    Update the weight: w(t+1) = w(t) + y*x*
6:    t = t+1   
```

如果训练集样本是完全线性可分的, 那么, PLA算法在将所以样本正确分类后, 自动终止. 如果数据集非线性可分数据, 则需设定终止准则.

通过前两章, 我们知晓感知器模型学习性. 我们了解学习的两个基本准则:

1. 能否确保 $$E_{out}(g), E_{in}(g)$$ 非常接近?
2. 能否使得$$E_{in}(g)$$ 尽可能小?

对于第1个准则, 感知器模型的 VC维数为 d+1, 通过 VC泛化边界(2.12), 我们可以得到

$$E_{out}(g) \leq E_{in}(g) + O(\sqrt{\frac{d}{N} \ln N})$$

当训练样本个数 N 足够大时, 能确定 $$E_{in}, E_{out}$$ 非常接近. $$O(\cdot)$$ 表示关于其中变量的无穷小量.

对于第2个准则. 如果数据集线性可分, 那么在最后得到的权重下 $$E_{in}(\vec w^{\ast}) = 0$$.

如果数据集非线性可分, 如下图所示, 则 $$E_{in} = 0$$ 就不可能出现, 我们只能去确保 $$E_{in} \approx 0$$, 看看这个可能不, 那么如何确保 $$E_{in} \approx 0$$ 呢?

![non_seperatable](https://dn-learnml.qbox.me/image/ai/lfd_ch03_non_seperatable.JPG)

如上图, 数据不能线性分类, 因为存在异常值(outliers)或噪声(noise).

这时候, 我们要确保$$E_{in}(\vec w)$$尽可能小.

$$\min E_{in}(w) = \min_{\vec w \in \Bbb R^{d+1}} \frac{1}{N} \sum_{n=1}^{N} [[sign(\vec w^T \vec x_n) \neq y_n]] \tag{3.2}$$

其中 $$[[expression \ a]]$$ 表示: 如果表达式a成立, 则其值为1, 如果不成立, 则该值为0.

**NP-hard**: 式(3.2) 最小化问题就是所谓的 NP
-hard, 没有有效的算法来解决.

书中讲到用PLA的变种 **pocket algorithm**[1] 来解决:

```
# the pocket algorithm
1: Set the pocket weight vector w* to w(0) of PLA

2: for t = 0, ..., T-1, do
3:    Run PLA for one update to obtain w(t+1)

4:    Evaluate E_{in}(w(t+1))

5:    If w(t+1) is better than w* in terms of E_{in}, then set
            w* := w(t+1)

6: Return w*
```

与PLA对比, 多出计算 $$E_{in}$$ 部分, 所以计算比 PLA要慢.

上面的算法也设定了迭代步数 T.

书中案例提到数字识别.

## 2.线性回归

线性回归 linear regression 也是一种线性模型, 不过其假设输出值为实数.

对于信用卡额度问题, 可以使用 linear regression 来确定. 但是有前提:

> The choice of a linear model for this problem presumes that there is a linear combination of the customer information fields that would properly approximate the credit limit as determined by human experts. If this assumption does not hold, we cannot achieve a small error with a linear model. We will deal with this situation when we discuss nonlinear transformation later in the chapter.

$$h(\vec x) = \sum_{i=0}^d w_i x_i = \vec w^T \vec x$$.

如何得到最终假设, 确定权重 w 值? 需要使用学习算法, linear regression 使用的学习算法为: 最小二乘法 ordinary least squares(OLS).

$$E_{in}(h) = \frac{1}{N} \sum_{n=1}^{N}(h(\vec x_n) - y_n)^2$$

Then

$$\begin{align}
E_{in}(\vec w) &=  \frac{1}{N} \sum_{n=1}^{N}(\vec w^T \vec x_n - y_n)^2 \\
    &= \frac{1}{N} \| X \vec w - \vec y\|^2 \\
    &= \frac{1}{N}(\vec w^T X^T X \vec w - 2 \vec w^T X^T \vec y + \vec y^T \vec y)
\end{align}$$

其中, 特征矩阵

$$X_{N, d+1} = \begin{bmatrix}
\vec x_1^T \\
\vec x_2^T \\
\ddots \\
\vec x_N^T
\end{bmatrix}$$

目标值矩阵or向量:

$$\vec y = \begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_N \\
\end{bmatrix}$$

书中推演得到权重 w 的解析解, 可以参考书本, 也可以参考以前的线性回归学习笔记[线性回归(Linear Regression)](https://anifacc.github.io/machinelearning/2017/06/12/linear-regression/)中矩阵形式的推导.

$$X^{\dagger} = (X^T X)^{-1} X^T$$

最后得到:

$$\vec w_{lin} = X^{\dagger} \vec y$$

对于线性回归的泛化问题, 其

$$\Bbb E[E_{out}(g)] = \Bbb E[E_{in}(g)] + O(\frac{d}{N})$$

![learning_curve_linear_regression](https://dn-learnml.qbox.me/image/ai/lfd_ch03_linear_reg_learning_curve.JPG)

可以参考 [exercise 3.4](https://github.com/JeremiahZhang/gopython/blob/master/AI/course-learning-from-data-of-caltech/exercise_problems_solu/ch03_linear_model.ipynb)的解了解一下.

## 3.逻辑回归

逻辑回归的输出值在[0,1]区间. 具体笔记可参考之前的学习笔记[逻辑回归(Logistic Regression) ](https://anifacc.github.io/machinelearning/2017/06/14/classification-logistic-regression/), 与文中讲述类似, 都是用极大似然函数法来求解权重, 并用的是平均 ln-likehood.

$$h(\vec x) = \theta (\vec w^T \vec x)$$

其中 $$\theta(s) = \frac{e^s}{1+e^s}$$ 是 sigmiod 函数

in-sample error:

$$E_{in}(\vec w) = \frac{1}{N} \sum_{n=1}^{N} \ln \left( 1 + e^{- y_n \vec w ^T \vec x_n} \right)$$

对于该线性模型, 如何最小化 $$E_in$$, 所使用的算法是 **梯度下降法(Gradient Descent)**.

### 3.1 梯度下降法

梯度下降法常用于最小化2阶可微函数, 就如逻辑回归中的 in-sample error $$E_{in}(\vec w)$$.

如何目标函数不止一个谷底, 梯度下降易陷于局部最优. 但是在上面的逻辑回归中, $$E_{in}$$ 为关于 w 的 凸函数, 它只有一个最低点.

![weight_convex](https://dn-learnml.qbox.me/image/ai/lfd_ch03_E_in_convex.JPG)

那么如何开始 search 最优权重 w?

 (1) 权重 w 向一个方向 $$\hat {\vec v}$$上走, 在目标函数上先走一下步:

$$\vec w(t+1) = \vec w(t) + \eta \hat{\vec v}$$

(2) 如何确定 $$\hat {\vec v}$$ 使得 $$E_{in}(w(t+1))$$ 尽量小呢?

看差异:

$$\begin{align}
\triangle E_{in} &= E_{in}(\vec w(t+1)) - E_{in}(\vec w(t)) \\
    &= E_{in}(\vec w(t) + \eta \hat{\vec v}) - E_{in}(\vec w(t)) \\
    &= \eta \nabla E_{in}(\vec w(t))^T \hat{\vec v} + O(\eta ^2), \ \text{Taylor's Expension}
\end{align}$$

当

$$\hat{\vec v} = - \frac{\nabla E_{in}(\vec w(t))}{\| \nabla E_{in}(\vec w(t))\|} \tag{3.10}$$

时(为什么, 可以参考练习 [exercise 3.8 解答](https://github.com/JeremiahZhang/gopython/blob/master/AI/course-learning-from-data-of-caltech/exercise_problems_solu/ch03_linear_model.ipynb), 简言之就是两向量反方向时, 其乘积为负的最小),

$$\triangle E_{in} \geq -\eta \| \nabla E_{in}(\vec w(t))\|$$.

学习因子 $$\eta$$ 对算法搜索最优值的影响情况, 如下图所示.

![learning_rate](https://dn-learnml.qbox.me/image/ai/lfd_ch03_GD_learning_rate.JPG)

- 太小, 收敛速度慢
- 太大, 则波动大, 不稳定, 有时难以收敛, 左右摇摆.
- 适中, 最好.

理想方法: 当离最小值非常远时, 步长也大一些, 使得收敛快一些; 当接近最小值时, 步长变小, 使其收敛.

比如将学习因子设定成与 in-sample 误差梯度成比例的值.

$$\eta_t = \eta \| \nabla E_{in}\|$$.

这样取有一个方便:

$$\begin{align}
\vec w(t+1) &= \vec w(t) + \eta_t \hat{\vec v} \\
    &= \vec w(t) + \eta \| \nabla E_{in}\vec w(t)\| (- \frac{\nabla E_{in}(\vec w(t))}{\| \nabla E_{in}(\vec w(t))\|}) \\
    &= \vec w(t) - \eta \nabla E_{in}(\vec w(t)) \\
    &= \vec w(t) + \eta \vec v_t
\end{align}$$

其中: $$\vec v_t = -\nabla E_{in}(\vec w(t)$$. 这时候方向向量不再是之前的单位向量(3.10). 这就是 **fixed learning rate gradient descent algorithm** for miniming $$E_{in}$$(with redefined $$\eta$$)[1].

```
# Fix learning rate gradient descent algorithm
# (batch gradient descent)
1: Initialize at step t = 0 to w(0).

2: for t = 0, 1, 2, ..., do
3:    Compute the gradient
              g_t = ▽E_in(w(t))

4:    Move in the direction
              v_t = - g_t

5:    Update the weights:
              w(t+1) = w(t) + η v_t

6:    Iterate 'until it is time to stop'
7: end for
8: Return the final weights.
```

学习因子需确定, 一般取 $$\eta = 0.1$$ 左右.

in-sample error of logistic regression:

$$E_{in}(\vec w) = \frac{1}{N} \sum_{n=1}^{N} \ln \left( 1 + e^{- y_n \vec w ^T \vec x_n} \right)$$

$$\vec g_t = -\frac{1}{N} \sum_{n=1}^{N} \frac{y_n \vec x_n}{1 + e^{y_n \vec w^T (t) \vec x_n}}$$

### 3.2 SGD (stochastic gradient descent)

GD算法计算所有样本的 in-sample error $$E_{in}$$. 我们也可以随机挑选一个样本, 计算单个 in-sample error $$e$$, 并用起梯度更新权重.

- (1) 首先(uniformly)从训练集中随机挑选一个训练样本 $$(\vec x_n, y_n)$$  
- (2) 计算其误差: $$e_n(\vec w) = \ln(1 + e^{- y_n \vec w^T \vec x_n})$$
- (3) 计算误差梯度: $$\nabla e_n(\vec w) = \frac{- y_n \vec x_n}{1 + e^{y_n \vec w^T \vec x_n}}$$
- (4) 权重更新.

$$\begin{align}
\vec w(t+1) &\leftarrow \vec w(t) - \eta \nabla e_n(\vec w(t)) \\
    &= \vec w(t) + y_n \vec x_n \left(\frac{\eta}{1 + e^{y_n \vec w^T \vec x_n}} \right)
\end{align}$$

这与我们使用整个训练集的误差和来优化(batch gradient descent)不同, 这里使用单个样本的误差, 但最后平均值是相同, 因为N个单个样本的权重变化期望为:

$$- \eta \frac{1}{N} \sum_{n=1}^N \nabla e_n(\vec w)$$.

与 batch gradient descent 权重更新中的相同.

### 3.3 初始化和终止条件

在上面的算法流程中, 初始化权重及算法停止条件需要确定.

- 初始化权重 w(0):
  - (1) 全部为 0 或者
  - (2) 随机数: 如 均值为0, 方差较小的正太分布中随机选择数值.
- 终止条件:(优化中重大话题)
  - 迭代次数
  - g_t < 阈值
  - 误差阈值
  - 混合

### 3.4 线性模型联系

另外书中讲到三个线性模型(线性分类, 线性回归逻辑) 之间其实本质相近.

- 逻辑回归的输入值在[0,1]区间, 如果再设定一个阈值, 那么就可以变为线性分类.
- 同样, 线性回归也可以设定阈值, 变为线性分类.

[练习3.9](https://github.com/JeremiahZhang/gopython/blob/master/AI/course-learning-from-data-of-caltech/exercise_problems_solu/ch03_linear_model.ipynb) 是证明 线性分类的 error measure, 比线性回归和逻辑回归的 error measure 值小.

因此, 线性回归或逻辑回归得到的权重可以作为线性分类的初始化权重.

## Sum

本次主要学习了3个线性模型: 线性分类, 线性回归, 逻辑回归, 并了解与它们对应的算法: 感知器学习算法 PLA, 最小二乘法 OLS 和 梯度下降法.

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 1 & Chapter 3 The Linear Model
2. [Learning From Data: Lecture-Slides L2, L8-L9](http://www.cs.rpi.edu/~magdon/courses/learn/slides.html)

## ChangeLog

```
@Anifacc
read: 9: 17
note: 6: 17
all: 15: 34
2017-09-12 ~ 09-15 beta 1.0 WX
```
