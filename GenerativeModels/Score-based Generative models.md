---
Date: 2024-05-08
Title: Score-based generative models
dg-publish: true
tags:
  - GenerativeModels
---
[Generative Modeling by Estimating Gradients of the Data Distribution | Yang Song (yang-song.net)](https://yang-song.net/blog/2021/score/)
# 1 Introduction
本文的作者Song Yang 

目前的生成模型按照他们表示概率的方式可以被分成:
1. likelihood-based models: normalizing flows, EBMs, VAE
2. implicit generative models: GANs



# 3 Method

给定一个数据集${x_{1},x_{2},\dots,x_{N}}$每个数据都独立同分布于$p(x)$。 我们目标是用一个模型去拟合这个分布，然后生成更多符合这个分布的样本。 

要实现这个目标，我们首先需要确定一种表示概率分布的方法，第一种方法是直接建模概率密度函数(pdf)或者概率质量函数(pmf). 考虑一个由一组可学习参数的$\theta$定义在实数域上的函数$f_{\theta}(x) \in \mathbb{R}$,那么概率密度函数可以通过
$$p_{\theta}(x) = \frac{e^{-f_{\theta}(x)}}{Z_{\theta}}$$

$Z_{\theta}$ 是一个大于0的常数使得 $\int p_{\theta}(x) \, dx=1$。 这里的$f_{\theta}(x)$ 被成为未归一化的概率模型，或者基于能量的模型(energy-based model)


# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

# 6 Comments

