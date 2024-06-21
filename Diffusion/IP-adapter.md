<<<<<<< Updated upstream

---
=======
#! https://zhuanlan.zhihu.com/p/704329549
<!-- ---
>>>>>>> Stashed changes
Date: 2024-06-19
Title: IP-adapter
dg-publish: true
tags:
<<<<<<< Updated upstream
  - Diffusion 
  - Personalization
---

=======
  - Diffusion
  - Personalization
--- -->
>>>>>>> Stashed changes

# IP-Adapter
# 1 Introduction

## 1.1 Problem Statement
预训练的文生图模型是非常强大的通用图片生成器。 但是在一些个性化的，需世界知识的情况下，生成效果不太好。 为了生成好的图片，需要的提示工程的付出非常庞大。 research gap就是要解决prompt engineering的问题，让提示词更加高效。让扩散模型更加高效的满足用户的需求。 


> 个人认为foundational diffusion model有这个问题的原因是: 训练数据集过大而拟合的distribution过于一般。 


## 1.2 Stated Contribution

- 一个轻量的adapter处理image prompt，解耦cross attention来做微调
- IP-adapter是可以重用的，而且非常灵活，并且可以和其他的adapter一起使用
- 支持image prompt的多模态生成
# 2 Related Work

## 2.1 Text2Image Diffusion Models
Versatile Diffusion：统一I2V & T2V到一个模型里面
RAPHAEL： 用MoE做文生图的条件控制


## 2.2 Adapter for Large Models

PEFT的方法在LM里面用的很多了，大多都是基于插入小网络进行微调来提升模型效果的思路。 最近关于controlnet及其改进版的工作对文生图的控制能力有了非常大的启发。 后续改进的工作包括Uni-controlnet和Controlnet shuffle

![Image](https://pic4.zhimg.com/80/v2-debfd5b54c12486d19a9a25b20de8a4d.png)

# 3 Method

## 3.1 Diffusion的前置内容
损失函数：
![Image](https://pic4.zhimg.com/80/v2-606771b80835ff647d48c3289c6e43d4.png)
CFG：
![Image](https://pic4.zhimg.com/80/v2-c4e6c1d318d455c68dc98ea9889f7296.png)

## 3.2 Image Prompt Adapter

### 3.2.1 Image Encoder
用一个冻住的CLIP Image Encoder做图片编码器，后面跟可以训练的线性层和LN来对其编码特征。

### 3.2.2 Decouple Cross-Attention

编码好了图片之后就是应该考虑如何把图片特征和文本特征融合到一起。 

Q是输入的隐向量Z作为query，K V是文本提示词得到的特征， K‘V'是图片提示的到的特征。 融合的方法是把两个特征做attention了之后相加。 DynamicCrafter里面也是这样做的，公示基本一样。 
![Image](https://pic4.zhimg.com/80/v2-686e74a6c7c3205e79b789152baa1caf.png)

# 4 Experiment
## 4.1 Implementation Details 

以下是从给定段落中提取的关键信息：

1. **实验基础**：
   - 基于 **SD v1.52** 进行实验。
   - 使用 **OpenCLIP ViT-H/14** 作为图像编码器。

2. **模型结构**：
   - SD 模型中有 **16 个跨注意力层**。
   - 为每个跨注意力层添加一个新的图像跨注意力层。
   - **IP-Adapter** 的总可训练参数约为 **22M**，包括投影网络和适配模块。

3. **实现与训练**：
   - 使用 **HuggingFace diffusers 库** 实现 IP-Adapter。
   - 使用 **DeepSpeed ZeRO-2** 进行快速训练。
   - 在一台机器上使用 **8 个 V100 GPU** 进行训练，共 **1M 步**，每个 GPU 的批量大小为 **8**。

4. **优化器与学习率**：
   - 使用 **AdamW 优化器**，固定学习率为 **0.0001**，权重衰减为 **0.01**。

5. **图像预处理**：
   - 训练期间，将图像的最短边调整为 **512**，然后中心裁剪为 **512 × 512** 的分辨率。

6. **无分类器引导**：
   - 使用 **0.05** 的概率分别丢弃文本和图像，并用 **0.05** 的概率同时丢弃文本和图像。

7. **推理阶段**：
   - 采用 **DDIM 采样器**，步数为 **50**。
   - 引导尺度设置为 **7.5**。
   - 仅使用图像提示时，文本提示设为空，**λ = 1.0**。

这些关键信息涵盖了实验的基础、模型结构、实现与训练细节、优化器设置、图像预处理步骤、无分类器引导策略以及推理阶段的设置。

![Image](https://pic4.zhimg.com/80/v2-e4d0211e31604e0e063b5a84890b3485.png)

# 5 Summary

以下是从给定段落中提取的关键信息：

1. **信息丢失问题**：
   - **IP-Adapter** 使用来自 **CLIP 图像编码器** 的全局图像嵌入，可能会丢失参考图像中的某些信息。

2. **细粒度特征条件**：
   - 设计了一个基于细粒度特征的 **IP-Adapter**。
   - 首先，从 **CLIP 图像编码器** 的倒数第二层提取网格特征。
   - 使用一个小型查询网络来学习特征。
   - 具体地，定义了 **16 个可学习的 token**，使用轻量级 transformer 模型从网格特征中提取信息。
   - 查询网络的 token 特征作为输入提供给跨注意力层。

3. **实验结果**：
   - 两种适配器的结果如 **图11** 所示。
   - 使用细粒度特征的 **IP-Adapter** 可以生成与图像提示更一致的图像。
   - 细粒度特征适配器可以学习空间结构信息，可能会降低生成图像的多样性。
   - 可以结合额外的条件（如文本提示和结构图）与图像提示生成更具多样性的图像。
   - 例如，可以在额外的人体姿势指导下合成新的图像。

这些关键信息涵盖了 IP-Adapter 在使用全局图像嵌入时的信息丢失问题、细粒度特征条件的设计、实验结果的观察以及如何通过额外条件来增加生成图像的多样性。

# 6 Comments

## 6.1 relative position
task : text2image 
user need: personalization 
method: finetuning - adapter-based finetuning 
