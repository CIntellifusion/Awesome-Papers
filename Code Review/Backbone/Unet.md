> 参考lvdm里面的openaimodel3d.py的实现


# Transformer

## Relative Position 

$$ X \sim \text{Xavier}(μ, σ) \Leftrightarrow X_{i, j} \sim \sqrt{\frac{6}{μ + j + 1}} $$

## CrossAttention
交叉注意力机制
接受一个x作为隐藏状态，接受一个context作为条件，接受一个mask

- x乘上一个矩阵得到query 
- context 乘上一个矩阵得到key 和 value 

如果只有text作为条件:
那么 x和text进行注意力计算

如果有image作为条件:
那么x和text注意力计算的结果需要和x和image的结果加权求和。 

## Basic Transformer
默认的注意力机制是CrossAttention
默认的Transformer是
进行两次norm-attention和一次前向传播

## Spatial Transformer

用于处理图片数据的空间维度
- 先用linear或者conv获得token
- 再经过d个basic transformer
- 最后一个零初始化的out layer 
- 无relative position

## Temporal Transformer

用于处理图片数据的时间维度
- 先用linear或者conv获得token
- 再经过d个basic transformer，包含self attention或者causal attention，有relative position
- 最后一个零初始化的out layer 


# Upsample and Downsample 

上采样和下采样层分别有插值和卷积的实现
之后加上一个池化层
