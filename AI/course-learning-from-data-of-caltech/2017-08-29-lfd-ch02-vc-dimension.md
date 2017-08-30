---
layout: post
title: LFD第二章笔记:VC维
categories:
- MachineLearning
- LearningFromData
---

在前一节的读书笔记[泛化误差](https://anifacc.github.io/machinelearning/learningfromdata/2017/08/25/lfd-ch02-theory-generalization/)中, 我们已了解泛化误差, 并经历千山万水得到假设集有效数的边界. 我幼稚的以为, 到这里, 证明的过程总算可以结束. 但是, 事实并不如此, 在书中, 我们还要啃一块骨头---VC维(VC Dimension). 本节笔记主要内容包括以下两部分.

- **VC 维(VC Dimension)**
- **VC 泛化误差边界 (VC Generalization Bound)**

---

## 1.VC 维

上一节书中得到假设集有效数 $$m_{\cal H}(N) \leq B(N, k) \leq \sum_{i=0}^{k-1}{N \choose i}$$, 其中 k 为假设集的 break point. 当书中得到证明之后, 我很幼稚的以为, 这下泛化误差边界总算可以确定, 用有效数提到M不就可以嘛? 然而, 书中还要提到 VC 维.

**Definition 2.5 VC-Dimension**

假设集 $${\cal H}$$ 的 VC 维(Vapnik-Chervonenkis dimension) $$d_{vc}({\cal H})$$ 或 $$d_{vc}$$ 是使得假设集有效数 $$m_{\cal H}(N) = 2^N$$ 成立的 N 的最大值. 换句话来讲, 该 $$d_{vc}+1 = k$$ (break point).

$$m_{\cal H}(N) = 2^N, \forall N \Rightarrow d_{vc}({\cal H}) = \infty$$

从定义我们可以看出, VC 维 $$d_{vc} = k - 1$$.

$$m_{\cal H}(N) = \sum_{i=0}^{d_{vc}} {N \choose i} \tag{2.9}$$

看这个有效数再引入 VC 维后, 变得好看一些. 通过归纳证明(书中第二章问题 Problem 2.5 就是此证明, 可以参考我的[练习与证明](https://github.com/JeremiahZhang/gopython/tree/master/AI/course-learning-from-data-of-caltech/exercise_problems_solu)), 还可以得到下面更简介形式, 关于 N 的多项式.

$$m_{\cal H}(N) \leq N^{d_{vc}} + 1 \tag{2.10}$$

这样假设集有效数(或增长函数)被限制在与 VC维 相关的N的多项式边界中. 如果一个假设集的 VC维无穷大, 那么该假设集增长函数就趋于无穷大, 或许这就是所谓的维数灾难.

到这里, 我们就只用考虑一个问题: 使用假设集的有效数或增长函数 $$m_{\cal H}(N)$$ 替代 泛化误差边界(上一节式2.1)中的 假设集中假设的总个数 M 可行不? (*备注*: 之前我认为假设集的增长函数 m 就表示假设集中假设的总数 M, 原来前面的介绍只是针对输出为{+1, -1}二元分类的问题, 因此还需要推广到更一般性的假设集)

$$E_{out}  \leq^{?} E_{in} + \sqrt{\frac{1}{2N} \ln{\frac{2m_{\cal H}(N)}{\delta}}}$$

如果 VC维 有限, 则假设集有效数 $$m_{\cal H}(N)$$ 被限定与 N 的多项式有关的边界(式2.10)中. 这样泛化误差中 $$\ln{m_{\cal H}(N)} \rightarrow d_{vc} \ln N$$, 那么再加上因子 $$\frac{1}{N}$$, 与一定的 $$\delta$$, 则可以得到 $$E_{out} \approx E_{in}$$.

备注:

$$\lim_{x \rightarrow \infty} \frac{\ln x}{x} =0$$

如果 $$d_{vc} = \infty$$, 则上面的结论就不成立.

所以当 VC维是有限数时, 泛化误差趋近0, 那么训练得到的假设可以泛化用于来自输入样本空间中其他数据的检验, 并使得误差与在训练样本上的误差相近$$E_{out} \approx E_{in}$$.

这时候, 能简单得就直接用 $$m_{\cal H}(N)$$ 替代 M嘛? 书中提到, 不能直接使用如此简单的替代, 要做调整, 转换到类似的结果.

从上面的讨论中, 我们可以看出 VC维的重要性.

- (1) "好模型"的 VC维数有限, 当训练样本数 N 很大时, $$E_{in} \approx E_{out}$$, 模型在训练集 in-sample 上的性能可以泛化到 out-of-sample 上, 即模型泛化能力不错.
- (2) "差模型"的 VC维数趋近无穷, 则该模型泛化能力差. (但也可以建立好的泛化能力, 参考书中P51的脚注2)

既然 VC维重要, 书中针对 VC维作了些讨论.

> $$d_{vc}({\cal H}) \geq N$$ 就表明: 假设集 $${\cal H}$$ 能 "shatter" 大小为 N 的数据集 $${\cal D}$$, and vice versa.

这容易理解, VC维与 break point k 有关, 如果一个假设集的 VC维已知为 N, 那么这个假设集能 "shatter" 数据集中的 N个点. 但不能 "shatter" N+1个点.

还有一些相关的容易理解的结论, 不过也比较混, 让我们一起来理清.

> (1) There is a set of N points that can be shattered by $$\cal H$$. In this case, we can conclude that $$d_{vc} \geq N$$

如果数据集中存在一个 N 个点的子集, 假设集 $$\cal H$$ 能 "shatter" 这个子集中的 N 个点, 那么我们可以得出的结论是 $$d_{vc} \geq N$$. (这个容易理解, 假设集能"shatter" N 个点, 那么 break point $$k >= N+1$$, 就可得出结论)

> (2) Any set of N points can be shattered by $$\cal H$$. In this case, we have more than enough information to conclude that $$d_{vc} \geq  N$$

这个容易理解, 假设集"shatter" 任意一个包含N个点的子集, 我们有足够理由得出上面的结论.

> (3) There is a set of N points that cannot be shattered by $$\cal H$$. Based only on this information, we cannot conclude anything about the value of $$d_{vc}$$

数据集中存在一个包含 N 个点的子集, 而假设集不能"shatter"这子集中的 N 个点, 这种情况下, 我们不能得出任何关于 VC维 的信息. 从上面 (1) 的说明中, 我们可以理解这种情况.

> (4) No set of N points can be shattered by $$\cal H$$. In this case, we can conclude that $$d_{vc} < N$$

从数据集中任意取出N个点, 假设集都不能"shatter"它们, 这就说明 $$d_{vc} \leq N-1$$. 因为 break point k = N.

书中练习 2.4 就是利用上面的结论证明感知器的 VC维, 可参见俺的[简要证明](https://github.com/JeremiahZhang/gopython/blob/master/AI/course-learning-from-data-of-caltech/exercise_problems_solu/ch02-training_vs_testing_exercise_problems.ipynb). 对于 d 维的输入空间, 感知器的 VC维数为 $$d_{vc} = d + 1$$.

2-D 感知器, 其 VC维数为 d+1 = 2+1 = 3 = k-1 = 4-1.

其中 d+1 为感知器权重(参数)数目, 我们可以将 VC维看作是该模型参数的有效数目. 因此模型参数越多, 假设集则更多样化(可观察假设集的有效数 $$m_{\cal H}(N)$$ 得到).

>  The eﬀective parameters may be less obvious or implicit. The VC dimension measures these eﬀective parameters or 'degrees of freedom' that enable the model to express a diverse set of hypotheses.

假设集的多样性未必是件好事, 这个还是可以从假设集有效数即 VC维得出. 如果一个假设集很多样化, 其$$m_{\cal H}(N) = 2^N \Rightarrow d_{vc}({\cal H}) = \infty$$, 如此从下面讨论的 VC泛化误差边界得出模型没有泛化能力.

---

## 2.VC 泛化误差边界

引出 VC维有什么用处呢? 因为上面提到我们不能直接将假设集有效数 $$m_{\cal H}(N)$$ 替代 M.

我们还不确定不等式(2.11)是否成立.

$$E_{out}(g) \leq^{?} E_{in}(g) + \sqrt{\frac{1}{2N} \ln{\frac{2m_{\cal H}(N)}{\delta}}} \tag{2.11}$$

书中接下来讨论用 VC generalization bound 替代上面的泛化误差边界. 如下所示.

**Theorem 2.5 VC generalization bound**

> $$E_{out}(g) \leq E_{in}(g) + \sqrt{\frac{8}{N} \ln{\frac{4 m_{\cal H}(2N)}{\delta}}} \tag{2.12}, \forall \delta > 0$$ 该事件发生的概率$$P \geq 1 - \delta$$

从不等式中可以看出 $$m_{\cal H}(2N)$$ 替代进泛化误差上界中. 该数仍然是关于 N 的多项式, 最大阶数为 VC维数 $$d_{vc}$$.

上面的不等式表明: 无限大却具有有限 VC维数的假设集, 其中的每一个假设都拥有好的泛化能力, $$E_{in} \rightarrow E_{out}$$. 因为假设集的有效数(用有限的增长函数)替代假设集实际无穷大的数目.

使用 VC bound 和 Union bouund的直观差异如下图所示.

![](https://dn-learnml.qbox.me/image/ai/lfd-ch02-vc-bound.JPG)

VC bound 将边界范围缩小.

该理论的证明, 可参考书中的附录A, 一层层推导下来, 特有意思.

主要证明: $$\Bbb P \lbrack \sup_{h \in {\cal H}} \lvert E_{in}(h) - E_{out}(h)\rvert > \epsilon \rbrack \leq 4 m_{\cal H}(2N) e^{- \frac{1}{8} \epsilon^2 N}$$

出发点: 两个数据集上 $${\cal D, D'}$$ 上的$$E_{in}, E_{in}'$$.

## 3.SUM

这一小节, 我们了解 VC维数的定义, 已经将泛化误差边界用 VC维数泛化边界表示.

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 2 Training VS Testing
2. [L6 slider Hsuan-Tien Lin > MOOCs](http://www.csie.ntu.edu.tw/~htlin/mooc/)

---

## ChangeLog

```
@Anifacc
2017-08-30 beta 1.0 WX
```
