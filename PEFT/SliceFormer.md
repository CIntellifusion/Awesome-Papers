
# Motivation
对transformer的改进，意在解决MHA的缺点，设计出理想的attention map. 

> 这个工作很不错的地方在于他是analysis-orientated. 从分析到方法的过程是非常清晰的。 

transformer能够成功的原因在于加了softmax和norm正则化，否则它一定是会坍缩的。 

这里针对作为encoder的transformer，也就是判别任务上的transformer。

transfomer和它的一些变体有一些共同的特征，attention的平方复杂度要求我们追求一个 稀疏的，满秩并且双随机的attention map.  （但是这是为什么呢） 


传统的MHA机制在长序列问题上的问题有： 计算复杂度高，可扩展性差，数值稳定性差。 

SparseTrans和LongFormer利用滑动窗口机制计算出一个稀疏的全局attention map来改进这些工作。  Performer这些工作通过降低列数量来压缩矩阵的秩，Linformer降低矩阵的行秩。 

> 我们有没有一个统一的架构来解释这个工作。 这个事情可能是非常有价值的。 



# Method

$$
Att(V;Q,K):=P(Q,K)V
$$

$$
P(Q,K)=Softmax(\frac{QK^T}{\sqrt(D)})
$$



