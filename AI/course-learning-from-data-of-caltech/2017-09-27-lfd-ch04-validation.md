---
layout: post
title: LFD第四章笔记:Validation
categories:
- MachineLearning
- LearningFromData
---
书本[1]4.3节讲述另一种"治疗" overfitting 的方法: Validation. 书本先讲述

- (1) Validation Set: 什么是 validation set?
- (2) Model Selection: validation 可以用于 model selection.
- (3) Cross Validation: 交叉验证. validation 方法: Leave-One-Out, V-Fold(K-Fold)

书本还是偏重理论讲解, 我们得加强实战内容. 还好马上就要把这本书前半部分基础理论啃完, 之后就要进入实战. 在以后具体算法部分, 以 Top-Down 方式来学习. Validation 这部分理论内容帮助我们理解 Scikit-Learn 机器学习库中的 validation 的具体应用, 理解它的原理, 真是舒畅.

## 0.Intro

我们可以认为: regularization 和本节中讲述的 validation 都在最小化 $$E_{out}$$ 上面作文章, 而不是 $$E_{in}$$. 然后, 显示中, 我们只有 sample, 我们不可能知道真实的 $$E_{out}$$, 所以我们只能基于现有的样本去估计 $$E_{out}$$. 从某种角度来讲, *find an in-sample estimate of the out-of-sample error* 是机器学习的必杀技(Holy Grail of machine learning.). 这逻辑很正确, 我们只能根据已有的(采集到的)数据样本(sample) 来估计 out-of-sample error.

Regularization 最小化 out-of-sample error 的方法是通过 overfit penalty.

$$E_{out}(h) = E_{in}(h) + \text{overfit penalty}$$
$$E_{out}(h) = E_{in}(h) + \frac{\lambda}{N} \Omega(h)$$

而在 Validation 中, 直接估算 out-of-sample error.

$$E_{out}(h) = E_{in}(h) + \text{overfit penalty}$$

在第二章中, 我们有了解 test set. 将数据分为训练集 和 测试集. 测试集就是用来评估学习算法得到最终假设的性能($$E_{test}$$ 是否很小或满足要求.)

> Test error $$E_{test}$$, unlike the in-sample-error $$E_{in}$$, is an unbiased estimate of $$E_{out}$$.

test error $$E_{test}$$ 是 out-of-sample error $$E_{out}$$ 的无偏估计 (很多很多个 test error 变量的期望等于 out-of-sample error).

