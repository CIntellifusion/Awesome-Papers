---
Date: 2024-06-16
Title: Improved VQ-Diffusion and MIN-SNR
dg-publish: true
tags:
  - GenerativeModels
  - Diffusion
  - Efficiency
---

# 1 Introduction

VQ-Diffusion should be categorized into discrete diffusion. 用VQVAE把图片编码成离散的token，然后在离散的空间上进行扩散。 VQ-Diffusion要求相对少的推理时间步数。

## 1.1 Problem Statement

## 1.1.1 posterior issue

条件图片生成中，条件信息可以被设置成y,生成的图片设置为x，生成模型的目标是： 最大化先验概率p(x|y)。 同时假设生成的图片x满足后验概率分布p(y|x)。  作者发现这个假设在大多数情况下会失效，即生成的图片并不满足后验概率。 

为了解决这问题，作者提出同时考虑先验分布和后验分布，通过后验概率的限制，改进模型去预测概率而不是预测噪音。 然后改进classifier free guidance为一种更加精确而普遍的方式: 用一组可以学习的参数去作为条件来近似概率分布p(x)

### 1.1.2 joint distribution issue

联合概率分布的问题： 考虑一个简单的离散的数据集AA和BB，如果我们分别预测第一位和第二位，我们仍然会采样出AB和BA两个错误的结果。 这是独立预测不同位置的token导致的。 实际上他们应该服从一个联合概率分布。  

为了解决这个问题，作者提出了High quality inference strategy。  这个策略有两个关键组成部分，减少每一步采样的token数量，因为同时采样越多的token意味着这个联合概率分布会带来的问题越大。 第二是引入一种purity prior去采样高置信度的结果。 



## 1.2 Stated Contribution

- 用后验限制来提高了图片生成的质量
- 指出了vq-diffusion的联合概率分布的问题
- 在多个数据集上证明了方法的有效性。


# 2 bachground VQ-diffusion


# 3 Method

# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

## 5.1 Relative Position
# 6 Comments

