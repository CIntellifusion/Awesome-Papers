#! https://zhuanlan.zhihu.com/p/704329914
<!-- ---
Date: 2024-05-17
Title: SDv3 MMDIT
dg-publish: true
tags:
  - Diffusion
  - DiT
  - GenerativeModels
--- -->

# SDv3 MMDIT 技术报告 
# 1 Introduction

原文链接： https://stability.ai/news/stable-diffusion-3-research-paper
这个博客的写作手法直抒胸臆，直击最关心的arch和expriment，看起来非常舒服。 
## 1.1 Problem Statement


## 1.2 Stated Contribution

# 2 Related Work

# 3 Method
## 3.1 MMDIT: multi-modality transformer

![Image](https://pic4.zhimg.com/80/v2-d513e0cb80e7e3eb192119c94e0f6eaf.png)

多模态的transformer:MMDIT
一个基本的transformer block包括两个tokenizer(大概可以这样理解)分别编码文本和图片信息，然后把特征连接起来做Joint Attention,然后再接入两个FFN模块。 

由于是denoising network,还需要有一个对timestep的特征编码，并且参与到特征融合中。 


## 3.2 Improving Rectified Flows by Reweightning
Rectified Flow (RF) formulation 有待深入了解 open-sora也用了这个方法进行训练

## 3.3 Flexible Text Encoders
他们把T5干掉了，这样可以减少很多推理时候的时间。 


# 4 Experiment
![Image](https://pic4.zhimg.com/80/v2-d672edacae96e7eabb485aa79fad4600.png)

一个简单但是最有力的比较：和更早的两个diffusion transformer架构相比，训练收敛速度更快，并且最终效果更好。 值得注意的是，在200k step以前，MMDIT的效果不明显，但是在之后MMDIT的优势就显示出来了。 


# 5 Summary

# 6 Comments

