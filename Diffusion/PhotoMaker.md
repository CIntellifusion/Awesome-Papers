#! https://zhuanlan.zhihu.com/p/704330349
---
Date: 2024-04-02
Title: PhotoMaker
dg-publish: true
tags:
  - Diffusion
  - TrainingFree
  - GenerativeModels 
---
# Customizing Realistic Human Photos via Stacked ID Embedding
# 1 Introduction

## 1.1 Problem Statement
![Image](https://pic4.zhimg.com/80/v2-5455184f95c44e141ee83b1af5b2ed90.png)


个性化的图片生成任务收到了广泛的关注，从CVPR23Best student paper DreamBooth以来，有了非常多的尝试。 下游任务包括个性化肖像生成，图片驱动，虚拟试衣等等。 


## 1.2 Stated Contribution
- unified ID embedding: 聚合多个输入图片的identity
- ID-oritented Data pipeline: 自动化的数据集构造方法
- 不需要测试的时候进行微调。

相比于DreamBooth的两个改进：
- 更好的variation，在生成的时候有更好的多样性，并且还要保证identity
- 训练的时候有更多更准确的表示ID的数据

值得注意的是：虽然在训练阶段输入的ID特征都来自同一个人，但是photomaker也支持对多人的identity进行混合。 


# 2 Related Work

## 2.1 t2i diffusion models
截止文章写作的时候SD XL是最有效的开源模型。 但是截止本博客写作的时候，SD3已经发布。 

## 2.2 Personalization in Diffusion Models

Diffusion训练的模型是通用的生成模型，越来越多的工作开始关注个性化定制和生成模型，去对某个ID进行生成。 DreamBooth和Textual Inversion是两个相对最早的工作。 这些工作有的关注于PEFT方法进行小成本的微调，有的尝试用个性化数据集进行训练。 

# 3 Method

## 3.1 ID特征融合
用CLIP做图片编码器取得图片的特征。 
在输入之前会去掉图片中的背景噪音。 
然后用一个MLP微调一下这个特征。 

堆叠过程。 之前的工作已经证明独特的token可以用来作为个性化的特征。 man，woman作为默认的class condition token组成embedding，也可以通过年龄等条件替换性别。 
这个工作相比于dreambooth最大的好处是同时输入了所有的identity. 

特征融合。继承了CrossAttention机制做ID特征的融合，然后替换掉原始embedding的内容。 
![Image](https://pic4.zhimg.com/80/v2-b07220d7a7249e5395d4d593deaa95f6.png)

## 3.2 数据构造流程
从VoxCeleb1和VGGface2里面抓去了名人的名字，然后下载高质量图片。 然后做人脸检测过滤。 接下来用arcface做identity check，过滤特征相似度更低的模型。 然后做裁剪分割。 最后用BLIP2生成一些描述。 

# 4 Experiment
![Image](https://pic4.zhimg.com/80/v2-ce0d3685c331013b6a9d6e2e22774bd8.png)
![Image](https://pic4.zhimg.com/80/v2-f85cf60b50f6c54a5dc44623a16ad15c.png)
# 5 Summary

把多于一张图片的identity embedding堆叠起来，然后做一个特征融合，希望他能学到这个这个人的最本质的特征。 
# 6 Comments