![01-test-set](https://dn-learnml.qbox.me/image/ai/lfd_ch04_01_test_set.JPG)

下面我们来看看到底什么是 Validation?

---

## 1.Validation Set

在理解什么是 Validation 之前, 我们先来理解什么是 validation set.

**Validation Set** 就是在 Validation 中所使用的数据集, 称为验证集(validation set).

我们首先从数据集中取出一个子集, 这个子集中的样本不用于训练. 比如, 我们的总样本集为 $$\cal D$$, 样本个数为 N . 我们将其划分为包含 (N-K) 个样本的训练集 $$\cal D_{train}$$, 以及包含 K 个样本的验证集 $$\cal D_{val}$$, 它们分别用于模型训练和模型验证. 这时候, 未用于训练的 K 个样本, 我们将其作为 out-of-sample 来看待, 用来估计 $$E_{out}$$.

验证集 和 测试集 的区别. 虽然两者都没有用于模型训练, 但是验证集影响着模型学习过程, 它影响最终假设的确定. 而测试集并没有这样的影响, 测试集只在最终假设确定后, 用来评断模型学习能力.

那么我们可不可以从数据集角度来理解, 总数据集 $$\cal D_{all}$$. 我们要将其分为 $$\cal D_{1}, D_{test}$$.

- $$\cal D_{1}$$: 用于模型训练, 并确定最终假设. 这又分为:
  - $$\cal D_{train}$$: 用于模型训练的训练集
  - $$\cal D_{val}$$: 用于模型验证的验证集, 该数据集并不用于模型训练
- $$\cal D_{test}$$: 用于测试最终假设效果的测试集.

我们可不可以这样理解: 在模型选择, 训练, 确定最终假设过程中, 我们需要使用的是 训练集和验证集. 之后测试模型最终效果时, 我们需要使用测试集? 这样理解, 就不会将测试集和验证集混淆呢? 待定, 自己思考.

![02-validation-set](https://dn-learnml.qbox.me/image/ai/lfd_ch04_02_validation_set.JPG)

现在, 我们的总样本集为 $$\cal D$$, 样本个数为 N . 我们将其划分为包含 (N-K) 个样本的训练集 $$\cal D_{train}$$, 以及包含 K 个样本的验证集 $$\cal D_{val}$$, 它们分别用于模型训练和模型验证.

我们通过训练集 $$\cal D_{train}$$ 训练模型得到一个最终假设 $$g^{-} \in {\cal H}$$, 然后我们用这个假设在验证集(validation set) 上计算 validation error(验证误差)

$$E_{val}(g^{-}) = \frac{1}{K} \sum_{ {\bf x}_n \in {\cal D_{val}} }  {\bf e} \left( g^{-}({\bf x}_n, y_n)\right)$$

其中 $${\bf e} \left( g^{-}({\bf x}_n, y_n)\right)$$ 为验证集中每个样本的误差. 对于分类问题: $${\bf e} \left( g^{-}({\bf x}_n, y_n)\right) = [[g^{-}({\bf x}) \neq y]]$$, 即 如果 $$g^{-}({\bf x}) \neq y$$, 则误差为1, 否则为0. 对于回归问题, 使用平方误差, 如 $${\bf e} \left( g^{-}({\bf x}_n, y_n)\right) = \left( g^{-}({\bf x}) - y \right)^2$$.

Validation error $$E_{val}$$ 也是 out-of-sample error $$E_{out}$$ 的无偏估计(因为最终假设 $$g^{-} $$ 的确定不依赖于 验证集中的样本, 只依赖与训练集中的样本). 因此有:

$$\begin{align}
\Bbb E_{\cal D_{val}} \left[ E_{val} (g^{-}) \right]
    &= \frac{1}{K} \sum_{ {\bf x_n} \in {\cal D_{val}} } \Bbb E_{\cal D_{val}} \left[ {\bf e} \left( g^{-}({\bf x_n}, y_n) \right) \right] \\
    &= \frac{1}{K} \sum_{ {\bf x_n} \in {\cal D_{val}} } \Bbb E_{\bf x_n} \left[ {\bf e} \left( g^{-}({\bf x_n}, y_n) \right) \right] \\
    &= \frac{1}{K} \sum_{ {\bf x_n} \in {\cal D_{val}} } E_{out}(g^{-}) \\
    &= E_{out}(g^{-})
\end{align} \tag{4.8}$$

第二个等式变化中, e 只与 $$D_{val}$$ 中的 $${\bf x}_n 有关$$. [其无偏估计与 test set 中计算类似.]

$$E_{val}$$ 估计 $$E_{out}$$ 的可靠性如何? 书中以 分类问题为例. 利用 Hoeffding 不等式 和 VC 边界.

$$E_{out}(g^-) \leq E_{val}(g^-) + O\left(\frac{1}{\sqrt{K}} \right) \tag{4.9}$$

将 $$\cal D_{val}$$ 当作 "in-sample" data set. 不限现在的假设集中只有一个假设$$g^-$$, 样本数目为 K.

同样, 按照 Test set 中推演, 我们可以得到:

$$\begin{align}
{\bf Var} [E_{val}(g^{-})] &= \frac{1}{K^2} \sum_{k=1}^K {\bf Var}[e_k] \\
  &= \frac{1}{K} {\bf Var}_{\bf x}[e(g^{-}({\bf x}), y)]  \\
  &= \sigma_{val}^2
\end{align}$$

书中以2次多项式 $$\cal H_2$$的期望验证误差, 其图形如下所示. 其中: target function 的为 10次多项式 $$Q_f = 10$$, 数据集样本总数为 $$N =40$$, 噪声水平 $$\sigma^2 = 0.4$$. 验证误差的期望等于 $$E_{out}(g^-)$$, 如公式(4.8)所示.

![03-expected-val-error](https://dn-learnml.qbox.me/image/ai/lfd_ch04_03_expected_validation_error.JPG)

注: 蓝色线为 $$\Bbb E[E_{val}(g^-)]$$, 是关于 K 的函数, 而阴影部分区域为: $$\Bbb E[E_{val}(g^-)] \pm \sigma_{val}$$.

从上图中, 我们可以看出, 验证集样本数目 K变化时, 验证误差的期望也变化. 大体趋势是: K 增大, $$\Bbb E[E_{val}]$$ 先减小, 后增大. 所以 K 的选择需要慎重. **实际经验公式: K = N/5**. (数据集N中的20%可用作验证集).

关于验证集数目 K, 我们还需要讨论一下[1].

- (1) It has to be big enough for $$E_{val}$$  to be reliable, and(公式 4.9)
- (2) it has to be small enough so that the training set with N-K points is big enough to get a decent $$g^-$$.(从之前的学习曲线 learning curve可以看出.) [The fact that more training data lead to a better final hypothesis has been extensively verified empirically, although it is challenging to prove theoretically.]

这里就出现矛盾了吧. 经验是训练集数目越大, 我们最终假设也越好. 但用理论很难证明.

### 1.1 Restoring D

![04_validation_set_estimate](https://dn-learnml.qbox.me/image/ai/lfd_ch04_04_val_estimate_e_out.JPG)

我们有数据集 D, 主要目标是在所有N个数据上进行训练, 得到最终假设 $$g$$, 通过 $$E_{in}(g)$$ 来估计 $$E_{out}(g)$$; 现在, 使用 validation, 我们的目标变为 估计 $$E_{out}(g)$$, 但是 我们只能在 N-K 个数据上训练得到最终假设 $$g^-$$, 并通过验证集得到 $$E_{val}(g^-)$$, 并用其来估计 $$E_{out}(g^-)$$.

(1) 主要目标:

$$E_{out}(g) \leq E_{in}(g) + O \left( \sqrt{\frac{d_{vc}}{N} \log N} \right) \tag{4.10.1}$$

不等式中的 最后的小量 is biased error bar depends on $$\cal H$$

(2) 次要目标:

$$E_{out}(g) \leq E_{out}(g^-) \leq E_{val}(g^-) + O \left( \frac{1}{\sqrt K}\right) \tag{4.10.2}$$

其中, 第一个不等式: 根据 learning curve 经验确定, 而非理论(训练样本数少, 则误差大). 最后的小量 is unbiased error bar depend on $$g^-$$.

比较(4.10.1) 和 (4.10.2), 在验证集上的验证误差估计得到的 $$E_{out}$$ 有可能比用全部 数据集得到的 $$E_{in}$$ 估计的 $$E_{out}$$ 要好. 因为(4.10.1)中 假设集的 VC 维数可能很大.

现在, 我们知道, 用验证集来估计 $$E_{out}$$, 而该验证集不会影响学习过程. 这是验证集使用的一种方式, 其实, 我们还可以用验证集来影响学习过程. 下面道来.

---

## 2.Model Selection

Validtion 的重要作用是 Model Selection. 这意味着, 我们可以使用 Validation 对 模型进行选择: 从线性模型或非线性模型中进行选择; 也可以从一个模型的1阶, 2阶, ..., 多阶多项式中进行选择; 或选择 regularization 中的 regularization parameter 参数.

![05-model-selection](https://dn-learnml.qbox.me/image/ai/lfd_ch04_05_model_selection.JPG)

假设我们有 M 个模型 $${\cal H_1, H_2, \cdots } {\cal H}_M$$, 在每一个模型上, 我们使用训练集训练, 验证集进行验证, 得到 validation errors $$E_1, \cdots, E_M$$, 参见下图.

![06-m-models](https://dn-learnml.qbox.me/image/ai/lfd_ch04_06_M_hypothesis.JPG)

$$E_{m} = E_{val}(g^{-}_m); \ \ m =1, 2, ..., M.$$

每个验证误差估计对应的模型$${\cal H}_m$$的$$E_{out}(g^{-}_m)$$

我们如何确定最后的模型呢? 哪个 validation error 最小, 我们就选哪个模型. $$E_{m^{\ast}} \leq E_m, \ for \ m=1, ..., M$$. 其所对应的 $$\cal H_{m^{\ast}}$$ 就是我们最后选择的模型. 这时候值得注意的是: $$E_{m^{\ast}}$$ 不再是 $$E_{out}(g^{-}_{m^{\ast}})$$ 的无偏估计.(思考下为什么? 因为我们选择验证误差最小的那个模型来估计, 所以不再是无偏估计.)

书中以 $$\cal H_2, H_5$$ 之间的模型选择为例. target function 的复杂度 $$Q_f = 3$$, 噪声水平 $$\sigma^2 = 0.4$$, 数据集样本数目 $$N = 35$$. 最终假设的期望误差曲线如下图所示.

![7-model-selection-example](https://dn-learnml.qbox.me/image/ai/lfd_ch04_07_model_selectin_example.JPG)

以之前所学来理解 Model Selection 过程: 模型结果训练后的到最终假设, 这时候, 有 M 个最终假设.

$${\cal H}_{val} = \{ g_1^{-}, g_{2}^{-}, \cdots, g_{M}^{-}\}$$

这时候, Validation 假设集有 M 个假设. 下面的过程, 类似之前学习的过程, 在 M 个假设集中再确定一个最终假设$$g^{-}_{m^{\ast}}$$. 根据霍夫丁不等式和 VC边界, 我们可以得到式子(4.11)

$$E_{out}(g^{-}_{m^{\ast}}) \leq E_{val}(g^{-}_{m^{\ast}}) + O \left( \sqrt{\frac{\ln M}{K}} \right)$$

如果不用 validation set 来确定最终假设, 我们也可以在所有数据集N上进行训练, 然后比较 in-sample-error 来确定最终假设 $$g_m$$.

如果使用 validation set, 那么我们就比较 validation error 来确定最终假设  $$g_{m^{\ast}}^{-}$$. 用这种方法来进行模型选择, 前提是我们相信式(4.12) 第一个不等式的成立. (虽然我们不能证明其成立, 只是根据实际经验确定(参见 learning curve)). 在利用 validation set 选择模型后, 得到模型 $${\cal H_{m^{\ast}}}, E_{m^{\ast}}$$, 利用该假设集 $$\cal H_{m^{\ast}}$$, 再在所有数据集 D 上得到的最终假设 $$g_{m^{\ast}}$$.

$$E_{out}(g_{m^{\ast}}) \leq E_{out}(g_{m^{\ast}}^{-}) \leq E_{val}(g_{m^{\ast}}^{-}) + O \left( \sqrt{\frac{\ln M}{K}} \right) \tag{4.12}$$

![08-validation_model_selection_error_comparing](https://dn-learnml.qbox.me/image/ai/lfd_ch04_08_validation_model_selection_error_comparing.JPG)

![09-](https://dn-learnml.qbox.me/image/ai/lfd_ch04_09_validation_example.JPG)

两个假设集进行模型选择, 一个是5阶多项式的假设集, 一个是 10阶多项式的假设集. 该图来自台大机器学习基石[3]的L15课, 与书中所说的假设集不一样, 但是图形是一样的. [我都不晓得为什么模型不一样, 得到结果一样. 可能存在bug]. 结合式子(4.12) 来理解该曲线图. 并思考上面图中最后提出的问题. [问题解答: 因为 K 增加, 用于训练集的 N-K 数目就减小, 训练得到的最终假设 $$g_m^-$$ 效果比 使用所有 N个样本训练得到的 $$g_m$$ 要差, 这就会造成 红色曲线会出现部分高于黑色直线.]

Validation 方法需要在数据集中取出 K个样本作为 Validation Set, 从而减少训练样本数目, 这是 Validation 的缺点. (如果数据集本来就很少, 怎么办???)

文中接下来就介绍 Cross Validation.

---

## 3.Cross Validation

> 交叉验证.

![10-K-dilemma](https://dn-learnml.qbox.me/image/ai/lfd_ch04_10_dilemma.JPG)

第一个近似, 建立在 K 值较小的基础之上, 因为 K 越小, N-K 越大, 训练得到的最终假设 $$g^{-}$$ 则越好, 这样 $$E_{out}(g^{-})$$(validation 得到的最终假设 的 out-of-sample error) 与 $$E_{out}(g)$$(在所有数据集N 上训练得到的最终假设的 out-of-sample error) 之间的差距就越越小.

但是, K 小, 比如 K = 1时, 根据式子(4.9), 则 $$E_{val}(g^{-})$$ 估计 $$E_{out}(g^{-})$$ 的 可靠度就变低. (最后的小量变大啦.)

$$E_{out}(g^-) \leq E_{val}(g^-) + O\left(\frac{1}{\sqrt{K}} \right) \tag{4.9}$$

这时候, 我们可以使用 cross validation 来估计 out-of-sample error. 书中介绍两种 cross validation 方法:

- Leave-One-Out
- V-Fold (K-Fold)

### 3.1 Leave-One-Out

![11-loocv](https://dn-learnml.qbox.me/image/ai/lfd_ch04_11_loocv.JPG)

留一法: 此时 validation set 的 K = 1, 即只有一个样本作为验证集, 其他的作为训练集. 每个样本要做过一次验证集, 总共会有 N 次不重复的 validation.

每一次 validtion 得到的 error 为:

$$e_n = E_{val}(g^{-}_n) = err \left( g^{-}_n(x_n), y_n \right)$$

$$E_{cv} = \frac{1}{N} \sum_{n=1}^{N} e_n = \frac{1}{N} \sum_{n=1}^{N} err \left( g^{-}_n(x_n), y_n \right)$$

案例[3]:

![12-loocv-example](https://dn-learnml.qbox.me/image/ai/lfd_ch04_12_loocv_example.JPG)

$$E_{cv}$$ 是 $$E_{out}(g^{-})$$ 的无偏估计. 这里 $$g^{-}$$ 在每一次 validation 时都不一样, 不再是单一假设的 $$g^{-}$$, 而是 $$g^{-}_n$$.

![13-theory-guarantee](https://dn-learnml.qbox.me/image/ai/lfd_ch04_13_loocv_theory.JPG)
> Theorem. $$E_{cv}$$ is an unbiased estimate of $$\bar E_{out}(N-1)$$(the expecteation of the model performance, $$\Bbb E [E_{out}(g)]$$, over data sets of size N-1)

![14-loocv-progress](https://dn-learnml.qbox.me/image/ai/lfd_ch04_14_loocv_progress.JPG)

> How reliable is the cross validation estimate $$E_{cv}$$?

只有计算 $$E_{cv}$$ 的方差 variance. 这时候 方差计算时, $$e_1, e_2, ..., e_N$$ 不是相互独立的变量啦. (为什么, 自己思考下.)

实际中, 不是经常使用 Leave-One-Out 方法, 更多的是使用 V-Fold validation 方法.

### 3.2 V-Fold (K-Fold)

> V-折交叉验证法 或 K-折交叉验证法.

![15-10-fold](https://dn-learnml.qbox.me/image/ai/lfd_ch04_15_k_fold_validation.JPG)

该交叉验证法最常用的是 10折交叉验证. V-折交叉验证法 就是将数据集D 均匀分成V份, 总进行 V次 validation, 每一次选择不同的验证集, 其他的作为训练集. 比如上面的 10折交叉验证: 数据集均匀分成 10个子集, 第一次将 $$D_1$$ 作为验证集, 其他 9 个子集作为训练集, 然后得到最终假设 $$g^{-}_1$$, 第 v 次是, 将 $$D_v$$ 作为验证集, 其他 9 个子集作为训练集  然后得到最终假设 $$g^{-}_v$$, 依次下去, 10个子集都做过一次验证集后结束. 总共会进行10次 validation.

$$E_{cv}({\cal H, A}) = \frac{1}{V} \sum_{v=1}^{V} E_{val}^{(v)}(g_v^{-})$$

选择模型 by $$E_{cv}$$:

$$m^{\ast}: = {\bf argmin}_{1\leq m \leq M} \left( E_m = E_{cv}({\cal H_m, A_m}) \right)$$

经验: 尝试 5折与10折.

---

## Sum

书中4.3节主要讲解 validation 的基础理论. 主要内容为:

- 什么是 validation, validation set;
- validation 进行模型选择;
- 介绍两种 cross validation:
  - Leave-One-Out validation
  - V-Fold cross validation

书中第四章到此就结束. 第四章主要讲述内容总结[1]:

- Noise (stochasitic or deterministric) affects learning adversely, leading to overfitting
- Regularization helps to prevent overfitting by constraining the model, reducing the impact of the noise, while still giving us flexibility to fit the data.
- Validation and cross validation are useful techniques for estimating E_{out}. One important use of validation is model selection, in particular to estimate the amount of regularization to use.

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 1 & Chapter 3 The Linear Model
2. [Learning From Data: Lecture-Slides L13](http://www.cs.rpi.edu/~magdon/courses/LFD-Slides/SlidesLect13.pdf)
3. [台大机器学习基石-L15_handout.pdf](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/15_handout.pdf)

---

## ChangeLog

```
@Anifacc  
read:  4: 53
note:  4: 33
all:   9: 26
2017-09-27 beta 1.0 WX
```
