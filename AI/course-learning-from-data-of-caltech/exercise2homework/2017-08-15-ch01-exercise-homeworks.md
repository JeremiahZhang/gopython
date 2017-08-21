# Exercises

## P4 ex1.1

1. Medical diagnosis:
  - 输入空间X：病人的症状。
  - 输出空间Y：病人得了啥病
2. Handwritten digit recognition
  - 输入空间X：邮政编码的数字图片 pixel
  - 输出空间Y：数字（到底是什么数字）
3. Determining if an email is spam or not
  - 输入空间X：邮件（内容）
  - 输出空间Y：是垃圾邮件还是非垃圾邮件
4. Predicting how an electric load varies with price, temperature, and day of the week
  - 输入空间X：price, tepmerature, and day of the week
  - 输出空间Y：electric load
5. A problem of interest to you fr which there is no analytic solution, but you have data from which to construct an empirical solution.
  - X：data of problem
  - Y：solution

## P6 ex1.2

a. 广告，购物，情色，发票，商店，打折，影片...
b. 亲人，学习，...
c. Threshold or b

## P7 ex1.3

a. 如果x(t)被错分，实际的y(t)和$$\vec w^T(t)\vec x(t)$$异号，即$$y(t)\vec w^T(t)\vec x(t) < 0$$，要不然就分类正确。
b. $$\begin{align}
y(t) \vec w^T(t+1) \vec x(t) &= y(t)[\vec w^T(t)+y(t)\vec x(t)] \vec x(t) \\
&= y(t)\vec w^T(t) \vec x(t) + y^2(t) \vec x^T(t) \vec x(t) \\
& >  y(t)\vec w^T(t) \vec x(t)
\end{align}$$ （第二项大于0）
c. 从a和b可以看出，如果x(t)被错分，则会修正权重$$\vec w(t+1) = \vec w(t) + y(t)\vec x(t) $$, $$y(t)\vec w^T(t) \vec x(t)$$从原来的 $$<0$$，慢慢会变成 $$>0$$. 最后 $$y \vec w^T x > 0$$, x 被正确分类。

## P8 ex1.4

产生数据，使用python编程来尝试一些。

## p17 ex1.7

**The purpose of the exercise is to show what can possibly happen outside the data, namely anything, and it is the same no matter how you pick your g from the data.**

a. 全是黑点和全是白点的H 与 g 总非训练样本上的差异。若H全是黑点，则与8个可能的g在非训练样本上预测的差别：H与g在三个点预测全错的g个数为1个，H与g在一个点上预测一样的g个数3个，H与g在两个点上预测一样的g个数为3个，H与g在三个点上预测一样的g的个数为1个。 全是白点一样的道理。（1-3-3-1）
b. 若选择匹配数据集最少的假设，则选择全是白点的，结果是和上面一样。
c. H是异或逻辑集。则H在未知样本上的预测f2一样。
d.  the learning a lgorith m picks the hypothesis that agrees with a l l training examples, but otherwise disagrees the most with the XOR. H包含所有可能的假设，而算法选择的是：在训练机集上，h(x)结果一样的假设，而在未知数据上的与XOR差别最大的假设。即f7，f7在训练集上预测为XOR逻辑，而在未知数据上，预测完全与XOR逻辑相反（差异最大）。

## p19 ex1.8:

> If µ = 0.9, what is the probability that a sample of 1 marbles will h ave v <= 0.1? [Hints: 1. Use binomial distribution. 2. Te answer is a ver small number.]

有放回的取10个弹球, 其中全是绿色球X=0和只有一个是红色球X=1的概率。X表示红色球数目。

$$P(\nu <= 0.1) = P(X=0) + P(X=1) = 0.1 ^ 10 + C_10^1 \cdot 0.9 \cdot 0.1^9 = 9.1 \cdot 10^{-9}$$

## P19 Exercise 1.9

> If µ = 0 .9, use the Hoeffding I nequality to bound the probability that a sample of 10 marbles will have v <= 0.1 and compare the a nswer to the previous exercise.

$$P(\rvert \nu - \mu \rvert ) > 0.8^{-}) \leq 2e^{-2*0.8^2*10} = 5.5 * 10^{-6}$$

## P23 ex1.10

不理解如何进行试验，问题到底是什么意思

## P25 ex1.11

**训练集**：给定训练集D的样本数为25.

**未知的目标函数** $$f: X \rightarrow Y, \ X = \boldsymbol R, \\ Y=\{-1, +1\}$$

**假设集**: 为了学习得到未知的目标函数f, 使用简单的假设集 $$H = \{h_1, h_2\}$$, 其中$$h_1=+1$$(任何训练样本输入进来，输出都为+1); $$h_2=-1$$(如何训练样本输入进来，输出都为-1).

**学习算法**：S(smart) 和 C(cracy).

- S 算法对于训练集中样本类别数多的就判别为该类别, 即如果训练集中类别为+1的样本数>类别为-1的样本数目, 则算法S将选择$$h_1$$假设作为g, 反之则选择$$h_2$$.
- C 算法就是个“疯子”, 所做所谓与S相对,只要S选了$$h_1$$假设, 则C算法就故意选$$h_2$$假设作为g.

