# Error and Noise

误差和噪声.

回顾两点学习问题的观点:

1. What approximation means when we say that out hypothesis approximates the target function well?(h->f 好到底是如何好?)
2. The nature of the target function.(目标函数的本质)

`输入-系统-输出`, 系统输入中往往存在噪声, 噪声和输入一起经过系统后, 输出就不完全由输入决定. 比如振动信号采集过程中, 往往外界存在噪声.

在机器学习问题中, 也涉及到了噪声这个问题. 看系统相通.

那么在学习问题中, 引入噪声, 会得到怎样的结果呢?

等等, 在学习问题中, 这个噪声源在哪里呢? 或者说哪里会存在噪声? 在系统中, 输入存在噪声. 那么我们推想下, 在学习问题中, 我们的输入是数据(sample), 这个数据或多或少存在噪声. Sample 又取自于数据样本空间 X, 而样本空间 X(out of sample) 的数据又是由 target function f(假想, 未知, 一种模式) "确定". 因此, 我们的噪声从根本上存在这个target function f中, 如果 f 有噪声影响, 那么其"由来"的数据, 就不一定准确.

---  

## 1.Error Measure

误差度量.

学习的目标: $$g \rightarrow f$$. 那么问题是: 如何确定 g 接近 f 的程度? 我们就需要使用 error measure(误差度量, 又名: error function, cost, objective, risk) 来量化这个接近程度.

不同的误差度量影响学习的结果(final hypothesis). 即使 target f 和数据一样, 这个问题同样存在. 因此, 误差度量的选择影响学习的最终结果. 那么误差度量的选择准则是什么呢?

误差度量就是量化 每个 hypothesis h 和 target function f 的差异程度, 形式化表示:

$$Error = E(h, f)$$

其中, $$E(h, f)$$ 只是形式化表示每个h与f之间的差距, 真正还是要建立在每个输入数据点(训练样本)之上. 对于单个训练样本x, 则单个误差表示为 $$e(h(x), f(x))$$, 整体的h与f的误差为所有数据误差的平均值, 即:$$E_{in}(h) = \frac{1}{n} \sum_{i=1}^{n} e(h(x_i), f(x_i))$$.

而 out-of-sample error:

$$E_out(h) = \Bbb E_X [e(h(X), f(X))]$$

其中, $$X$$ is from the input space(来自整个输入空间) $$\cal X$$

简单的误差实例:

- Squared error: $$e(h(x), f(x)) = (h(x) - f(x))^2$$
- Binary error: $$e(h(x), f(x)) = [[h(x) \neq f(x)]]$$

理想情况, $$E(h,f)$$应由用户定义. 相同的学习目标在不同的情景中需要使用不同的误差度量. 比如**超市的指纹识别**和**CIA中情局的指纹识别**. 因为有时候$$E(h,f)$$作为原本使用$$f$$最终却使用$$h$$后的代价(cost), 两者情景不同, 错误($$h(x) \neq f(x)$$)的代价也不同.

### 指纹识别案例

