---
layout: post
title: LFD第四章笔记:Overfitting
categories:
- MachineLearning
- LearningFromData
---

书本[1]第四章第一节内容主要讲述 overfitting 相关内容, 主要为:

- what 什么是 overfitting(过拟合)?
- when 什么时候出现 overfitting?
- Stochastic Noise 与 Deterministic Noise

## 1.What is overfitting?

书本以 [Paraskevedekatriaphobia
– fear of Friday the 13th](https://en.wikipedia.org/wiki/Friday_the_13th) 的迷信为例, 以人的 overfitting 类比机器的 overfiting. 作者真会类比, 我们想想也挺合理的. 人们在过去事件基础上, 搞出 Paraskevedekatriaphobia 这样的迷信, 类似"overfitting". 机器学习中的 overfitting 类似, 在现有数据上学习模型, 到未见数据上的效果不好, 甚至很差.

那么什么是 "overfitting"(过拟合)? 书中如下:

> Overftting is the phenomenon where fitting the observed facts (data) well no longer indicates that we will get a decent out-of-sample error, and may actually lead to the opposite effect.

那么我们可不可以这样理解:

一个模型(假设集 $$\cal H$$) 在训练集D上的训练效果非常好, 得到最终假设为$$g$$, 其$$E_{in}(g) \approx 0$$, 但是在未知数据上(输入空间中的样本), 其效果非常差, $$E_{out}$$ 非常大.

比如下面一个简单的 overfitting 例子.

![1_overfitting_example](https://dn-learnml.qbox.me/image/ai/lfd_ch04_01_overfitting_example.JPG)

上面就是典型的overfitting: simple target with excessively complex H.

- 目标函数为 二次曲线 如蓝色曲线所示
- 训练样本数: 5个
- 一点点误差: (测量误差 or 观测误差)
- 训练得到: 4阶多项式曲线

从上图中我们可知晓: $$E_{in} \approx 0; E_{out} \gg 0$$

为什么会发生? 噪声影响. (如果数据多一些, 还会出现过拟合吗? 数据多一些, 噪声也多一些, 直觉是有可能出现过拟合.)

> overfitting is not just bad generalization.

从上面来看, overfitting 会出现 $$E_{in}$$小, 而 $$E_{out}$$大, 我们可以说 overfitting 就等于泛化能力差么? 如果出现 overfitting, 那么模型泛化能力是差, 但 overfitting 不仅仅只是泛化能力差.

![2](https://dn-learnml.qbox.me/image/ai/lfd_ch04_02_bad_generalization.JPG)

泛化不好, 是 VC 边界太大.

![3](https://dn-learnml.qbox.me/image/ai/lfd_ch04_03_overfitting.JPG)

Overfitting 中, $$E_{in}$$ 越来越小, 而 $$E_{out}$$ 越来越大.

那么问题来了, 什么时候会出现 overfitting 呢?

---

## 2.When does overfitting occur?

多项式线性回归中的 Overfitting.

- 数据特征: 1 维
- 线性模型: 线性回归(多项式) 特征变化 $$x \rightarrow (1, x, x^2, ...)$$

下图是数据与目标函数(现实中, 我们不可能知晓目标函数的, 这是假设目标函数知晓情况下展开讨论).

![4](https://dn-learnml.qbox.me/image/ai/lfd_ch04_04_overfitting_case.JPG)

上面左图的目标函数是10阶的多多项式形式. 而数据是带噪声的数据; 右图是50阶的目标函数, 数据不带噪声. 我们分别使用 $$\cal H_2, H_{10}$$ 二阶多项式和10阶多项式拟合.

拟合结果如下图所示:

![5](https://dn-learnml.qbox.me/image/ai/lfd_ch04_05_overfitting_case_study_results.JPG)

1. 在10阶目标函数, 噪声数据的情形下, 2阶多项式拟合比10阶多项式拟合效果好.
  - $$E_{in}({\cal H_2}) = 0.050 > E_{in}(\cal H_{10}) = 0.034$$, 2阶多项式拟合的 in-sample error 比 10阶稍微大一些;
  - 但是 $$E_{out}({\cal H_2} = 0.127 < E_{out}({\cal H_{10}}) = 9.00$$, 2阶多项式拟合的 out-sample error 远比 10阶小.
2. 更复杂的目标函数: 50阶; 数据无噪声情形下, 2阶拟合的效果要比10阶的好.

从上面的例子, 我们可以看出, 越简单的假设集 $$\cal H$$ 对于无噪声数据及复杂目标函数拟合的效果更好些.  

但是现实中不存在无噪声数据. 而$$\cal H$$ 只能从数据中学习得到最佳假设 $$g$$, 因此, 数据中有噪声(Noise), 便会使得拟合不准确, 也就是拟合时, 连 Noise那部分也一块学习咯. 模型才不管你的数据哪些是真实的, 哪些是 Noise 的部分呢. 不过人就可以.

> When is $$\cal H_2$$ Better than $$H_{10}$$?

![6](https://dn-learnml.qbox.me/image/ai/lfd_ch04_06_overfitting_learning_curves.JPG)

上图中, 数据集个数对两个假设的学习结果有一定影响. 在阴影部分, $$\cal H_2$$ 的 $$E_{out}$$ 值要比 $$\cal H_{10}$$ 要小, 但超出阴影部分, 就正好相反. 是不是可以说: 模型越复杂, 我们所需要的训练样本也更多, 才能保证复杂模型的效果比简单模型的拟合效果要好呢?? 但这种情况下, 模型对 noise 的学习程度也大呢?? 这是个问题, 暂且没有结论.

书中中又研究了那些因素对 overfitting 的影响, 以$$E_{out}({\cal H_{10}}) - E_{out}({\cal H_2})$$ 作为 overfit measure. 如下图所示.

![7](https://dn-learnml.qbox.me/image/ai/lfd_ch04_07_overfitting_measure.JPG)

- 三维图
- 横坐标为样本数目
- 纵坐标, 左图为 噪声水平(方差); 右图的为 目标函数复杂度 $$Q_f$$
- 颜色表示: overfit measure.

观察可以发现:

1. 样本数目增加, overfitting 程度增加
2. Noise 增加, overfitting 程度增加
3. 目标函数复杂度增加, overfiting 程度增加.

---

## 3.Noise

Noise 是什么? 在书本第一章讲过 Noise. 在实际中, Noise:

> The part of y we cannot model.

- Stochastic and
- Deterministic Noise

![9](https://dn-learnml.qbox.me/image/ai/lfd_ch04_09_stochastic_noise.JPG)

我的理解: stochastic noise 就是数据值与真实值之间的差异, 可能是随机性, 也有可能是测量时产生的差异. 这个 Noise , 在模型没有学习的情况下, 就已经存在. 下面的是 Deterministic Noise.

![10](https://dn-learnml.qbox.me/image/ai/lfd_ch04_10_det_noise.JPG)

如果我们得到一个最佳假设$$g$$, 那么这个最佳假设与目标函数之间的差异部分就是: **deterministric noise**. 这个所谓的 Noise, 在确定最终的假设之后, 才可能得到.(实际中我们无法得到, 因为目标函数永远无法知晓.)

学习算法不应该从 noise 中来学习, 但是算法无法分辨哪些部分是真实信号, 哪些是 noise. 如果数据集中样本数目有限, 则算法就会使用一些自由度来拟合噪声, 这就导致为 overfitting 和 伪最终假设.

两种噪声对 overfitting 有同样的影响. 但也有区别.

- (1) 重新产生测量样本数据值 $$y_n$$ , stocha.noise 会改变, 而 det.noise 不改变
- (2) 改变假设集 $$\cal H$$, stocha.noise 不变, 而 det.noise 则改变.

这是容易理解的. stocha.noise 与假设集无关, 与测量有关; det.noise 与 目标函数, 假设集有关.

![8](https://dn-learnml.qbox.me/image/ai/lfd_ch04_08_noise.JPG)

在 [bias-variance 分解](https://anifacc.github.io/machinelearning/learningfromdata/2017/09/07/lfd-ch02-bias-variance-learning-curve/)中, 我们得到在多个数据集下 out-sample error 期望的表达式.

$$\Bbb E_D[E_{out}(g^{(D)})] = \sigma^2 + \ bias + \ var$$

头两项就反映出 sto.noise($$\sigma^2$$ 反映) 和 det.noise (bias 反映) 的影响. 而 var 这一项受这两种噪音的间接影响.

> The var term is indirectly impacted by both types of noise, capturing a n1.odel's susceptibility to being led astray by the noise.

---

## 4.Sum

阅读书本4.1节, 了解了(1)什么是 overfitting; (2) 什么时候会产生 overfitting 及(3) overfitting 产生的原因.

那么如何来解决 overfitting 这类问题呢?

overfitting 的解药是:

- Regularization
- Validation

会在下面的章节中解释.

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 1 & Chapter 3 The Linear Model
2. [Learning From Data: Lecture-Slides L11](http://www.cs.rpi.edu/~magdon/courses/LFD-Slides/SlidesLect11.pdf)

---

## ChangeLog

```
@Anifacc
reading: 4: 34
note:    2: 24
all:     6: 58
2017-09-19 beta 1.0 WX
```
