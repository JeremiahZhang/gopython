---
layout: post
title: LFD第二章笔记:泛化边界与测试集
categories:
- MachineLearning
- LearningFromData
---

书本上一节介绍 VC dimension, 并得到泛化误差的 VC 泛化边界, 具体笔记可参考 [LFD第二章笔记:VC维 · Anifacc](https://anifacc.github.io/machinelearning/learningfromdata/2017/08/29/lfd-ch02-vc-dimension/). 书本这一节解释 VC 泛化边界及其在实际中的理解, 具体包括一下内容.

- 泛化边界(VC 上界 Generalization Bound)
- 样本复杂度 N(Sample Complexity)
- 模型复杂度 M(Penalty for Model Complexity)
- 测试集(Test Set)
- 其他目标函数.

这一节是从上一节 VC边界讲起, 讨论其中参数对边界的影响, 其中涉及 **样本复杂度**, **模型复杂度** 以及 **测试集**. 在讨论学习问题, 以及 VC维边界等都是以二分类目标函数为例展开的讨论, 但这些讨论, VC维边界等结论同样可应用于 **其他目标函数**, 具有一般性.

---

## 1.泛化边界

上一节中, 我们得到 VC 泛化误差边界(VC generalization bound)如下面不等式 2.12 所示. VC 泛化边界应用于所有假设集(hypothesis sets), 学习算法(learning algorithms), 输入空间(input spaces), 概率分布(probability
distributions), 和二进制目标函数(binary target functions), 看 VC 泛化边界的通用性很强.

$$E_{out}(g) \leq E_{in}(g) + \sqrt{\frac{8}{N} \ln{\frac{4 m_{\cal H}(2N)}{\delta}}} \tag{2.12}, \forall \delta > 0$$

那么我们就来看看这个 VC泛化误差边界. 直观上对比之前的边界与上面的VC边界.

$$E_{out}(g) \leq^{?} E_{in}(g) + \sqrt{\frac{1}{2N} \ln{\frac{2m_{\cal H}(N)}{\delta}}} \tag{2.11}$$

(2.10)的误差边界与(2.10)的VC边界相比, 看公式猜测 VC边界的数值会比前者大, 或者说 VC边界将误差范围放得更宽松些. 事实也的确如此(书中是这么讲的, 或许我们也可以用前者-后者的差, 看看那个大, 可以利用计算机算法实现).

书中简单分析 VC边界宽松的原因, 可以参考公式来分析, 简单总结如下.

- 不等式 2.12是从最基本的霍夫丁不等式推导而来, 其绝对值展开后使用的是单边范围.
- 假设集有效数(其表示是增长函数)$$m_{\cal H}(N)$$ 为假设集的最大的dichotomies数目, 不管这 N 个样本点如何. 比如说 [2d-convex sets](https://anifacc.github.io/machinelearning/learningfromdata/2017/08/25/lfd-ch02-theory-generalization/)中, 其增长函数为 $$m_{\cal H}(N) = 2^N$$, 但实际中, 我们根据来自输入空间的N个数据样本中得到的假设集数目小于增长函数$$2^N$$. 从中我们发现, 有效数是取最大值, 总是大于比实际情况假设集数目.
- 在假设集有效数的讨论中, 我们将其限制在与 VC维数有关数值下, 如下式 2.10 所示. 这也是将误差边界发大的一个原因.

$$m_{\cal H}(N) \leq N^{d_{vc}} + 1 \tag{2.10}$$

上面的分析, 是博主本人阅读书籍原文后的理解, 有没表达错误, 请自行思考.

现在我们知道之前的 VC分析中, 我们得到的 CV 泛化误差边界比之前的宽松许多.(许多研究想让其变紧缩, 但做了很多努力, 结果是  diminishing returns---性能变差).

既然如此, 我们为什么还要费这么大的精力得到这个边界呢? 原因有二:

- 实际中假设集中假设数目是无限多的, 那么 VC分析依然仍让学习可以进行.
- 尽管边界变宽松, 但是对于不同模型, 同等变宽松, 因此可帮助我们比较这些不同模型的泛化能力.

VC分析得到的 VC泛化误差边界如此有用!!!

在实际中, 发现 VC维数 $$d_{vc}$$ 越小, 其泛化能力要好于大的 VC维数, 这可以从不等式 2.12 看出来, 假设集有效数与 VC维数有关(式子2.10).

实际中的一个 **经验法则**: 良好的泛化性能需要的数据样本 $$N $$ 至少为 $$10 \cdot d_{vc}$$. 仅仅是经验法则, 不可一概而论.

VC 分析对于泛化能力理解指导作用, 但也不可绝对的, 不要教条化了哦. 不过可以看看对下面一些实际作用.

---

## 2.样本复杂度

样本复杂度: 训练样本 N 的数目为多大, 才能取得特定的泛化性能.

式 2.12 中, VC 边界中, 可得出

$$N \geq \frac{8}{\epsilon^2} \ln{\frac{4m_{\cal H}(2N)}{\delta}}$$

时, 泛化误差 $$\leq \epsilon$$ 发生的概率至少为 $$1-\delta$$(参考霍夫丁不等式或式 2.1).

进一步可以得到:

$$N \geq \frac{8}{\epsilon^2} \ln{\frac{4 \cdot [(2N)^{d_{vc}} + 1]}{\delta}} \tag{2.13}$$

如何得到N, ($$\epsilon, \delta$$ 确定)可以利用数值分析方法, 观察 N 与 VC维数 $$d_{vc}$$ 的关系.

例2.6 展示了 N 与 VC维数的关系. 实际经验是: $$N \approx 10 \cdot d_{vc}$$.

这对训练样本数目的确定有一定指导作用.

---

## 3.模型复杂度

大多情况下, 我们有确定数目 N 的训练样本集$$\cal D$$. 那么我们从模型复杂度的角度来分析泛化性能.

从式2.12 开始, 可得到

$$E_{out}(g) \leq E_{in}(g) + \sqrt{\frac{8}{N} \ln{\frac{4 \cdot [(2N)^{d_{vc}} + 1]}{\delta}}} \tag{2.14}$$


令

$$\Omega(N, {\cal H}, \delta) = \sqrt{\frac{8}{N} \ln{\frac{4 \cdot [(2N)^{d_{vc}} + 1]}{\delta}}}$$

则 式 2.14 变为下式2.16.

$$ E_{out}(g) \leq E_{in}(g) + \Omega(N, {\cal H}, \delta)$$

我们现在就要观察 $$\Omega(N, {\cal H}, \delta)$$ 这个模型复杂度的惩罚数(a penalty for model complexity). 如果假设集 $$\cal H$$变得更复杂(大的 VC维数), 那么该数就变大, 导致泛化误差就变大(其他参数确定的情况下). 模型简单, 可能得到满意的泛化性能, 如下图所示. 还是从其中的参数出发来考虑泛化误差.

![](https://dn-learnml.qbox.me/lfd_ch02_vc_bound_d_vc.JPG)

---

## 4.测试集

关于测试集, 书中讲解非常清楚, 豁然开朗, 现在明白为什么在实际中将数据样本集划分为训练集和测试集, 以及它们存在的意义.

式2.12 中的 VC边界给出基于 in-sample error $$E_{in}$$, 对 out-of-sample $$E_{out}$$的评估. 上面讲过 VC 泛化误差边界相对宽松, 对训练过程有一定指导作用, 但对于实际预测 $$E_{out}$$的作用几乎没有. 这时候, 我们需要一个测试集(不用于训练过程)来帮助我们估计$$E_{out}$$. 看测试集的作用在这里.

式2.12 指导我们训练得到好的假设 $$g$$, 然后, 我们在测试集上进行测试得到 $$E_{test}$$, 用这个 $$E_{test}$$ 来估计 $$E_{out}$$. 实际中 我们可以确定 $$E_{test}$$ 对于 $$E_{out}$$ 的估计能力强.

$$E_{test}$$ 和 $$E_{in}$$都是样本估计嘛. 同样, 我们可以使用最初的霍夫丁不等式. 这时候, 假设集中就只剩下训练得到最终的假设 $$g$$. 如此, 我们有

$$E_{out} \leq E_{test} + \sqrt{\frac{1}{2N_{test}} \ln{\frac{2}{\delta}}}$$

其中, $$N_{test}$$ 就是测试集中样本数目. 书中并没有将此公式展示出来, 我猜想是这样的.

如此, 泛化边界就变得比之前的 VC边界小很多, 我们可从[练习2.6](https://github.com/JeremiahZhang/gopython/blob/master/AI/course-learning-from-data-of-caltech/exercise_problems_solu/ch02-training_vs_testing_exercise_problems.ipynb)中看一下他们之间的对比.

实际中训练集和测试集都是从总数据样本中划分出来, 训练集数目 = N - 测试集数目, 那么划分到一定程度, 训练得到的误差边界如下所示.

$$E_{out}(g) - E_{in}(g) \leq  \sqrt{\frac{8}{N_{train}} \ln{\frac{4((2N_{train})^{d_{vc}}+1)}{\delta}}}$$

测试得到的误差边界如下所示.

$$E_{out}(g) - E_{test}(g) \leq  \sqrt{\frac{1}{2N_{test}} \ln{\frac{2}{\delta}}}$$

其中 $$N = N_{test} + N_{train}$$

两个误差边界之间存在此消彼长(程度如何, 未知)的关系(纯属猜测, 我是这么理解, 在做完练习2.6之后). 或者至少存在一个临界, 使得前者的 VC边界小于后者的边界.

---

## 5.其他目标函数

VC 分析不仅适用于二进制目标函数, 也可扩展到实值目标函数中, 以及其他目标函数.书中没有证明, 暂且知道即可. 我们也不用深入.

二进制目标函数中, 我们使用 $$h(x) = f(x), h(x) \neq f(x)$$ 来计算 $$E_{in}$$, 从而评估 $$E_{out}$$.

实数值目标函数中, 我们使用的是 $$h(x), f(x)$$ 之间的"距离"来度量. 比如我们常用的一个误差度量是平方误差squared error $$e(h(x), f(x)) = [h(x) - f(x)]^2$$.

$$E_{out}(h) = \Bbb E[(h(x) - f(x))^2]$$

假设集在整个输入样本空间 $$X$$ 上的误差 out-of-sample error $$E_{out}$$ 是误差度量的期望值.

而在训练集下, 误差为
$$E_{in}(h)= \frac{1}{N} \sum_{i=1}^{N}(h(x) - f(x))^2$$

$$E_{in}$$ 是 $$E_{out}$$ 的一个样本估计嘛.

根据大数定理, 有 $$E_{out} \leftarrow E_{in}$$

---

## 6.Sum

本次学习了解一些参数对边界的影响, 其中涉及 **样本复杂度**, **模型复杂度** 以及 **测试集**, 并且知道 VC分析适用于其他目标函数. 到目前学习为止, 我们再一次理解机器学习的可行性.

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 2 Training VS Testing
2. [L7 slider Hsuan-Tien Lin > MOOCs](http://www.csie.ntu.edu.tw/~htlin/mooc/)

## ChangeLog

```
@Anifacc
2017-08-31 beta 1.0 WX
```
