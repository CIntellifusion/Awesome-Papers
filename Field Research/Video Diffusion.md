---
Date: 2024-04-21
Title: Video Diffusion
dg-publish: false
---
The inherence of this template can be a reference of a subsection in Related Work. 

# 1 Task Definition
Video Diffusion Models aims to generate videos from text prompts or images using diffusion methods. 

A typical diffusion-based methods typically include:
- a feature extractor that computes embeddings from input. 
- a VAE model for implicit representation 
- a neural network that denoising feature from a certain space

As a type of generation model, video generation derivate many similar characters from image generations.  As we also know, videos are sequences of images.  But video also proposes many issues that requires specific solutions. 


## branches 
# 2 Current Exploration
current exploration can be seen as isomorphism to the exploration of image. 

## 2.1 GAN models
there exist quite a few works using GAN to video generation. But I still haven't seen any of them yet. So this part is omitted. 

## 2.2 Custom Image Diffusion Models
[[Diffusion/Video Diffusion/AlignYourLatents|AlignYourLatents]],[[Diffusion/Video Diffusion/ControlVideo|ControlVideo]] both aims to generate videos directly using a pertrained diffusion models. 

## 2.3 Cascade Diffusion Models
[[Code Review/Project/LVDM|LVDM]],[[Code Review/Project/VideoCrafter|VideoCrafter]] get the idea from Latent Diffusion Models, they use hierarchical design to reduce resource consumptions. 


## 2.4 Generation Backbone exploration
[[Diffusion/Video Diffusion/Latte|Latte]] try to replace Unet with a newly design SS and TS for generation. 
Open-Sora系列也是基于Diffusion Transformer做的。 


# 3 Topics

## 3.1 video specific issues
The generation target, video , itself contain many new characters that may not exist or at least not exist together. 
### 3.1.1 temporal coherence
时间维度上的质量控制是现在VideoDiffusions的关键问题。 

VideoVAE上能做出什么样的改进呢？ 要先训练一版来看看才知道。 

目前常见的时间信息的控制方法包括: 
- Mask and Interpolation prediction 
- Auto Regressive Modeling 

除此之外还有对attention机制的微改:
- 将输入连接成大图作为attention的输入


### 3.1.2 long video generation 

- 利用自回归的方法延长视频生成
- 层次化生成：关键帧+帧间补全
- DDIM采样结果的重用 

### 3.1.3 resources reduction

### 3.1.4 image quality 

### 3.1.5 domain-specific generation

### 3.1.6 visual conditioning

## 4 Dataset
缺乏清晰的视频数据集让训练VideoDiffusion模型受到一定限制。 
一些列工作[[Diffusion/Video Diffusion/AlignYourLatents|AlignYourLatents]],[[Code Review/Project/VideoCrafter|VideoCrafter]]都探索过利用高质量的图片数据集提升Video的图片质量。 

- Dataset Construction 
- Dataset Curation 
## 4.1 Video Dataset 

### Sky_timelapse
全部都是天空的图片

640$\times$ 360 RGB 图片
训练集 32 $\times$ 35383 图片
测试集 32 $\times$ 2815 图片

### WebVid-10M
Large-scale text-video dataset, **containing 10 million video-text pairs** scraped from the stock footage sites
1千万视频文本对
视频总时长约5.2w小时


## 4.2 Image Dataset
### Pick A PIC  v2
990000+对图片

## 4.3 Build Dataset 
创造一个新的数据集通常有两种方式：重新爬数据和筛选数据
后一种的工作量会稍微小一些。 
在构造数据集之前，需要考虑好数据集的用途和结构。 
这里构造新的数据集的论文有:
- MagicTime - Youtube

做了数据筛选的论文有:
- Stable Video Diffusion 
- Follow Your Pose - LAION-pose 
- Follow Your Click - WebVid-motion

### 4.3.1 Dataset Construction

### 4.3.2 Dataset Curation 

- 用BLIP或者LLM重写caption
- 用CLIP aesthetic做评分
- 用Detection和Segmentation做评分 

