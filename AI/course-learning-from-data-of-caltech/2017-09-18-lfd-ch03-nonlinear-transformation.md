---
layout: post
title: LFD第三章笔记:非线性转换(特征转换)
categories:
- MachineLearning
- LearningFromData
---

# 前言

在[LFD第三章笔记:线性模型](https://anifacc.github.io/machinelearning/learningfromdata/2017/09/14/lfd-ch03-linear-model/)中, 我们已了解线性模型中都使用下面的线性和式子.

$${\bf w^T x} = \vec w^T \vec x = \sum_{i=0}^d w_i x_i \tag{3.11}$$

式(3.11)中, 输入特征$$x_i$$ 和  $$w_i$$ 都是线性量. 如果输入特征 $$x_i$$ 是非线性, 该如何处理. 书中主要讲的就是关于这个问题的解决及一些理论分析.

## 1.Z 空间

> 转换空间

![1_z_space](https://dn-learnml.qbox.me/image/ai/lfd_ch03_z_space.JPG)

左上图中, 我们可以看出, 我们不能直接使用一条直线将它们分类出来. 而经过非线性变换后, 如右上图所示, 我们可以将这些数据点用直线分类出来.

这时候原特征空间 非线性变换到 Z 空间.

$${\bf x} = \begin{bmatrix} 1 \\ x_1 \\ x_2 \end{bmatrix} \rightarrow {\bf z} = {\bf\Phi( x)} = \begin{bmatrix} 1 \\ x_1^2 \\ x_2^2 \end{bmatrix} = \begin{bmatrix} 1 \\ \Phi_1(x) \\ \Phi_2(x) \end{bmatrix}$$

其中,

$$\Phi({\bf x}) = (1, x_1^2, x_2^2) \tag{3.2}$$

这时候, 假设集:

$$h({\bf x}) = \tilde h (\Phi({\bf x}))$$

X 空间 变化到 Z 空间之后, 就可以使用线性模型识别分类.

![2_linear_seperate](https://dn-learnml.qbox.me/image/ai/lfd_ch03_linear_z_space.JPG)

## 2.泛化

$${\cal X}: \Bbb R^d \rightarrow {\cal Z}: \Bbb R^{\tilde d}$$

经过非线性变化后, 感知器模型的 VC维数从 $$d+1$$ 变为 $$\tilde d + 1$$.

根据[泛化边界](https://anifacc.github.io/machinelearning/learningfromdata/2017/08/31/lfd-ch02-generalization-bound-interpretion-test-set/), 我们可以知晓, $$E_{out}, E_{in}$$ 非常接近, 误差范围在泛化边界内, 只要我们保证 $$E_{in}$$ 足够小就可以.

这里有一个 **前提**: 非线性变化不能在观察过数据之后确定, 在没有窥探数据的情况下(decide on the transform before seeing the data), 使用非线性变化, 泛化边界中的 $$d_{vc} = d_{vc}({\cal H_{\Phi}})$$ 作为其 VC维数. 如果 decide on the transforma after seeing the data, 会影响 VC边界中的 VC维数.

书中练习3.12可举例说明这一点.

![3_ex_3_12](https://dn-learnml.qbox.me/image/ai/lfd_ch03_ex3_12.JPG)

如果对于上面的非线性问题, 先直接使用线性模型, 发现不成功; 然后在使用非线性变化, 成功了. 此时, 假设集有效数就不再是简单的(a)或(b), 而是(c).

谨慎使用 degree-k 多项式变换

![4_k_degree_polynomial](https://dn-learnml.qbox.me/image/ai/lfd_ch03_k_degree_polynomial.JPG)

经过 $$\Phi_k({\bf x})$$ 变换后, 特征空间维数变为 $$\tilde d = \frac{k(k+3)}{2}$$. 这就增大 VC维数, 从而增长 VC泛化边界.

因此要谨慎使用该变换.

## 3.Sum

通过书上的3.4节, 了解如何将非线性数据变换为线性的数据. 但要注意非线性变换要在观察到数据之前, 而且需要谨慎使用, 以免增大 VC维泛化边界 以及造成过拟合问题.

---

# 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 1 & Chapter 3 The Linear Model
2. [Learning From Data: Lecture-Slides L10](http://www.cs.rpi.edu/~magdon/courses/LFD-Slides/SlidesLect10.pdf)

---

# ChangeLog

```
@Anifacc
read + exercise:  3: 14
note:             1: 12
all:              4: 26
note: 2017-09-18 beta 1.0 WX
```
