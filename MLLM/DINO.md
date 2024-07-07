---
Date: 2024-06-16
Title: DINO
dg-publish: true
tags:
---
# DINO: self-distillnation with no label 

# 1 Introduction
本文提出问题方式是： 追踪现有的Transformer模型在指标上的进步的来源。 

## 1.1 Problem Statement
核心问题是： 自监督学习时候会给VIT新的特性。 

他们发现： 自监督的学习可以
1. 提供显式的语义级别的特征
2. 是一个非常好的KNN分类器

NLP社区里面的自监督训练从BERT开始到gpt系列的成功证明了自监督训练的强大潜力。 


## 1.2 Stated Contribution
自监督的VIT有监督的VIT和convnets都不具有特征：最后一层的attention map天然包含分割边界等信息。 如下图所示：
![[picture/Pasted image 20240626151208.png]]

自监督的VIT即使不做任何微调，也是一个非常好的最近邻居分类器(KNN).

# 2 Related Work

# 3 Method

# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

## 5.1 Relative Position
# 6 Comments

