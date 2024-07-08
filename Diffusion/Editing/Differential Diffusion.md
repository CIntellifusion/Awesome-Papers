---
Date: 2024-06-16
Title: Differential Diffusion
dg-publish: true
tags:
  - Diffusion
  - Editing
  - GenerativeModels
---

> 本文应该是基于diffusion的图片编辑模型的第一篇精读。 所以会对任务定义讲的更加详细一些。 
# 1 Introduction
Modern generative models can create photo-realistic images from random noise. 
这就是对图片生成模型做的事情的一个高度总结。 这些模型都在对数据分布进行建模，希望构造出从高斯分布到真实图片分布到变换。 

而图片的生成又可以被分为两个部分:unconditional generation和conditional generation. 无条件的生成就是对训练数据集的分布的建模。 而有条件的生成则包含了condtion和x分布的条件概率分布的研究。 

> 生成模型的最终目标是满足用户需求

用户有一个图片需求（正如检索用户有信息需求一样） ，然后可能用文本，点击等等方式作为输入，希望得到想要的满足需求的图片。 

假设我们有一个足够好的生成模型，即他可以很好的建模真实图片的潜在分布。 另外我们可以假设condtion记为c也服从一个潜在分布。 接下来我们的问题就变成了研究c和x分布之间的关系。 一个符合条件c的x的分布可以记为p(x|c,noise)。

在本文之前条件生成模型大多有两种思路： 第一种是conditional GAN， 直接学习mapping f: x_orig -> x_edited.  这种方法不能处理新的条件，需要反复重新训练，非常消耗时间。 第二类是用 GAN inversions。 一个训练好的GAN模型被用来编码图片到隐空间（latent representation space)。 然后在隐空间上修改这个向量，最后重建到图片空间。  latent code的编辑本身存在不忠实于原图的问题。  一个相关的topic是： 这些生成模型的隐空间是不是足够好，是不是一样好。 此处的好指隐空间具有一些良好的性质，线性组合等等。 


## 1.1 Problem Statement
之前的工作不能在faith和condition之间很好的平衡，难以复用比较消耗资源。 在这个工作里面，作者提出了SDEdit， 一个利用生成随机方程的编辑框架。 


## 1.2 Stated Contribution



# 2 Related Work

## 2.1 Text-based image synthesis
现在主流的文生图的方法还是基于Dif fusion的。 这篇文章的作者提了几个高度相关的文章：
1. promptpaint
2. multidiffusion
3. spatext
## 2.2 Text-based Editing
- diffusionCLIP
- more control for free
- pix2pix
- prompt-to-prompt
- DiffEdit
作者认为虽然文生图的方法有了非常大的进步，但是mask在做引导方面具有无可替代的重要地位。 
## 2.3 Mask-based Editing 

Stable Diffusion是天然支持i2i的 补全任务的。 其他的方法
- DeepFloyd 
- Stable Diffusion XL 

另一条线的编辑方法： 
- blended diffusion - blended latent diffusion
- SDEdit - stroke based picture editing 

# 3 Method

看不太懂
等看完socre-based models和SDE之后回来


# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

## 5.1 Relative Position
# 6 Comments

