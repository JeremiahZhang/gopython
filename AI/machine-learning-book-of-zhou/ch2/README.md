# 模型评估与选择

- 经验误差与过拟合
- 评估方法
    - 留出法 hold-out
    - 交叉验证法 cross validation
    - 自助法 bootstrapping
    - 调参与最终模型
- 性能度量
- 比较检验
- 偏差与方差

---

## 概念

`accuracy`:

正确率： 正确分类的样本数目 a 与总样本数 m 之比， 即$$\frac{a}{m}$$

`error rate`:

错误率： 未正确分类的样本数目 e 与总样本数 m 之比， 即$$\frac{e}{m}=1-\frac{a}{m}$$

`error`:

误差： 机器学习算法训练得到模型在输入样本上的实际预测输出与该输入样本的真实输出之间的误差。

`training dataset`

训练集： 机器学习算法需要在一些样本上进行训练学习得到预测模型，这些样本组成“训练集”。 一般在已知的样本上进行随机选择，当然也是有选择方法。

`testing dataset`

测试集：机器学习算法经过训练后得到的预测模型需要在另一些样本上进行预测，进而得到该预测模型的误差（测试误差`testing error`）。这一些样本组成“测试集”(testing dataset).

`training error or empirical error`:

训练误差 or 经验误差: 算法通过训练样本进行训练（从经验中学习）得到预测模型，该模型不一定是百分百正确，可能存在误差，那么这个误差就称为“训练误差”或“经验误差”，也就是训练后，在训练集上的误差。

`generalization error`:

泛化误差: 在训练样本上进行学习，我们可以看作为在“特殊”（经验）样本上进行学习，这样得到的预测模型，在新样本（general，更一般的新样本）上进行预测，该预测会产生误差，该误差称为“泛化误差”。

`overfitting`:

> Overfitting is the problem of creating a model that classifies our training dataset very well, but performs poorly on new samples.

过拟合：简而言之，算法在训练集上得到的预测模型在训练集上表现非常好，但是在新样本上的表现却不尽如人意（泛化能力差），该问题就是“过拟合”问题。

`underfitting`:

欠拟合：相反，算法在训练训练集上得到的预测模型在训练集上表现就不怎么好。

## 评估方法

算法训练得到的预测模型该如何评估？ 评估“泛化误差”。 然书中讲到用“测试误差”作为“泛化误差”的近似，进而评估“测试误差”来判断算法效果如何。

那么就涉及如何将一个样本数据集划分为：“训练集”（training dataset）和“测试集”（testing dataset）。书中提到三种方法：

- [`hold-out method`][1] 留出法
  - 将数据集划分为两组：
    - Training dataset：used to train the classifer
    - Testing dataset：used to estimate the error rate of the trained classifer
  - 缺点：
    - 对于 dataset 稀少的情况，就存在困难咯
    - 恰巧划分地不好，那么错误率会明显增加
  - So: hold out method 的限制，可以用下面的 resampling methods（重采样方法）解决（不过有更多的计算成本）
- [Resampling methods][1]：
  - `cross validation` 交叉验证法
    - `random subsampling`
      - 从dataset中k次随机不重复采样。
    - `K-Fold cross validation`
      - 将dataset划分为k个大小相似的互斥子集，每次k-1个子集的并集作为训练集，余下的1个作为测试集，总k次。
      - K 如何选取？ 一般取 k=10. 还是与具体情况而论.
    - `Leave-one-out cross validation`
      - 对于稀疏样本dataset比较好，m个样本划分了m个子集，训练集选用m-1个子集的并集。总m次。
  - `bootstrapping` 自助法
    - 在所有 dataset（D） 中有放回的取去样本作为训练集(X)，那么测试集就是：T=D-X（-表示差集）

> Validation techniques are motivated by two fundamental problems in pattern recognition: **model selection** and **performance estimation**.

## [调参与最终模型][1]

> If model selection and true error estimates are to be computed simultaneously, the data needs to be divided into three disjoint sets.

- 训练集 Training dataset: a dataset of examples used for learning: to fit the parameters of the classifer
- 验证集 Validation dataset: a dataset of examples used to **tune the parameters of a classifer**（运用于调参）
- 测试集 Testing dataset： a dataset of examples used only to assess the performance of a fully-trained classifer

流程：

1. 划分样本数据集为：训练集、验证集、测试集
2. 选择算法结构和参数（对于同一算法）
3. 使用训练集训练模型
4. 使用验证集评估模型
5. 使用不同的算法结构和参数，重复2-4步
6. 选择最好的模型
7. 使用测试集评估最后的模型

