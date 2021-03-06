# 基础技巧
## 数据集
+ 训练集
+ 验证集
+ 测试集

    训练集用于训练参数W、b, 验证集评价参数表现后调整超参数后继续训练，如此反复最后基于测试集测试
    
    验证集与测试集数据来源需要一致，否则超参数不一定适用。

    训练集与验证集可能出现数据来源不一致的情况，需要引入训练验证集判断这类情况，做法：从训练集中取部分数据作为训练验证集，比较模型在验证集及训练验证集上的表现，如果相差较大，表示可能存在数据异源问题。

## 欠拟合和过拟合
### 欠拟合
一般表现：模型对训练数据预测不准确

解决：
+ 尝试更大的神经网络、增加神经网络层数、增加神经元个数
+ 增加训练次数
+ 尝试其他优化算法
+ 尝试不同的神经网络架构

### 过拟合
一般表现：模型在训练数据集上预测准确但在测试数据集上预测误差较大

解决：
+ 获取更多训练数据，或通过数据增强手段丰富数据集。
+ 正则化，常用L2正则，即对损失函数增加一个L2正则项约束，避免权重过大。
+ 尝试不同的神经网络架构
+ dropout，在训练时随机删除神经元，dropout导致神经网络结构发生变化，所以损失函数不一定随着训练次数递减，所以不便监视训练过程，一般开始将dropout关掉，观察成本随着训练次数递减后再开启dropout。

## 输入特征归一化
    均值0，方差1

## 梯度消失和梯度爆炸
+ L2正则
+ relu激活函数
+ batchnorm
+ 残差结构
+ LSTM
+ 合理初始化神经网络权重，尽量接近0

## 梯度检验
    检验神经网络是否存在bug，利用数值逼近求得的偏导数与反向传播求得的偏导数做比较检验

# 优化算法
## Mini-Batch
+ 将大训练集拆分为小训练集进行神经网络的训练，如果使用整个训练集就是batch梯度下降，如果子训练集只有一个样本即随机梯度下降。
+ batch梯度下降的方向是所有样本学习后的优化方向，但受限于样本量、硬件瓶颈及模型学习周期过长，经常需要将训练集拆分成小数据集。
+ 子训练集的大小是一个超参数，需要不停的尝试，一般选择2的次方个样本组成小训练集。
+ Mini-batch梯度下降时，成本是波荡起伏的，一般使用iteration表示一次梯度下降，epoch表示整个训练集进行了一次梯度下降，Mini-batch 梯度下降有可能最终一直在最小值附近徘徊，可以通过降低学习率解决。

## 梯度下降
### 指数加权平均
超参数k表示趋势值v受前
${1 \over 1-k}$
个数值影响
$$
v_t = {k·v_{t-1} + (1-k)·w_t \over 1-k^t}
$$
### 动量梯度下降
动量梯度下降即引入一个超参数k，对$dw$和$db$做指数加权平均
### RMSprop
1. 计算 $dw$ $db$
2. 计算指数平均值$S_{dw}$
$$
S_{dw} = kS_{dw} + (1-k)dw^2
$$
其中 $dw^2$ 是元素的平方
3. 同理计算 $S_{db}$
4. 更新 $w\ b$
$$
w = w - \alpha({dw \over \sqrt{S_{dw} + u}})
\\
b = b - \alpha({db \over \sqrt{S_{db} + u}})
$$
### ADAM

# 调试神经网络