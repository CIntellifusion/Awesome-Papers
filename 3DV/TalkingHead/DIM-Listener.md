---
Date: 2024-10-13
Title: Dyadic-Interaction-Modeling
dg-publish: true
tags:
  - ECCV24
---
# 1 Introduction

## 1.1 Problem Statement


## 1.2 Stated Contribution



# 2 Related Work

# 3 Method

## 3.1 Facial Motion Representation
用EMOCA做动作捕捉
## 3.2 Learning Discrete Speaker-Listener  
VQVAE学一个表征。 这个东西和L2L和LM-Listener是一样的配置。 但是这里的motion codebook对speaker和listener是分开的。 分别是:
listener encoder: $Enc^{(l)}_{VQ}$
listener decoder: $Dec^{(l)}_{VQ}$
speaker encoder: $Enc^{(s)}_{VQ}$
speaker decoder: $Dec^{(s)}_{VQ}$

## 3.3 Dyadic Interaction Modeling
哥们，你这个小标题没有什么意义啊，这一节怎么全是炫技。 
speaker motions: $s_{1:T}$
audio features: $a_{1:T}$
listener motion: $l_{1:T}$
用contrastive learning的方式来匹配speaker-listener pairs. 这里把speaker和listerner的特征堪称两个不同的但是可以对齐的特征空间。 然后用mask的方式做数据增强，用CE loss训练



# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

# 6 Comments
这个文章感觉技术上也没有什么创新，但是跟之前的工作还是挺不一样的。 但是论文的记号确实不太清楚，尤其是3.3节，除此之外，visually我感觉结果也没有特别好。 
[[LM-listener]]
[[learn2listen]]

所以我应该先看learn2listen和lm-listener的结果，这样可以快速搞出来两个论文。然后再看DI吗这个工作。 
