# L2 and Sec1.3 Is Learning Feasible?

学习可行么? 学习的目标是目标函数f. 但是 f 未知, 未知, 未知.

在监督式学习中, 我们关注的是:

- Unkown target function $$y = f(x)$$
- 训练集 dataset $$(x_1, y_1), \cdots, (x_N, y_N)$$
- Learning algorithm picks $$g \approx f$$ from a hypothesis set H.

我们的算法只能从训练集中得到 hypothesis $$g$$, 但是对于来自非训练集的新的样本, 一定能保证学习得到的 $$g$$ 能正确预测么?

---

## 1.Is learning feasible?

学习的目标: the target function f, 但是这个 f 的的确确未知. 我们有的是一些数据data, 但问题来了, 我们不可能获得无穷多的数据, 采集到的数据数目有限, 这些有限的数据如何能让我们达到学习的目标--得到这个 target function f?

在上节课最后, 讲师讲了一个puzzle.

![lfd-puzzle](https://dn-learnml.qbox.me/image/ai/lfd-puzzle.JPG)

从已知的数据(训练样本)中, 我们其实无法确定这个 f 到底是多少的?

比如: f1为(左上角黑色:-1, 左上角白色:+1),f1(新样本)=-1.

又如:f2为(黑色图形非对称:-1, 黑色图形对称:+1), 因此 f2(新样本)=+1.

所以, 我们无法从已知的数据, 我们可能无法完全确定 f. 但这并不意味着学习是不可行的.

从上例中, 我们看到, 我们选择的学习规则(hypothesis)不同, 对与新样本预测的结果也不同. 这是不是看上去有点糟糕啊!!!

---

## 2.Outside the Dataset

在Puzzle案例中, 训练集Dataset是图形中上面两行的图像, 我们知道未知目标函数 f 在这些样本上的输出.

- f(样本来自第一行) = -1,
- f(样本来自第二行) = +1,

我们只知道 f 在样本上的结果, 不代表已经学到或得到这个 f, 因为我们无法保证 f 在非训练集(outside the Dataset)上样本的结果. 就如这里, 不同的规则下f1 或 f2, 我们可以得到不同的结果.

那么问题来了.

> Does the data set D tell us anything outside of D that we didn't know before? If the answer is ==yes==, then we have learned something. If the answer is ==no==, we can conclude that learning is not feasible.

再来看一个例子.

![lfd-boolean-example](https://dn-learnml.qbox.me/image/vi/lfd-boolean-example.JPG)

已知5个训练集数据样本$$(x_1, y_1), \cdots, (x_5, y_5)$$. 总共有8个样本, 其中5个样本的特征x和类别已知. 还有三个样本, 我们知道其特征 x, 但并不知道其类别.

- x 每一位的取值只有0或1, 则总有$$2^3=8$$中不同的样本x. 即总的输入空间X样本量为8.
- y 表示类别, 两类, 白点(+1)和黑点(-1).

在输入空间X (y未知的情况下)上, 我们可以计算所有可能的 target function f的数目: $$2^8 = 256$$.

现在我们有训练样本啦,就是上面的5个(x, y). 我们可以将 target function f 的数目减少到 8个, 这个通过枚举得到, 如下表所示.

![lfd-boolean-example-hypothesis](https://dn-learnml.qbox.me/image/vi/lfd-boolean-example-hypothesis.JPG)

这样, 如果 g 在所有训练集上都分类或预测正确, 那么在未知数据上, 其可能性就有8种情况, 如上表所示. 我们无法确定到底选择哪一个会比较好. 这就是问题所在.

> Whether 1 has a hypothesis that perfectly agrees with D (as depicted in the
table) or not, and whether the learning algorithm picks that hypothesis or
picks another one that disagrees with D (diﬀerent green bits) , it makes no
diﬀerence whatsoever as far as the performance outside of D is concerned. Yet
the performance outside D is all that matters in learning!

这个问题不仅局限于上面的案例, 这涉及到一般性的学习问题.

>  As long as f is an unknown function, knowing D cannot exclude any pattern of values for f outside of D. Therefore, the predictions of g outside of D are meaningless.

但这就能说明学习不可行么(要不然就没有机器学习啦), 不能!可用 **概率** 来解决这个问题. 概率是个好工具. 一定要懂些概率哦.

番外: 这个可以用于企业分析或金融分析中, 同样, 过去历史数据, 我们可能得到一个模型g, 但是这个g在未来(未知数据)表现如何, 太不确定啦. 我们还是得用 **概率** 来解决问题. 这个世界本来就是充满不确定的嘛.

---

## 3. 概率解决

课程中, 讲师先从概率中的案例出发.

![lfd-marbles-01](https://dn-learnml.qbox.me/image/ai/lfd-marbles-01-experiments.JPG)

- 一个罐子中有许多小球(可能无限多个-大数定理,才有会下面的概率), 从中取一个小球,
  - 取得红球的概率为 $$P(红球) = \mu$$,
  - 取得绿球的概率为 $$P(绿球) = 1 - \m
u$$
- 我们不知$$\mu$$是多少;
- 我们有返回的从中随机选取N个独立的小球,作为样本
- 在这N个样本中, 红球所占的比率为 $$\nu$$

从大数定理角度来看, 如果N无限大, 那么$$\nu \approx \mu$$, 但其实我们的N不可能无穷大. N总会是有限的. 这有限个N中, 有可能取出的球全是绿球, 也有可能取出的球全是红球.

因此$$\nu$$在一定意义上能代表 $$\mu$$么? 只有在N足够大的时候, 两者接近. 为说明两者的关系, 引入霍夫丁不等式(hoeffding Inequality).

$$\boldsymbol P[|\nu - \mu| > \epsilon] \leq 2e^{-2\epsilon^2N}$$

$$|\nu - \mu| > \epsilon $$ 发生的概率虽然与其中三者都有关, 但是其边界依赖于$$\epsilon$$ 和样本数量N. 我们只知道$$\nu$$依赖于我们的N个随机样本, $$\mu$$并不是随机的, 它是个常数, 也只有上帝知道它是多少.  

通过霍夫丁不等式, 我们可以使用$$\nu$$来推测$$\mu$$, 虽然是$$\mu$$影响着$$\nu$$. 如果$$\nu \rightarrow \mu$$, 那么我们可以推测 $$\mu \rightarrow \nu$$.

好了, 我们可以将其进行拓展类比到学习问题中.

![lfd-marbles-02](https://dn-learnml.qbox.me/image/ai/lfd-marbles-02-related-learning.JPG)

如上图所示, 罐子中同样有许多小球(样本空间X), 我们学习的目标是 target function f(), 在这个罐子中, 我们按下面的方法来给小球的"上色".

- 如果小球x 输入一个 hypothesis h中, 其输出 $$h(x) = f(x)$$, 则给小球涂成绿色;
- 相反的, 如果$$h(x) \neq f(x)$$, 则定小球涂成红色.

如此, 我们就得到与之前罐子中类似的绿球和红球, 这是其中的$$P(红球)= \mu$$ 对于我们而言未知, 因为我们并不知道目标函数 target function f(这个 target f 我们正在苦苦寻找).

现在将之前学习的过程重新展示一下:

![lfd-marbles-03-progress](https://dn-learnml.qbox.me/image/ai/lfd-marbles-03-learning-diag-pro.JPG)

训练集是从样本空间X(一定的概率分布)中得到的. N个训练集就类似于我们随机从罐子中取得的N个样本小球.

这时候, 如果我们通过算法A训练从假设集 hypothesis set 中确定了一个假设 h, 那么这个假设 h 在训练集(x)上, $$h(x) = y = f(x)$$, 则该样本小球x为绿球, 否则 $$h(x) \neq y = f(x)$$该样本小球x为红球. 这就会得到在红球占N个样本球总数的比为$$\nu$$.

从中我们看出, $$\nu$$ 取决于我们选用的假设.在实际问题中, 算法A其实在假设集中搜索误差小的假设. 单单以一个假设来看, 我们不是在学习, 算法A学习是要检验好多假设. 因此我们还得继续. 多个假设, 就有多个不同的 $$\nu, \mu$$(他们依赖于假设h). 如下图所示:

![lfd-marbles-04bin](https://dn-learnml.qbox.me/image/ai/lfd-marbles-04bin-multiple.JPG)

现在我们用不同的表示法来表示$$\mu, \nu$$, 便于我们更好理解学习的问题.

- $$E_{in}(h) := \nu$$: hypothesis h 在训练样本D上(in sample)与 target f 不同的比率 (在训练样本上出错率, 训练样本中红球占比嘛)
- $$E_{out}(h) := \mu$$: hypothesis h 在 "out of sample" 上与 target f 不同的比率(在样本空间X上的出错率, 罐子中红球占比)

如下图所示, 单个 hypothesis h 下 $$E_{in}(h), E_{out}(h)$$
![lfd-marbles-05](https://dn-learnml.qbox.me/image/ai/lfd-marbles-05-ein-eout.JPG).

对于学习的过程(算法假设集中搜索), 就会出现多个类似的 bin, 如下图所示:

![lfd-marbles-06](https://dn-learnml.qbox.me/image/ai/lfd-marbles-06-multi-bins-ein.JPG).

到这里为止, 我们利用霍夫丁不等式, 对于单个hypothesis h, 我们有:

$$P[|E_{in}(h) - E_{out}(h)| > \epsilon] \leq 2e^{-2 \epsilon ^2 N}, \ for \ any \ \epsilon > 0$$

其中, N就是训练样本的数目. The in-sample(单单训练样本集上) error $$E_{in}$$ 和$$\nu$$类似, 是个依赖于样本的随机变量. 而 out-of-sample(整个样本空间X上) error $$E_{out}$$ 和 $$\mu$$ 类似, 对于我们而言是个未知量, 但不是随机量.

对于一个假设集 $$H = \{ h_1, h_2, ..., h_M \}$$.

**这里, 我们是先确定 hypothesis, 然后再生成数据集(训练集), 上面霍夫丁不等式中的概率也是和随机数有关.**

证明霍夫丁不定式成立的前提: h is fixed before you generate the data set

> we emphasize that the assumption "h is fixed before you generate the data set" is critical to the validity of this bound. If you are allowed to change h after you generate the data set, the assumptions that are needed to prove the Hoeffding Inequality no longer hold.

在学习的过程中, 算法选择最终的hypothesis g是在训练集(data set D)确定之后.

所以, 我们不能简单用 g 替换 霍夫丁不等式中的 h.

我们以另一种方法来确定 $$P[|E_{in}(g) - E_{out}(g)| > \epsilon]$$ 的边界. 因为 g 不管算法和训练集(sample)如何, g 总是从 假设集 H 中选取(error 最小), 则

$$\begin{align}
|E_{in}(g) - E_{out}(g)| > \epsilon &\Rightarrow |E_{in}(h_1) - E_{out}(h_1)| > \epsilon \\
    & or \ |E_{in}(h_2) - E_{out}(h_2)| > \epsilon \\
    & \cdots \\
    & or \ |E_{in}(h_M) - E_{out}(h_M)| > \epsilon \end{align}$$

那么:

$$\begin{align}
P[|E_{in}(g) - E_{out}(g)| > \epsilon] &\leq P[|E_{in}(h_1) - E_{out}(h_1)| > \epsilon \ or \cdots or |E_{in}(h_M) - E_{out}(h_M)| > \epsilon] \\
&\leq \sum_{m=1}^{M} P[|E_{in}(h_M) - E_{out}(h_M)| > \epsilon]
\end{align}$$

对于每个 hypothesis h, 我们可以使用霍夫丁不定式, 因此

$$P[|E_{in}(g) - E_{out}(g)| > \epsilon] \leq 2Me^{-2 \epsilon ^2 N}$$

---

## 4.学习是可行的

两个论点:

- We can not learn anything outside of D
- the other says we can!

这两个论点互相矛盾, 我们该怎么办呢?

> 1. The question of whether D tells us anything outside of D that we didn't know before has two diﬀerent answers.
>     - If we insist on a deterministic answer, which means that D tells us something certain about f outside of D, then the answer is no.
>     - If we accept a probabilistic answer, which means that D tells us something likely about f outside of D, then the answer is yes.

关键还是从概率角度来看. 书本练习1.11 非常有意思, 从中看出, 训练样本D情况和样本空间X的概率分布情况, 在某种程度影响着算法的性能(在 outside D 上).

> 2. what we mean by the feasibility of learning

学习产生一个好的假设, 让这个$$g \approx f$$. 如果学习成功, 则 $$g \approx f$$, 两者差别很小, 即 $$E_{out}(g) \approx 0$$. 但是在上面概率角度分析中, 我们得到的霍夫丁不等式并不能说明这点啊. 我们只能得到 $$E_{out}(g) \approx E_{in}(g)$$. 所以我们还得再前进一步, 让$$E_{in}(g) \approx 0$$, 从而得出 $$E_{out}(g) \approx 0$$.

我们不能保证一定能找出这样一个假设g使得 $$E_{in}(g) \approx$$, but at least we will know if we find it. target f 未知, 则 $$E_{out}(g)$$也未知, 我们只能知晓$$E_{in}(g)$$. 之后通过霍夫丁不等式

$$P[|E_{in}(g) - E_{out}(g)| > \epsilon] \leq 2Me^{-2 \epsilon ^2 N}$$

我们就能确定$$E_{in}(g) \approx E_{out}(g)$$, 从而用 $$E_{in}$$来代表 $$E_{out}$$.

走了这么多路, 就是想说明学习是可行的.

学习可行性再最后划分为两个问题:

1. Can we make sure that $$E_{out}(g)$$ is close enough to $$E_{in}(g)$$?
2. Can we make $$E_{in}(g)$$ small enough?

霍夫丁不等式只能解决第一个问题. 第二个问题只能在学习算法在实际训练集上跑过之后才见分晓.

如果游戏继续的话, 我们可以进一步观察 (1) the complexity of H, and (2) the complexity of f.

(1)**The complexity of H**. 假设集H的数目可以作为反映假设集的复杂度(complexity), 如果 M 增大, 则不等式左边的霍夫丁边界值会变大, 从而到此 $$E_{in}(g)$$ 可能不能很好评估$$E_{out}(g)$$, 但如果 M 大, 则我们从更多的H中得到的某个 g, 它的$$E_{in}(g)$$很小. 因此, 假设集H的复杂度是学习理论中需要研究的内容.

(2) **The complexity of f**. 直观而言, 复杂的目标函数 f 比 简单的更加习得. 但从霍夫丁不等式来看, 我们看不出 f 的复杂性怎样影响 $$E_{in}(g) \approx E_{out}(g)$$. 因为不论f的复杂度如何, 假设集 和 训练样本数确定, 我们就得到相同的霍夫丁边界. 这并不代表从复杂的f中学习与从简单的f中一样容易. 因为霍夫丁不等式只等解决学习可行性的第一个问题. 如果目标函数f复杂, 来自于复杂 f 的数据比来自简单 f 的 数据更难拟合. 这意味着, 从来自复杂 f的数据中学习, 我们可能得到更糟糕的$$E_{in}(g)$$. 如果提高假设集H的复杂度, 以便得到小的$$E_{in}(g)$$, 但这时$$E_{out}$$ 将不再与 $$E_{in}$$接近, 这个可以结合第(1)点和霍夫丁不等式看出来. 不管怎样, 从复杂的f 中学习难度比预期的大. 极端情况下, 如果f太复杂, 我们可能不能从中学习.

从分析来看, 学习挺难的哦. 但实际中, 大多目标函数没那么负债, 我们还是可以从中学习.

只要我们确定 霍夫丁不等式的边界, 我们学习的成败就在于我们从训练样本中的训练情况.

```
@anifacc
2017-08-17 17:38:08
```
