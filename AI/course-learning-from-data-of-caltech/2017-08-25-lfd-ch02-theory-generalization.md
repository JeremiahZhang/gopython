---
layout: post
title: LFD第二章笔记:泛化误差
categories:
- MachineLearning
- LearningFromData
---

# 泛化误差边界

书中将机器学习中的训练和测试与校园学习中的做练习与考试类比, 非常好的类比. 如果高考中,一个学生平常练习中成绩非常好, 在最后的高考, 成绩不咋样的话, 按一般结论而言, 这个学生不可能考上清华或北大. 类似, 在机器学习中, 学习得到的 Hypothesis 在训练样本上的效果 $$E_{in}$$ 很好, 但在非训练样本或来自整个输入空间X的其他样本上的效果 $$E_{out}$$ 非常差, 那么这个 Hypothesis 能很好解决未来的问题么? 自己思考.

本章主要讲机器学习中的训练 (training) 与测试 (testing).

---

## 1.泛化理论

通过前面的讨论, 我们已经知道 out-of-sample error $$E_{out}$$ 衡量训练集$$\cal D$$训练获得的 hypothesis g, 在输入空间$$\cal X$$中的样本上, 其效果如何. 因此这个$$E_{out}$$的数据基础是非训练集的样本--整个输入空间的样本.

相反, $$E_{in}$$的数据基础是训练集. 它用来衡量我们训练的效果如何. 如果类比高考, 类似每一次的模拟考试的成绩.  即使在模拟考试中, 考试成绩再好, 到实际高考, 考砸了还是对于上清华北大无济于事.

看, 机器学习中, 不仅要考察训练效果 in-sample-error $$E_{in}$$, 也要考察 outer-of-sample error $$ E_{out} $$.

---

## 2.泛化误差

在 Learning from data 这本书中, 泛化误差的定义为: $$E_{in}, E_{out}$$之间的差异. 而也有人直接将$$E_{out}$$定义为泛化误差. 我们在此明确下使用前一种定义泛化误差, 可能处于直接使用 霍夫丁不等式(Hoeffding Inequality)不等式的考虑.(猜想) 反正我们能理解泛化误差就行.


在第一章中, 我们知道下面的霍夫丁不等式,

$$\Bbb P [\lvert E_{in}(g) - E_{out}(g)\rvert > \epsilon] \leq 2M e^{-2 \epsilon^2 N}, \forall \epsilon > 0$$

其中 $$M$$ 为假设集 hypothesis set H 中所有假设 h 的数目, $$N$$ 为训练集 D 中训练样本数目.

如果我们选择一个 tolerance level $$\delta = 2M e^{-2 \epsilon^2 N}\Rightarrow \epsilon = \sqrt{\frac{1}{2N} \ln{\frac{2M}{\delta}}}$$, 那么

$$E_{out}(g) \leq E_{in}(g) + \sqrt{\frac{1}{2N} \ln{\frac{2M}{\delta}}} \tag{2.1}$$

出现的概率至少为$$1 - \delta$$, 因为只考虑单边嘛.

因为不等式(2.1)将$$E_{out}$$限定在与$$E_{in}$$有关的边界中, 因此我们将称为泛化边界(generalization bound). Haha, 原来霍夫丁不等式暗含泛化边界.

那么再从另外的角度来看霍夫丁不等式.

$$\lvert E_{out} - E_{in}\rvert \leq \epsilon$$ 发生的概率至少为$$1 - \delta$$, 则可得到$$E_{out} \leq E_{in} + \epsilon$$(只考虑单边情况); 另外, 也可得到 $$E_{out} \geq E_{in} - \epsilon$$. 以上对于所有 $$h \in \cal H$$ 成立. (在这里思考下, 实际中最终的g, $$E_{out}(g) \geq E_{in}(g)$$? 不一定, 要看训练样本, 要看假设集)

在机器学习中, 我们不仅想要知道训练得到的假设g(比如训练误差最小的那个假设)在非训练集上是否效果仍很好(比如 $$E_{out} \leq E_{in} + \epsilon$$), 我们还想确定我们是否在假设集H做了最大努力的选择--选择最好的g(比如在假设集H中没有其他假设h, 其$$E_{out}(h)$$ 明显小于 $$E_{out}(g)$$).

那么从 $$E_{out}(h) \geq E_{in}(h) - \epsilon$$ 中可以看出, 我们已经做过最大的努力啦, 为什么呢? 因为最终假设g $$E_{in}(g)$$ 好于任意一个在假设集H中的假设h的$$E_{in}(h)$$, 因此, 存在$$E_{out}(h) \geq E_{in}(g) - \epsilon$$.

