---
Date: 2024-06-03
Title: Normalization
dg-publish: true
---
# Normalization

## 1 Introduction

一个困扰了我很久的问题: 为什么在训练的时候加normalization(一般)效果会更好，但是在测试的时候不用加？

于是我决定在最近把我之前没有搞清楚的问题都整理成一篇文章，再加上必要的实验。 

为了使得问题更加具体，我们可以考虑手写数字识别任务，利用卷积或者多层感知机作为backbone. 

## 2 Batch Normalization

要对这个问题进行分析，我们首先需要简化问题，我们只用考虑到多层感知机和多层卷积构成的模型即可。 (在实现上，多层感知机是卷积的一种情况)

除此之外，我们可以转化问题:
1. 为什么在图片识别的时候，我们对像素值进行归一化
2. 像素值的归一化和中间隐藏特征的归一化有没有一致性



## 2.1 没有Normalization的情况

考虑一个线性层，权重为$W$,偏置为$b$。 输入为$x$,输出为$\hat y$,标签为$y$。 
因此有前向过程:
$$
\hat{y} = Wx+b
$$
损失函数:
$$
L=\| \hat{y}-y||^2_{2}
$$

在这种情况下，$W,b$的取值范围理论上都是全体实数。

## 2.1.1 输入的归一化是否有收敛上的好处

为此我们可以构造一个数据集$D=\{p|(x^n,y)\}$

分别取$x^n$服从$N(0,1)$和$N(a,b)$观察训练过程中损失函数和模型权重的均值方差的变化


## 3 Layer Normalization


## 4 Group Normalization

## 5 Adaptive Normalization


## 6 Summary 

- 什么时候应该用什么样的normalization
- 

