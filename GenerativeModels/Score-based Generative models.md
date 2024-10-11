---
Date: 2024-05-08
Title: Score-based generative models
dg-publish: true
tags:
  - GenerativeModels
---
[Generative Modeling by Estimating Gradients of the Data Distribution | Yang Song (yang-song.net)](https://yang-song.net/blog/2021/score/)
# 1 Introduction
Yang Song.

> 这篇文章最近读了很多遍，每一遍都能有一些新的想法，而且可以有一些迁移。 

目前的生成模型按照他们表示概率的方式可以被分成:
1. likelihood-based models: normalizing flows, EBMs, VAE
2. implicit generative models: GANs


> 对什么东西进行建模是至关重要的问题。 


# 2 Key Words

Score Function: gradients of log probaility density fucntions
Score Function可以翻译成得分函数，定义为对数概率密度函数的梯度。 

# 3 Method

给定一个数据集${x_{1},x_{2},\dots,x_{N}}$每个数据都独立同分布于$p(x)$。 我们目标是用一个模型去拟合这个分布，然后生成更多符合这个分布的样本。 

要实现这个目标，我们首先需要确定一种表示概率分布的方法，第一种方法是直接建模概率密度函数(pdf)或者概率质量函数(pmf). 考虑一个由一组可学习参数的$\theta$定义在实数域上的函数$f_{\theta}(x) \in \mathbb{R}$,那么概率密度函数可以通过
$$p_{\theta}(x) = \frac{e^{-f_{\theta}(x)}}{Z_{\theta}}$$

$Z_{\theta}$ 是一个大于0的常数使得 $\int p_{\theta}(x) \, dx=1$。 这里的$f_{\theta}(x)$ 被成为未归一化的概率模型，或者基于能量的模型(energy-based model)

定义这样一个函数有什么好处呢？ 对于$f(x) \in [-\infty , \infty]$ ,$e^{-f_{\theta}(x)}$永远为正，且小于1。 这满足概率的两条定义，再加上一个配分函数保证概率的积分为1。 

但是这个配分函数一般来说是很难求解的，而且在神经网络的优化过程中，由于$\theta$一直改变，也会要求佩芬函数$X_{\theta}$一直变化。

## 3.1 梯度函数+朗之万动力学

如果我们去建模$p_{\theta}(x)$的梯度，那么配分函数作为一个常数，倒数就会为0 。 从而绕开求解配分函数Z的过程。 但是在我们得到了梯度函数之后，怎么才能采样呢？那就需要用到狼只玩动力学的算法，同多迭代来达到积分的效果。 

明确了我们要学习一个神经网络$s_{\theta}(x)$来近似数据分布的得分函数score function。 怎么解决score function本身不可知的问题呢？ 换句话说，损失函数优化目标怎么解决。 已经有一些列score matching的方法能够在不知道score functionn的条件下完成这个工作。 

当我们有了一个近似的得分函数$s_{\theta}(x)$，也就是理解为一个梯度场，我们可以用一个迭代的方式将初始化分布的数据点推到目标分布: 
$$
x_{i+1} \leftarrow x_{i} + \epsilon s_{\theta}(x) + \sqrt{2 \epsilon} z_{i}, i = 0,1,...,K
$$ 

其中z_i服从标准正态分布。 这个x_i+1在K趋近无穷大的时候会收敛到p(x)

## 3.2 Multi-scale noise perturbations 

我们学习到的得分函数在数据集经常出现的区域会比其他区域准确。 而在数据集样本点稀疏的区域，梯度不准确，就会导致采样的过程难以收敛。 

这里给出的解决办法是对数据点加噪音，加噪过后的数据点就会填充低密度的区域，让这些区域的梯度更加准确。 而为了让更多的区域都能够在信息加噪的过程中获益，这里采用了同时进行多个独立高斯分布进行加噪音。 

加噪音之后原数据分布从$p(x)$变成了$p_{\sigma_i}(x)$ ，其中$\sigma_i$表示加噪音的方差。 这个过程可以记为
$$
p_{\theta_{i}}(x)= \sum\limits p(y)\mathcal{N}(x;y,\sigma_i^2I)
$$
然后我们拟合的过程也就变成了多个噪音分布下的概率拟合的加权平均。 


## 3.3 Perturbing data with SDE 
用随机微分方程对数据进行加噪音。 并且将离散的加噪转化为连续时间步的加噪。 

