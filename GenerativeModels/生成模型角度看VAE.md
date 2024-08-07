---
Date: 2024-06-30
Title: VAE
dg-publish: true
tags:
---

# 引入

大部分讲VAE的博客一般会从AE开始讲起。 但是在我推了很多遍公式并且自己从头训练一个VAE然后**遇到很多问题**之后，我意识到VAE的公式是优雅的，但是实践上还需要从生成模型的角度来理解VAE，告诉我们什么样的情况会训练出问题。 因为现实并不是美好的，不是我们随便弄一个VAE+一个数据集他就能work。 

# 生成模型

个人浅见，所有的生成模型VAE，GAN， Diffusion, Flow-based models都在追求一个事情： 用高斯分布（足够简单的分布）建模复杂的潜在分布。 
从代码的角度来说，随机采样一个服从高斯分布的随机向量，输入一个生成模型，得到一个符合用户期望的东西。(图片，视频等等)

我们之所以不从AE谈起，因为AE不是生成模型。 

将一个512维度服从高斯分布向量输入styleganv2，可以得到一张人脸图片。  

## VAE
定义数据集$D=\{X_{1},X_{2},...,X_{N}\}$，数据集D服从一个分布$P(X)$。 但是我们通常不能得到这个分布。 我们可以通过一个隐向量来建模这个分布。 通过全概公式有：
$$
p(X)=\sum\limits_Zp(X|Z)p(Z)
$$

这个隐向量Z是不可观测的，所以叫做隐。 Z在这里的作用是作为建模X的一个工具。 而$P(Z)$作为一个工具，自然是一个我们已经掌握的分布。 所以称谓先验分布。 


## VAE退化成AE
- 这一点非常重要，因为我们在训练的时候真的遇到这个问题了。 







# 参考
[变分自编码器VAE：原来是这么一回事 | 附开源代码 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/34998569)