回到我们的泛化误差, 从不等式(2.1)中可到的误差边界(error bound) $$\sqrt{\frac{1}{2N} \ln{\frac{2M}{\delta}}}$$ 取决于M(假设集的大小)的大小. 如果假设集$$\cal H$$中存在无数多个假设, 那么这个误差边界就会变得无穷大, 这样这个边界就没有意义啦. 现实往往很残酷(所以我们要不断努力进步), 大多数学习模型的假设集存在无穷多的假设, 比如第一章中提到的最简单的感知器模型. 那么我们就无法进行了嘛, 之前说过, 现实残酷, 我们还得继续努力.

 怎么努力? 我们要将误差边界同样适用于无穷多的假设集H. 用有限的数来替代这个无穷大的M. 如果找到这个有限的数, 那么这个误差边界就有意义啦!

 怎么开始? 先来看看看我们如何得到霍夫丁不等式.

在第一章中, 我们是利用 [Boole’s 不等式](https://anifacc.github.io/math/probability/2017/04/21/Axiom-Conditional-Probability/) 得到霍夫丁不等式(2.1).

$$\Bbb P[\cal B_1 \cup B_2 \cup \cdots \cup B_M] \leq \sum_{i=1}^{M} \Bbb P[B_i]$$

这里不等式右边是左边概率取值的最大上限, 但是在实际中, 事件$$\cal B_1, B_2, ..., B_M$$ 往往存在着重叠现象, 如下图(3个事件)所示.

![](https://dn-learnml.qbox.me/image/ai/lfd_or_set_probabilty.JPG)

如果重叠区域越多, 其联合事件的概率要大大小于其所有事件发生概率的和. 这么说来, 我们可以将联合事件发生的概率进一步缩小. 也就是将霍夫丁不等式右边的概率进一步缩小. 但是有前提, 前提就是事件:

$$\lvert E_{in}(h_m) - E_{out}(h_m) \rvert > \epsilon; m = 1, \cdots, M$$

发生重叠的部分非常多, 如类似上图3个时间的重叠.

如果假设 $$h_1$$ 和 $$h_2$$ 非常相似, 那么两个事件 $$\lvert E_{in}(h_1) - E_{out}(h_1) \rvert > \epsilon \\ \lvert E_{in}(h_2) - E_{out}(h_2) \rvert > \epsilon$$ 在大多数据集上同时发生的可能性非常大.

**在大多经典学习模型中, 许多假设非常相似.** 一旦我们合理解释不同假设之间的重叠性, 那么我们就可以用一个**有效数**来提到霍夫丁不等式(2.1)中的无穷大的 M. 关键是如何得到这个**有效数**? 这个是难点, 涉及到数学理论. 下面我们来看看书中的讲解.

## 3.假设集有效数

书中引入增长函数(growth function)来量化假设集的有效数. 增长函数将替代不等式(2.1)中误差边界的M. 增长函数是量化假设集中假设不同的程度, 以及不同的事件发生多少重叠.

步骤:

1. 定义增长函数以及研究其基本特征;
2. 如何界定增长函数的值;
3. 证明增长函数替代误差边界中M的可行性.

经过这几步下来, 误差边界就可以使用在无穷大的M中啦, 因为它会被替代嘛. 好啦, 那么看看书中如何证明.

二进制目标函数为例. $$h(X) \rightarrow \{+1, -1\}; \forall h \in H$$

数据基础:  $$\cal D$$ 训练集(有限的样本), $$x_1, x_2, ..., x_N \in \cal D \subset X$$

### 定义2.1

由假设集 $$\cal H$$ 生成在数据集$$\cal D$$上的生成的二进制(dichotomies)为:

$${\cal H}(x_1, \cdots, x_N) = \{(h(x_1), \cdots, h(x_N) \mid h \in {\cal H} \} \tag{2.3}$$

我们会发现, 别看形式这么复杂, 其实 $${\cal H}(x_1, \cdots, x_N)$$ 就是一个集合, 只不过该集合的元素是由$$\cal H$$中的假设来确定, 这些元素分别为tuple(元组, 类似 Python 中的 tuple). 这些元素tuple为$$(h(x_1), h(x_2), ..., h(x_N))$$, 因为是二进制目标函数, 那么其可能值为$$(1_1, -1_2, ..., 1_i, ..., 1_N)$$, 下标表示位数(或者说第i个训练样本$$x_i$$所对应假设输出).

那么我们可以看出, $${\cal H}(x_1, \cdots, x_N)$$集合中的元素, 每一位上的选择只有2种(+1,-1), 那么我们可以计算这个集合中元素数目的最大值, 为$$2^N = 2_1\cdot2_2\cdots2_N$$

### 定义2.2: 增长函数的定义

上面集合 $${\cal H}(x_1, \cdots, x_N)$$的增长函数为

$$m_{\cal H}(N) = \max_{x_1, ..., x_N \in {\cal X}} \lvert {\cal H}(x_1, ..., x_N) \rvert$$

其中 $$\vert \cdot \vert$$ 表示几何中元素的数目, 不是绝对值.

那么从定义1中的讨论, 可以发现 $$m_{\cal H}(N) \leq 2^N$$

从集合$${\cal H}(x_1, \cdots, x_N)$$中, 我们发现其元素tuple中的元素是有假设$$h$$在各个数据上的输出确定. 而假设集$$\cal H$$中的假设$$h$$有可能不能"shatter"所有的数据. 这里"shatter"是什么意思呢? 我们通过举例说明.

#### 例2.1

![1](https://dn-learnml.qbox.me/image/ai/lfd_shatter_1.JPG)

如上图所示, 在2维欧式空间中, 训练样本只有一个$$x_1$$, 那么我们使用感知器模型, 假设集就是二维空间中的线, 能将样本划分类别. $$\cal H = {all \ lines \ in \ \Bbb R^2}$$. 这样假设集有两个假设: $$h_1(x_1) = +1, h_2(x_1) = -1$$.

定义2.1中的 dichotomies $${\cal H}(x_1) = \{(+1), (-1)\}$$

产生的增长函数$$m_{\cal H}(1) = \max_{x_1 \in {\cal X}} \lvert {(+1), (-1)} \rvert = 2^1$$.

这里感知器就能"shatter"这1个点.

![2](https://dn-learnml.qbox.me/image/ai/lfd_shatter_2%20.JPG)

我们来看看2个点(数据样本为$$x_1, x_2$$)的情况, 与1个点类似.

假设集$$\cal H$$中有4个假设.

$$h_1(x_1, x_2) = (+1, +1)$$
$$h_2(x_1, x_2) = (-1, -1)$$
$$h_3(x_1, x_2) = (+1, -1)$$
$$h_4(x_1, x_2) = (-1, +1)$$

那么, 其增长函数$$m_{\cal H}(2) =  \max_{x_1, x_2 \in {\cal X}} \lvert {(+1, +1), (-1,-1), (+1,-1), (-1,+1)} \rvert = 2^2=4$$

这里感知器就能"shatter"这2个点.

![3_0](https://dn-learnml.qbox.me/image/ai/lfd_shatter_3_0.JPG)

如果是3个输入样本, 感知器产生的假设能将这些样本进行分类, 感知器的假设集总有$$2^3=8$$个假设, 如上图所示. 这时的感知器能"shatter"这三个点.

但是如果3个输入样本很幸运出现在一条直线上(是不是可以说成线性相关呢? 从下面的4个输入样本来看, 不能简单说成是线性相关), 那么感知器只能产生含有6个假设的假设集. 如下图所示. 这种情况下, 感知器就不能"shatter"这三个点. 但是因为

$$m_{\cal H}(N) = \max_{x_1, ..., x_N \in {\cal X}} \lvert {\cal H}(x_1, ..., x_N) \rvert$$

取的是最大值. 所以2D中感知器的 $$m_{\cal H}(3) = max(6, 8) = 8 = 2^3$$

![3_1](https://dn-learnml.qbox.me/image/ai/lfd_shatter_3_1.JPG)

如果是4个输入样本呢, 如下图所示.

![4](https://dn-learnml.qbox.me/image/ai/lfd_shatter_4.JPG)

从图中可以看出, 4个输入样本点分散, 然而 2D 感知器只能产生只有14个假设的假设集. 其增长函数

$$m_{\cal H}(4) = 14 < 2^4=16$$  

因此, 2D中的感知器不能"shatter"4个输入样本. 这个数字4将在下面被称为"Break Point"(猜想, 这个样本数目打破-break-增长函数为2的幂次的规律).

#### 例2.2

在这里, 我们会找几种不同情况下的增长函数.

- Positive rays
- Positive intervals
- Convex sets

> 1-Positive rays

在一维的输入空间中,假设集$${\cal H}$$包含所有的假设$$h: \Bbb R \rightarrow \{-1, +1\}$$. 其形式为$$h(x) = sign (x - a)$$. 假设集具体划分数据集的情形如下图所示.

![](https://dn-learnml.qbox.me/image/ai/lfd_ex2_1_1_postive_rays.JPG)

分割点a右边数据样本的输出全为(+1), 其他的则为(-1). 对于上面的假设集, 就是上面的 Positive rays $$h(x)$$, 其可能产生划分N个数据样本的情形有N+1种, 其数目就等于能生成的 dichotomies 的数目, 根据a的改变而改变, 那么其增长函数

$$m_{\cal H}(N) = N + 1$$

> 2-Positive intervals

这时的假设集变为一段区域内的数据样本输出为(+1), 其他的为(-1), 如下图所示.

![](https://dn-learnml.qbox.me/image/ai/lfd_ex2_1_2_postive_interval.JPG)

该假设集, 能将数据集划分的情况有$$\binom {N+1} {2} + 1$$种, 也就等于产生的 dichotomies 数目. 其增长函数为

$$m_{\cal H}(N) = \binom {N+1} {2} + 1 = \frac{1}{2} N^2 + \frac{1}{2} N + 1$$

> 3-Convex sets 凸集假设

下图展示的区域是凸集.

![](https://dn-learnml.qbox.me/image/ai/lfd_ex2_1_3_convex_set_1.JPG)

> 凸集(convex set)，实数R上（或复数C上）的向量空间中，如果集合S中任两点的连线上的点都在S内，则称集合S为凸集。

前提:

- 输入空间: $${\cal X} = \Bbb R^2$$  
- 假设集: $${\cal H}$$ 包含的假设h, 当x在一个凸集区域其$$h
(x) = +1$$, 否则$$h(x) = -1$$.

那么对于N个输入样本, 其可能的情形如下.

![](https://dn-learnml.qbox.me/image/ai/lfd_ex2_1_3_convex_set_2.JPG)

如上图所示, 所有输入样本分布在一个大圆周上, 那么产生的假设集则有$$2^N$$个假设, 将数据进行划分. 如上图所示, 只要我们比蓝色区域的图形每个角点处大一点点, 那么就可以形成一个假设, 对于N个点, 则会有$$2^N$$个假设划分情形.

所以:

$$m_{\cal H}(N) = 2^N$$

我们走到这里, 有么有发现, 我们在寻找替代假设集假设数目M的有效数, 一个假设集的增长函数就是这个假设集的有效数.

下面我们只要找到这个假设集有效数-增长函数$$m_{\cal H}(N)$$的边界, 我们就能解决上面误差边界问题.

关键就在这里, 如何找到一个假设集增长函数或有效数的上界呢? 这里就需要引入**Break Point**概念, 帮助我们解决问题.

### 定义2.3

> If no data set of size k can be shattered by H, then k is said to be a break point for H.

如果 k 是 break point, 则 $$m_{\cal H}(k) < 2^k$$.

什么意思呢? 还是以例2.2中的假设集为例.

**Positive rays** 的增长函数$$m_{\cal H}(N) = N + 1$$. 如果 N = 2, $$m_{\cal H}(2) = 3 < 2^2 = 4$$, 那么 break point $$k=2$$. 数据样本数为1个时, Positive rays的假设集能shatter这个数据样本点, 但是不能shatter2个数据样本点. 为什么呢?

因为$${\cal H}(x_1, x_2) = \{(+1, +1), (-1, +1), (-1, -1)\}$$. 想想为什么不能产生(+1, -1)?

**Positive intervals** 的增长函数$$m_{\cal H}(N) = \frac{1}{2} N^2 + \frac{1}{2} N + 1$$.

$$N = 1, m_{\cal H}(1) = 2 = 2^1 \\
N =2, m_{\cal H}(2) = 4 = 2^2 \\
N =3, m_{\cal H}(3) = 7 < 2^3 = 8$$

因此, 这种情况下的 break point k = 3.

**Convet sets**: 没有 break point.

**2D 感知器**: break point k = 4.(上文已经讨论过)

到现在, 知道假设集的 break point k, 那么我们就可以找到假设集增长函数的边界.即为$$m_{\cal H}(k) < 2^k$$. (要知道, 如果k是一个假设集的break point, 那么 k+1, k+2, ..., 也是这个假设集的 break point).


---

## 4.增长函数边界

从上面我们已经知道, 如果假设集存在 break point, 那么其增长函数不是以2的幂次增长$$m_{\cal H}(N) = 2^N$$. 对于(2.1)不等式中的泛化误差边界$$\sqrt{\frac{1}{n} \ln \frac{2M}{\delta}}$$, 我们先前的想法是让增长函数(假设集有效数 $$m_{\cal H}(N)$$ )来替代, 但是这个又是2的幂次, 就比较困难, 然后我们引入 break point k, 将增长函数的范围缩小点, 如果增长函数 $$m_{\cal H}(N)$$ 可以写成 N的多项式形式, 那么泛化误差边界在 $$N \rightarrow \infty$$ 时, 其值也趋近于0(这个是怎么得到的, 对边界去极限可得到, 暂时为详细计算, 大概如此猜想).

那么下面的目标就是将增长函数限定到一定的边界中.

首先我们要引入一个基于 break point 的定义.

### 定义2.4 B(N, k) combinatorial quantity

> B(N, k) is the maximum number of dichotomies on N points such that no subset of size k of the N points can be shattered by these dichotomies.

定义的内容是什么呢?

B(N, k) 是 N点下的二分进制(dichotomies)的最大数目, 如此 N 个点中 k个 子点不能被这些二分进制(dichotomies) shatter.

白话一点, 如果没有 break point k, 那么对于一个假设集, 其训练样本数目有N个, 那么其有效数为$$2^N$$, 但是存在 break point k, 我们先不管这个 k 是多少, 对于任意一个假设集$${\cal H}$$, 我们都用 B(N, k)来表示其有效数的最大值, 在这种情况下的 最大的数目的 dichotomies 不能shatter N个数据样本集中的任意子集(样本数目为k).

$$m_{\cal H}(N) \leq B(N, k); \text{if k is a break point for} \ {\cal H}$$

B 取自 "binomial".

现在我们的目标又转化为 B(N, k). 看看B(N, k)能否变为N的多项式形式$$B(N, k) \leq poly(N)$$.

为评估其值, 我们可以首先可以确定:

$$B(N, 1) = 1  \\
B(1, k) = 2, \ for \ k>1 $$

- 对于第一个等式, 容易理解, break point 为1, 数据集N中任意一个点, 假设集都不能shatter, 其值$$B(N, 1) < 2^1$$, 那么就只能等于1了.
- 对于第二个等式, 可以这么理解.
  - k=1, 则是第一个等式的情形;
  - k>1, 则只有一个点的数据集中的任意子集(k个点)不能被shatter. 我们发现一个矛盾, 数据集只有一个点, 怎么会出现k>1个点呢, 这只能说明, 在这种情况下, 只有1个点能被shatter. 即有$$B(1, k) = 2$$.

下面我们要考察的是$$N \geq 2$$和$$k \geq 2$$的情况.

![](https://dn-learnml.qbox.me/image/ai/lfd_def_2_4_k_shatter.JPG)

如上表, 我们可以列出关于N个数据点$$x_1, x_2, ..., x_N$$的假设集的 dichotomies. 如果分开观察前N-1个点$$x_1, x_2, ..., x_{N-1}$$, 与第N个点$$x_N$$, 我们可以划分出如上表的情形.

- $$S_1$$中, 前N个点的dichotomies和$$S_2$$中的dichotomies各不相同, 其$$x_N$$的标签要么是{+1}, 那么是{-1}.
- $$S_2$$中, 又可划分出$$S_2^+, S_2^-$$.
  - $$S_2^+$$中的第N个点的标签却为{+1}, 即$$h(x_N) = +1$$
  - $$S_2^-$$中的第N个点的标签却为{-1}, 即$$h(x_N) = -1$$

如果这样还不好理解, 我们可以看看4个点的例子, 如下图所示.

![](https://dn-learnml.qbox.me/image/ai/lfd_def_2_4_bi_shatter.JPG)

上图紫色区域内正好对应上表中的$$S_1$$区域, 而非紫色区域对应上表中的$$S_2$$区域. 因为在上图$$S_2$$区域中, 前3个点dichotomies成双成对出现(因为$$x_4$$标签有2种情况嘛, 所以就成双成对出现).

继续N个点的dichotomies的讨论. 按上表划分出所有的dichotomies, 总数量为

$$B(N, k) = \alpha + 2\beta \tag{2.4} = (\alpha + \beta) + \beta$$

接下来, 考察前N-1个点的dichotomies, 如上表中的$$S_1 + S_2^+$$区域, 重复的 dichotomies $$S_2^-$$就不再放入讨论.

根据B(N,k)的定义, N个数据集中的任意k个点的子集都不能被假设集"shatter", 那么前N-1个数据集中的任意k个点的子集也不能被假设集"shatter". 这就得到

$$\alpha + \beta \leq B(N-1, k) \tag{2.5}$$

这下就只剩下一个$$\beta$$啦, 那么我们来考虑一下它, 如$$S_2^-$$区域中的dichotomies. 如果前N-1个点中存在k-1个点被假设集"shatter"的话, 再加上第N个点$$x_N$$, 这样就有k个点被"shatter", 与题设(不能被k个点"shatter")矛盾啦.[这里为什么会这样, 因为$$S_2^-$$中的$$x_N$$只有一个标签, 加到前N-1个点中, 肯定会出现k个点被"shatter".] 如此, 我们就可以得到

$$\beta \leq B(N-1, k-1) \tag{2.6}$$.

(2.4)在(2.5)和(2.6)的情形下就可以得出:

$$B(N,k) \leq B(N-1, k) + B(N-1, k-1) \tag{2.7}$$

这样利用式(2.7)和前面已知的两个值, 就可以得到所有的B(N,k), 如下表所示.

![](https://dn-learnml.qbox.me/image/ai/lfd_def_2_4_table_b.JPG)

下面就要利用归纳法求得B(N, k)的边界.

**Lemma2.3**(Sauer's Lemma)

$$B(N, k) \leq \sum_{i=0}^{k-1} \binom N i$$

证明, 利用归纳法.

(1) k=1, N=1时, 不等式成立;  
(2) 假设对于所有$$N \leq N_o, k$$, 不等式也成立, 那么我们只要证(3)成立即可  
(3) $$B(N_o + 1, k) \leq B(N_o, k) + B(N_o, k-1)$$  
(4) 因为

$$\begin{align}
B(N_o + 1, k) &\leq \sum_{i=0}^{k-1} \binom {N_o} i +\sum_{i=0}^{k-2} \binom {N_o} i  \\
  &= 1 + \sum_{i=1}^{k-1} \binom {N_o} i  + \sum_{i=1}^{k-1} \binom {N_o} {i-1} \\
  &= 1 + \sum_{i=1}^{k-1} \left[ \binom {N_o} i + \binom {N_o} {i-1} \right] \\
  &= 1 + \sum_{i=1}^{k-1} \binom {N_o +1} {i}, \text{extend to prove it}\\
  &= \sum_{i=0}^{k-1} \binom {N_o +1} {i}
\end{align}$$

得证.

注: $$\begin{align}
\binom {N} i + \binom {N} {i-1} & = \frac{N!}{i!(N-i)!} + \frac{N!}{(i-1)!(N-i+1)!} \\
  &= \frac{N \cdot (N-1) \cdots (N-i+1)}{i!} + \frac{i \cdot N \cdot (N-1) \cdots (N-i+2)}{i(i-1)!} \\
  &= \frac{N \cdot (N-1) \cdots (N-i+2) \cdot (N-i+1) + i \cdot N \cdot (N-1) \cdots (N-i+2)}{i!} \\
  &= \frac{N \cdot (N-1) \cdots (N-i+2) \cdot (N+1)}{i!} \\
  &= \frac{(N+1)!}{i!(N+1-i)} \\
  &= \binom {N+1} {i}
  \end{align}$$

因此根据 **Lemma2.3** 我们就找到B(N,k)的边界$$B(N,k) \leq \sum_{i=0}^{k-1} \binom N i$$, 它是关于N的多项式.

又因为B(N,k)是假设集有效数的边界, 所以我们可以得到有效数的边界, 而且这个边界是关于N的多项式.

$$m_{\cal H}(N) \leq B(N, k) \leq \sum_{i=0}^{k-1} \binom N i$$

## 5.千山万水总是情

经历千山万水, 我们终于得到假设集有效数的边界.

**Theorem 2.4**

> If $$m_{\cal H}(k) < 2^k$$ for some value k, then $$m_{\cal H}(k) \leq \sum_{i=0}^{k-1} \binom N i$$

不等式右边是关于N的多项式. 这样误差边界就容易确定.

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 2 Training VS Testing
2. 台大[机器学习基石 L5 slider.pdf](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/05_handout.pdf)
3. [凸集](https://baike.baidu.com/item/%E5%87%B8%E9%9B%86)
4. 台大 [机器学习基石 L6 slider.pdf](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/06_handout.pdf)

## ChangeLog

```
@Anifacc
2017-08-26 beta 1.0 wx
```
