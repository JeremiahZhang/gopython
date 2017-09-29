---
layout: post
title: LFD第五章笔记:奥卡姆剃刀-有偏采样-数据窥探
categories:
- MachineLearning
- LearningFromData
---
书本[1]第五章主要讲述学习的三个原则:

- 奥卡姆剃刀(Occam's Razor): 与模型选择相关, pick a model carefully
- 有偏采样(Sampling Bias): 与采集数据有关, generate the data carefuly
- 数据窥探(Data Snooping): 处理数据相关, handle the data carefully

## 1.奥卡姆剃刀

> The simplest model that fits the data is also the most plausible.

- 2 Questions
    - 1. What does it mean for a model to be simple?
    - 2. How do we know that simpler is better?

(1) 思考第一个问题, 从霍夫丁不等式以及 VC边界来看, 哪个模型的复杂度(一个表征:假设集有效个数)小, 哪个模型就相对而言简单. 关于模型复杂度, 在不同的领域, 其表征形式不一样的. **A hypothesis set with simple hypotheses must be samll**.

例子:

> Axiom of non-falsifability: If an experiment has no chance of falsifying a hypothesis, then the result of that experiment provides no evidence one way or the other for the hypothesis.

学习中使用奥卡姆剃刀, 不仅仅是 "as simple as possible, but no simpler". 而是 "s simpler fit than possible", namely an imperfect fit of the data using simple model over a perfect fit using a more complex one. 前提是: 学习性能为保证. 如果两个学习性能相同, 那么选择简单的那个当然好.

---

## 2.有偏采样

书中举例: 1948年的美国大选 **Dewey defeats Truman**. 报纸用电话调查"美国人民"的民意, 大部分"美国人民"选择杜威, 报纸就预测杜威获胜, 还刊登到报纸上, 最后的结果是杜鲁门获胜. 为什么结果会这样? 采样有偏差. 1948年那个时代有电话的美国人民是相对有钱的人, 并不能代表所有美国人. 因此打电话采样是有偏采样, 导致的结果也是有偏的.

> If the data is sampled in a biased way, learning will produce a similarly biased outcome.

因此, 在采集样本时, 我们需要保证: 训练集, 测试集都要来自相同的分布. 这样样本具有无偏性.

---

## 3.数据窥探

> If a data set has affected any step in the learning process, its ability to assess the outcome has been compromised.

我们需要[2]:

- estimate performance with a completely uncontaminated test set
- and choose H before looking at the data. (霍夫丁不等式的前提: 先确定 H, 再生成数据集. 学习可行性)

![01_rsearch](https://dn-learnml.qbox.me/image/ai/lfd_ch05_01_research.JPG)

数据窥探的发生情况:

- reuse of the same data set.
    - 举例: 科研论文, 结果总是往好的方向发展.
    - 我们常用的数据集, 在前人分析结果基础上, 我们再进行机器学习. 此种情况和科研论文类似.
    - 虽然结果会很好, 但是泛化能力不行, 因为 VC维数会变大(所有假设集的并集嘛).
- 在观察过数据之后, 进行模型选择, 也会出现问题.

解决:

- 避免窥探数据. 用于评估最终假设的数据, 我们最好把它们放在"安全"地方, 只有在确定最终假设的时候, 我们再来使用. 如果一个数据集在训练过程中被使用, 那么这个数据集在测试时就相当于已经被污染.
- 了解数据窥探, 参考书籍[1] 176页.

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 1 & Chapter 3 The Linear Model
2. [Learning From Data: Lecture-Slides L14](http://www.cs.rpi.edu/~magdon/courses/LFD-Slides/SlidesLect14.pdf)
3. [台大机器学习基石-L16_handout.pdf](http://www.csie.ntu.edu.tw/~htlin/mooc/doc/16_handout.pdf)

---

## ChangeLog

```
@Anifacc  
read:  2: 39
note:  0: 30
all:   3: 09
2017-09-29 beta 1.0 WX
```