![lfd_finger_print](https://dn-learnml.qbox.me/image/ai/lfd_finger_print.JPG)

目标函数 target f的输入为指纹, 输出为 +1 表示指纹正确, 输出为 -1 表示指纹错误.

现在我们有一个假设 h, 那么 h 的输出与 f 的输出存在四种不同情况. 如下所示:

| |  | f     | f |
|:---| :------------- | :------------- | :---|
|   |  | + 1 | -1 |
| h | +1 | no error | false accept |
| h | -1 | false reject | no error |

其中只存在两种错误情况. 那么在不同的情景中, 这两者错误情况所带来的后果存在差异.

比如, 如果该指纹识别系统要用于**超市中**, 那么 false accept 错误接受所带来的后果(即顾客不是该超市会员, 却被当作超市会员享受会员价)或损失并不大, 而 false reject 错误拒绝(顾客是会员, 却错误地拒绝他, 让他享受不了会员价, 该会员顾客或多或少会不开心, 说不定以后不来该超市也是有可能的)所带来的损失更大. 前者可能还不一定带来损失, 有可能为未来带来盈利, 但是后者的损失就比前者大, 会员顾客流失. 因此这两个错误的代价是不一样的. 前者小, 后者大.

- false accept **代价小**
- false reject **代价大**

如果指纹识别系统要用于**CIA中情局**, 那么情况就截然不同.

- false accept 带来的后果巨大(被外人意闯入成功, 窃取机密, 后果不堪设想🙈) **代价大**
- false reject 带来的后果可能比 false accept 小太多. **代价小**

两者不同的代价权重, 可以用下表表示:

![cia-market](https://dn-learnml.qbox.me/image/ai/fld_cia_market.JPG)

在这两种情景中, 最后得到的 final hypothesis g 会完全不同.(还是这样看容易理解, 如果引入 TF, FP 这种定义, 离实际好远)

所以, 误差度量依赖于系统在怎样的情景中使用, 我们不能思维定势, 以为有一个特定的误差度量选择标准来套用, 要会灵活变通, 举一反三.

上例只是理想情况, 实际中较难应用, 原因:

> 1. the user may not provide an error specification, which is common.
> 2. the weight cost may be a difficult objective function for optimizers to work with.

因此, 我们需要寻找其他方式(实际经验或分析等)来定义 error measure(误差度量).

- with purely practical considerations or
- analytic considerations.

---

## 2.Noisy Target

实际应用中, 目标函数 target function f 存在噪声, 训练样本并不处于确定性的目标函数, 而是处于带噪声的目标函数中. **Such that the output is not uniquely determined by the input**. 比如在之前的信用卡评估案例中, 两人相同的情况, 最终评定是否发放信用卡却不同(一个接受, 一个不接受). 因此, **the credit 'function' is not really a deterministic function, but a noisy one.**

我们还是得引入概率来建模.

将 output y 看作受 input x 影响的随机变量, 而不是由 input x确定的量(y = f(x)). 怎么表示呢? 以一个 target distribution $$P(y|x)$$ 替代确定性目标函数 $$y = f(x)$$. 因此一个数据样本$$(x, y)$$产生于联合分布: $$P(x, y) = P(x)P(y|x)$$.

> Noisy target = determined targe + added noise.

如果y是实数, 则:

- deterministic $$f(x) = \Bbb E(y|x)$$
- noise: $$y - f(x)$$.

Noisy target = deterministic f + noise

如果噪声为0, 那么这个target就是确定性的target function. (特例)

deterministic target is a special case of noisy target:

$$P(y|x) = 0 $$ expect for y = f(x).

也就是, 不确定性(P(y|x))不存在嘛.

练习 1.13 可帮助理解.  

 $$P(y|x), P(x)$$的在学习中的不同之处.

 - target distribution $$P(y|x)$$: what we are trying to learn
 - input distribution $$P(x)$$: only quantifies the relative importance of the point x in gauging how well we have learned.
 - Merging $$P(x)P(y|x) = P(x, y)$$: mixes two concepts.

学习可行性的分析同样适用 noisy target function. 因为霍夫丁不等式看用于随机未知的目标函数, 我们不用知道$$E_{out}$$, 我们只需要用$$E_{in}$$来近似.

![joint_dis](https://dn-learnml.qbox.me/image/ai/ldf_joint_distribution.JPG)

训练样本来自于独立联合分布. y 取自整个输入空间$$\cal X$$, 其概率分布为$$P(y|\cal X)$$; 而 x 取自概率分布$$P(\mathcal{X})$$.

Target function 中引入噪声后, $$E_{in}$$的情况变得糟糕, 因为噪声进入训练样本, 样本拟合学习难度增加.

在书籍第二章中, 在引入目标函数概率分布$$P(y|x)$$后, 会证明霍夫丁不等式的高阶版本. 敬请期待.

---

## 3.Sum

这节下来, 考虑误差和噪声引入目标函数后, 学习的过程就如下图所示:

![learing-diag](https://dn-learnml.qbox.me/image/ai/lfd_learning_diag.JPG)

---

## ChangeLog

```
@anifacc
2017-08-22
```
