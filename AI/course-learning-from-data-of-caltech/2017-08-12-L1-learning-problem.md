# L1 The learning problem

讲师首先讲了课程大纲，所按逻辑为以下。

- 课程逻辑：
    - What is learning?
    - Can we learn?
    - How to do that?
    - How to do it well?

紧接着就是第一课的课程内容：机器学习案例（涉及机器学习本质），学习的要素，简单模型，学习类型和问题。

- 机器学习案例
- 学习本质
- 学习的组成部分
- 机器学习类别
- 最后的puzzle

## 机器学习案例

- Netfix 电影评分：Predicting how a viewer will rate a movie
    - 解决
        - 观众的喜好向量（喜剧，动作，爱情...）
        - 实际电影类别向量（喜剧，动作，爱情）
        - 从中学习，或距离，或其他，来rating一部电影
- 信用卡申请发放

## 机器学习本质

- 问题存在一定模式
- 这种模式我们无法以数学形式或公式确定（can not pin it down mathematically）
- 但是我们有的是**数据**（没有数据，就别想机器学习，没门儿）

## 学习的组成部分

- 输入 x
- 输出 y
- 目标函数 $$f: X \rightarrow Y$$
- 数据DATA： $$(x_1, y_1), (x_2, y_2), \cdots, (x_n, y_n)$$, n个样本
- 假设Hypothesis：$$g: X \rightarrow Y$$

这其实是机器学习的一个骨架。骨架上的肌肉就是一个个算法。（输入输出类似系统论中的框架：输入-系统-输出，这里机器学习，系统就变为：假设空间+算法）

目标函数其实是理想的，我们收集到的数据，y不可能与f(x)正好完全相等，肯定存在偏差，也就是说我们不可能找到这个完全一样的目标函数。但是我们可以找到一个类似的或者趋近与这个目标函数的函数，从哪里找呢，就从我们的 **假设空间（Hypothesis)** 中找。通过数据集，只要我们从假设空间中找到一个Hypothesis，比如g, 这个g满足一定要求，能将数据的模式辨别出来就行，那么我们也就基本完成机器学习的过程。

一张图说明：

![机器学习过程](https://dn-learnml.qbox.me/image/ai/learning-progress.JPG)

解决机器学习问题的两个要素：

- The Hypothesis Set 假设集或假设空间 $$H={h}, g \in H$$
- The Learning Algorithm 机器学习算法

从上面的图中，我们可以看出，解决机器学习问题的本质就是：

数据集中存在一种模式（假设为目标函数f），我们要从假设集或假设空间中找出（识别）这种模式（类似目标函数的假设函数g，世界太复杂，不可能完全识别，因为问题本身就不能用纯数学表示出来，这能用机器学习来解决）。

那么通过什么办法呢？从已知的数据集中，用算法来学习，找出（通过更新迭代）这个假设函数g的参数，直到满意为止（$$g \approx f$$, 识别出问题模式，准确性高）。

> 一个简单的假设集（假设空间）：感知器（Perceptron）

- 输入 $$\boldsymbol x=(x_1, x_2, \cdots, x_d)$$(数据特征)
- 假设：$$h(x)=sign(\sum_{i=0}^{d}w_i x_i) = sign(\boldsymbol w^T \boldsymbol x)$$
- 学习算法：感知器学习算法 PLA
  - 训练样本来了 $$(x_n, y_n)$$
  - $$sign(\boldsymbol w^T \boldsymbol x_n)\neq y_n$$
  - 更新假设函数h的参数 $$\boldsymbol w_{j+1} \leftarrow \boldsymbol w_{j} + y_nx_n$$

讲师讲解从直观上理解感知器算法，非常容易理解。向量内积，两向量夹角为锐角，则内积为正，若为钝角，则内积为负。参考下图，可直观理解感知器学习算法。

![PLA](https://dn-learnml.qbox.me/image/ai/PLA-obj.JPG)

若$$w, x$$成钝角，上图第一个向量图，则$$sign(w^T x)=-1 \neq y=(+1)$$，则需要修正$$w \leftarrow = w + yx$$ 得到出图中蓝色所示的更新后的$$w$$，这样该更新后的假设函数的参数$$w$$就与$$x$$成锐角，其$$sign(w^Tx)=+1 = y$$。

看，这样从直观上就容易理解啦。

---

## 机器学习类别

学习的基本前提：

> Using a set of observations to uncover an underlying process

- 监督式学习(supervised learning)
  - 训练数据集或样本集的特征和标签已知(input, output)
- 非监督式学习(Unsupervised learning)
  - (input, ?)
- 强化学习(Reinforcement learning)
  - (input, some output(对输出进行奖惩))

## 最后的PUZZLE

课程最后的Puzzle有意识。其实是没有标准答案的，我想怎么解释就怎么解释。能解释得通，就OK。

的确，在非完全精确的领域，为何要追求精确呢？

投资类似机器学习，并非那么精确的哦。

---

## Ref

1. [slides01.pdf](http://work.caltech.edu/slides/slides01.pdf)

```
@anifacc
2017-08-12 10:28:16 Wangxiang
```