![three-way-split](https://dn-learnml.qbox.me/image/ai/three-way-split.JPG)

注：2wd1阅读，2wd2笔记。

## 性能度量

### Precise and Recall

- `Precise` 查准率
- `Recall` 查全率

这两个概念以及 `confusion matrix` make me confused. 还是看一下[Precision and recall - Wikipedia](https://en.wikipedia.org/wiki/Precision_and_recall)的图片吧。

![Precisionrecall](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Precisionrecall.svg/440px-Precisionrecall.svg.png)

再结合 confusion matrix 在二分类问题中理解这些概念。

| 总样本  | 预测：+     | 预测：-|
| :------   | :-----     | :----|
| +         | ++ True Positive(TP) | +- False Negative(FN) Type II error|
| -         | -+ False Positive(FP) Type I error | -- True Negative(TN) |

总样本数就那么多，只有两类+or-，实际预测中结果就有四类，2*2=4.

- 一个样本实际的类标签为 +，预测结果为 +，就表示为 ++（实际为+预测为+），True Positive(TP)；（正确预测）
- 一个样本实际的类标签为 -，预测结果为 +，就表示为 -+（实际为-预测为+），False Positive(FP)；（错误预测）
- 一个样本实际的类标签为 +，预测结果为 -，就表示为 +-（实际为+预测为-），False Negitive(FN)；（错误预测）
- 一个样本实际的类标签为 -，预测结果为 -，就表示为 --（实际为-预测为-），True Negative(TN)；（正确预测）

那么：

$$ P = Precision = \frac{正确预测为+的数目}{预测为+的数目} = \frac{TP}{TP+FP} $$  
$$ R = Recall = \frac{对于+类，正确预测（预测为+）的数目}{+类样本总数} = \frac{TP}{TP+FN}$$  

注：2wd2 笔记

> 查准率和查全率是一对矛盾的度量。

如何使用 P-R 评价性能。

1. P-R 曲线图看包围
2. P-R 曲线图 看“平衡点” Break Event Point
3. $$F_1$$ 度量
  - $$\frac{1}{F_1} = \frac{1}{2}(\frac{1}{P} + \frac{1}{R})$$
  - $$F_1 = \frac{2*P*R}{P+R}$$
4. $$ F_\beta = \frac{(1+\beta^{2})·P·R}{(\beta^{2}·P)+R} $$: 依照对查准率和查全率的重视程度不同而定。
  - $$\beta > 0$$ 度量查全率对查准率的相对重要性
  - $$\beta = 1$$ 退化为 标准的 $$F_1$$度量
  - $$\beta > 1$$ 查全率影响更大
  - $$\beta < 1$$ 查准率影响更大

对于一个二分类问题对应一个混淆矩阵，那么多分类问题呢，可以转化为多个(n)二分类问题，对应n个 confusion matrix，在此基础上综合考察查准率和查全率。($$(P_1, R_1), (P_2, R_2), \cdots, (P_n, R_n)$$).

直接平均法：

- macro-P: $$P_{macro} = \frac{1}{n} \sum_{i=1}^{n}P_i $$
- macro-R: $$R_{macro} = \frac{1}{n} \sum_{i=1}^{n}R_i $$
- macro-$$F_1：\frac{2·P_{macro}·R_{macro}}{P_{macro} + R_{macro}}$$

还有就是预先平均法：得到 $$\bar{TP}, \bar{FP}, \bar{FN}, \bar{TN}$$, 再计算：

- micro-P: $$P_{micro} = \frac{\bar{TP}}{\bar{TP}+\bar{FP}} $$
- micro-R: $$P_{micro} = \frac{\bar{TP}}{\bar{TP}+\bar{FN}} $$
- micro-$$F_1$$: $$F1_{micro} = \frac{2·P_{micro}·R_{micro}}{P_{micro} + R_{micro}} $$.

### ROC and AUC

> ROC: Receiver Operating Characteristic
> AUC: Area under the curve

Roc 曲线：

- 纵坐标：True Positive Rate(TPR)
- 横坐标：False Positive Rate(FPR)

[ROC curves and Area Under the Curve explained (video)](http://www.dataschool.io/roc-curves-and-auc-explained/) 解释挺不错的。 暂时学会如何去让。

---

## 习题

> 2.1

1. 分层采样:
  - 训练集: 350个正例(正例如何取的?500个正例中前350个,第二个开始的350个,第三个开始的350个,好多好多啊),350个反例(类似).
  - 测试集: 150个正例,150个反例.

> 2.2

- K-Fold:
  - 尽可能保持数据分布一致性,从样本集100个中分层采样.
  - 每次: 训练集90个(45+,45-),测试集10个(5+,5-)
  - 2个类别的训练样本数相同,随机猜测
  - 1次10-fold:错误率 50%
- Leave one out
  - 情况 1:
    - 训练集(99个): 50 +,49 -
    - 测试集(1个): 1 -
    - 错误率 100%
  - 情况 2:
    - 训练集(99个): 50 -,49 +
    - 测试集(1个): 1 +
    - 错误率 100%

> 2.3

假设学习器A的F1值比学习器B的高, 即: $$ F1^{A} > F1^{B}$$, 而 $$\frac{1}{F1} = 0.5(\frac{1}{P} + \frac{1}{R})$$, 代入之前的不等式中可得到:

- $$\frac{1}{P_A} + \frac{1}{R_A} < \frac{1}{P_B} + \frac{1}{R_B}$$,
- 对于BEP值, P=R, 所以 $$P_A = R_A, P_B = R_B$$,
- $$\frac{1}{P_A} + \frac{1}{R_A} < \frac{1}{P_B} + \frac{1}{R_B} \rightarrow \frac{1}{P_A} < \frac{P_B}$$
- $$ \rightarrow P_A > P_B \rightarrow BEP_A > BEP_B$$

即 A 的BEP值比 B 的高.

> 2.4

TPR(True Positive Rate 真正例率) = Recall(查全率), 查全率 Recall 和 查准率Precision 是一对矛盾的度量.

FPR(False Positive Rate 假正例率),  FPR大了, P就小了.


---

[1]:  http://research.cs.tamu.edu/prism/lectures/iss/iss_l13.pdf
