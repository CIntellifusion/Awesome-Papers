前段时间写代码效率比较低，现在感觉纠正一下写代码的习惯之后来总结一下研究代码的一些心得。 我们主要关注在如何从始到终完成一个新的工作。 

## Debug 

> 此处必须检讨之前写代码的几个坏习惯： 1. 只要代码不报错就不去看细节。 2. 从结果倒推代码正确性，然后返回去找bug。 3. 实验记录不完整不详细 不可追溯不可复现。 

Debug不仅需要解决报错，更需要解决代码里面的逻辑错误。 

所以实现一个算法的时候要把整个流程全部都搞清楚。 data-model-training-validation-logging几个部分。 

目前我们训练框架都是基于pytorch lightning的

## 任务： 把一个非lightning的训练代码改写到lightning下面

1. 把training和generation函数实现了
2. 在单个数据上overfit
3. 实现validation / logging 到wandb
4. 在小规模数据上验证数据正确性
5. 调训练参数

