# Chapter 02 Training VS Testing-Theory of Generalization

书中将机器学习中的训练和测试与校园学习中的做练习与考试类比, 非常好的类比. 如果高考中,一个学生平常练习中成绩非常好, 在最后的高考, 成绩不咋样的话, 按一般结论而言, 这个学生不可能考上清华或北大. 类似, 在机器学习中, 学习得到的 Hypothesis 在训练样本上的效果$$E_{in}$$很好, 但在非训练样本或来自整个输入空间X的其他样本上的效果$$E_{out}$$非常差, 那么这个 Hypothesis 能很好解决未来的问题么? 自己思考.

本章主要讲机器学习中的训练(training)与测试(testing).

---

## 1.泛化理论

通过前面的讨论, 我们已经知道 out-of-sample error $$E_{out}$$ 衡量训练集$$\cal D$$训练获得的 hypothesis g, 在输入空间$$\cal X$$中的样本上, 其效果如何. 因此这个$$E_{out}$$的数据基础是非训练集的样本--整个输入空间的样本.

相反, $$E_{in}$$的数据基础是训练集. 它用来衡量我们训练的效果如何. 如果类比高考, 类似每一次的模拟考试的成绩.  即使在模拟考试中, 考试成绩再好, 到实际高考, 考砸了还是对于上清华北大无济于事.

看, 机器学习中, 不仅要考察训练效果 in-sample-error $$E_{in}$$, 也要考察 outer-of-sample error $$E_{out}$$.

---

## 2.泛化误差

在 Learning from data 这本书中, 泛化误差的定义为: $$E_{in}, E_{out}$$之间的差异. 而也有人直接将$$E_{out}$$定义为泛化误差. 我们在此明确下使用前一种定义泛化误差, 可能处于直接使用 霍夫丁不等式(Hoeffding Inequality)不等式的考虑.(猜想) 反正我们能理解泛化误差就行.


在第一章中, 我们知道下面的霍夫丁不等式,

$$\Bbb P [\lvert E_{in}(g) - E_{out}(g)\rvert > \epsilon] \leq 2M e^{-2 \epsilon^2 N}, \forall \epsilon > 0$$

其中$$M$$为假设集 hypothesis set H 中所有假设 h 的数目, $$N$$ 为训练集 D 中训练样本数目.

如果我们选择一个 tolerance level $$\delta = 2M e^{-2 \epsilon^2 N}(\Rightarrow \epsilon = \sqrt{\frac{1}{2N} \ln{\frac{2M}{\delta}}})$$, 那么

$$E_{out}(g) \leq E_{in}(g) + \sqrt{\frac{1}{2N} \ln{\frac{2M}{\delta}}}) \tag{2.1}$$

出现在概率至少为$$1 - \delta$$, 因为只考虑单边嘛.

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

如果重叠区域越多, 其联合事件的概率要大大小于其所有时间发生概率的和. 这么说来, 我们可以将联合事件发生的概率进一步缩小. 也就是将霍夫丁不等式右边的概率进一步缩小. 但是有前提, 前提就是事件:

$$\lvert E_{in}(h_m) - E_{out}(h_m) \rvert > \epsilon; m = 1, \cdots, M$$

发生重叠的部分非常多, 如类似上图3个时间的重叠.

如果假设$$h_1$$和$$h_2$$非常相似, 那么两个事件$$\lvert E_{in}(h_1) - E_{out}(h_1) \rvert > \epsilon, \lvert E_{in}(h_2) - E_{out}(h_2) \rvert > \epsilon$$ 在大多数据集上同时发生的可能性非常大.

**在大多经典学习模型中, 许多假设非常相似.** 一旦我们合理解释不同假设之间的重叠性, 那么我们就可以用一个**有效数**来提到霍夫丁不等式(2.1)中的无穷大的M. 关键是如何得到这个**有效数**? 这个是难点, 涉及到数学理论. 下面我们来看看书中的讲解.

## 3.假设集有效数

书中引入增长函数(growth function)来量化假设集的有效数. 增长函数将替代不等式(2.1)中误差边界的M. 增长函数是量化假设集中假设不同的程度, 以及不同的事件发生多少重叠.

步骤:

1. 定义增长函数以及研究其基本特征;
2. 如何界定增长函数的值;
3. 证明增长函数替代误差边界中M的可行性.

经过这几步下来, 误差边界就可以使用在无穷大的M中啦, 因为它会被替代嘛. 好啦, 那么看看书中如何证明.

二进制目标函数为例. $$h(X) \rightarrow \{+1, -1\}; \forall h \in H$$

数据基础:  $$\cal D$$ 训练集(有限的样本), $$x_1, x_2, ..., x_N \in \cal D \subset X$$

**定义1**:

由假设集 $$\cal H$$ 生成在数据集$$\cal D$$上的生成的二进制(dichotomies)为:

$$\cal H(x_1, \cdots, x_N) = \{(h(x_1), \cdots, h(x_N) \mid h \in H \} \tag{2.3}$$

我们会发现, 别看形式这么复杂, 其实$$\cal H(x_1, \cdots, X_N)$$就是一个集合, 只不过该集合的元素是由$$\cal H$$中的假设来确定, 这些元素分别为tuple(元组, 类似 Python 中的 tuple). 这些元素tuple为$$(h(x_1), h(x_2), ..., h(x_N))$$, 因为是二进制目标函数, 那么其可能值为$$(1_1, -1_2, ..., 1_i, ..., 1_N)$$, 下标表示位数(或者说第i个训练样本$$x_i$$所对应假设输出).

那么我们可以看出, $$\cal H(x_1, \cdots, x_N)$$集合中的元素, 每一位上的选择只有2种(+1,-1), 那么我们可以计算这个集合中元素数目的最大值, 为$$2^N = 2_1\cdot2_2\cdots2_N$$

**定义2**: 增长函数的定义

上面集合$$\cal H(x_1, \cdots, x_N)$$的增长函数为

$$m_{\cal H}(N) = \max_{x_1, ..., x_N \in {\cal X}} \lvert {{\cal H}(x_1, ..., x_N)} \rvert$$

其中 $$\vert \cdot \vert$$ 表示几何中元素的数目, 不是绝对值.

那么从定义1中的讨论, 可以发现 $$m_{\cal H}(N) \leq 2^N$$

从集合$$\cal H(x_1, \cdots, x_N)$$中, 我们发现其元素是由 

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 2 Training VS Testing
2. 台大[机器学习基石 L5 slider](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/05_handout.pdf)