**概率分布**: 我们要从确定性观点和概率的观点看看这些算法在训练样本上的性能. 从概率的角度来看:X上存在概率分布,其 $$P[f(x)=1] = p$$.

> a) Can S produce a hypothesis that is guaranteed to perform better than random on any point outside D?

NO. 无法保证. 极端例子, D中所有样本 yn=+1.

> b) Assume for the rest of the exercise that all the examples in have Yn = 1. Is it possible that the hypothesis that C produces turns out to be better than the hypothesis that S produces?

Yes. 算法S确定的假设为h1,而算法C确定的假设为h2. 那么在未知数据上, C的性能有可能比S的性能好.

> c) If p = 0.9, what is the probability that S will produce a better hypothesis than C?

p = 0.9 即 $$P(f(x)=+1) = 0.9$$, X 中有90%的概率能抽出类别为+1的样本,有10%的概率能抽出类别为-1的样本. 我们要求的是: $$P(P(h_S(x) = f(x)) > P(h_C(x) = f(x)))$$ 这个概率. x 为 outside D. 训练集以外的样本.$$h_S, h_C$$分别为算法C,D在训练集上训练得到的假设.

现在我们已知的量有哪些呢?

- D所有中所有样本 yn = +1.------> $$h_S = h_1, h_C = h_2$$.
- 因为 $$P(f(x)=+1) = 0.9 \rightarrow P(h_S(x) = f(x)) = 0.9$$
- 因为 $$P(f(x)=-1) = 0.1 \rightarrow P(h_C(x) = f(x)) = 0.1$$

因为: 0.9 > 0.1 所以 $$P[P(h_S(x) = f(x)) > P(h_C(x) = f(x))] = 1$$

> d)  Is there any value of p for which it is more likely than not that C will produce a better hypothesis than S?

前提还是要记住: 所有训练样本的yn=+1. 仍延续 b, c的条件和结论

问题是:  如果要 $$P(h_S(x) = f(x)) < P(h_C(x) = f(x))$$, 则p的取值如何.

因为: $$P(h_S(x) = f(x)) = p, \ P(h_C(x) = f(x)) = 1-p$$. 则 $$p < 1-p \rightarrow p< 0.5$$

> 练习总结:

其实从这4个问题中,我们可以发现,对于a问题,我们不确定训练样本D中yn的情况,我们就无法确定算法S在训练集D上得到的假设在X上的性能就好于C算法的情况.

但如果我们确定D中样本的情况,比如已知所有样本yn=+1, 则我们知道S和C算法得到的假设.

进一步下去, 如果我们知道 outside D 以外的样本 X 的概率分布, 那么我们可以进一步确定, S算法和C算法得出假设在 X 上的性能情况.

从中可以看出, 训练样本情况和X的概率分布情况, 在某种程度影响着算法的性能(在outside D上).

## P26 ex1.12

问题: learning problem, 目标函数 f 未知, 已知4000个数据. 我们要得到hypothesis g 来尽可能趋近 f. What is the best that you can promise her among the fllowing:

> a. After learning you will provide her with a g that you will guarantee approximates well out of sample.

> b. After learning you will provide her with a g, and with high probability
the g which you produce will approximate well out of sample.

> c.  One of two things wil l happen.
>    - you will produce a hypothesis g
>    - you will declare the you failed.
>    if you do return a hypothesis g, then with high probability the g which you produce will approximate f well out of sample.

a. 从ex1.11的练习中, 我们可以看出 a中 我们是无法保证的.
b. 还是从练习1.1.中, 我们发现, 只要在知道这4000个数据集D的情况 以及 未知样本X的概率分布情况, 我们才能得到相关的概率.
c. 综合来看, c答案可能是一个比较好的选项.(未知数据的不确定性.)

或许,我们能给出的只有 Hoeffding Inequality.

但是, 可不可以有这样的答案呢?

> d. With high probability: you will either say you failed or you will produce a good g.

## P31 EX1.13

已知: h & target f, and $$P(h(x) \neq f(x)) = \mu, P(h(x)=f(x)) = 1 - \mu$$, we use the same h to a pproximate a noisy version of f given by

$$P(y|x) = \begin{cases}
\lambda & y=f(x)\\
1 - \lambda & y \neq f(x)\end{cases}$$

> a) what is the probability of error that h makes in approximating y if we use a noisy version of f.

要求: $$P(h(x) \neq y)$$

- 第一种情况: $$h(x) = f(x), y \neq f(x)$$, 其概率: $$P_1 = (1-\mu)(1-\lambda)$$;
- 第二种情况: $$h(x) \neq f(x), y = f(x)$$, 其概率: $$P_2 = \mu \lambda$$

所以  $$P(h(x) \neq y) = P_1 + P_2 = \mu(2\lambda -1) - \lambda + 1$$

> b) At what value of A will the perfrmance of h be independent of µ?

也就是h的性能与u无关, 那么就是$$P(h(x) \neq y)$$的值与u无关, 即u的系数为0, 则$$2\lambda -1 = 0 \rightarrow \lambda = 0.5$$.

## 
