---
Date: 2024-04-02
Title: VAR 自回归图片生成
dg-publish: true
---

# 1 Introduction

## 1.1 Problem Statement
任务是图片生成任务。 
方法是利用自回归方式做分辨率提升。 
motivation:借鉴了NLP领域的研究思路，主要关注scaling law和zero-shot两个属性。 

> 借鉴NLP研究思路这个想法可以追溯到ViT。 zero-shot能力在CLIP里面讨论了很多。 


尽管大模型有幻觉之类的局限，但是AR的LLM在scalbility和generalizability两个方面非常突出。 但是自回归的图片生成模型VQ-GAN和Dalle-E的效果长期不如Diffusion的模型。  然后一个自然而然的问题产生了:

**the power of autoregressive models in computer vision appears to be somewhat locked.**
![Image](https://pic4.zhimg.com/80/v2-244ad451dc8acb095adb0b1408a81adc.png)

作者展示了在不同的模型大小不同的backbone的模型的FID，他们在下降的时候明显有一个平台。 然后作者认为，自回归的模型要求数据有序，所以需要重新考虑如何在图片数据上建立一个有效的序列。  在下图中可以看到，他们将图片的大小作为一个序列，用一种逐渐清晰的方式生成图片。

> 这个图让人想起了progressive gan. 从低分辨率到高分辨率进行训练。 

![Image](https://pic4.zhimg.com/80/v2-25ecbaddec679f9c27c6b341ab7aabaa.png)

## 1.2 Stated Contribution

![Image](https://pic4.zhimg.com/80/v2-20a9fc1ef0817766947d5720e7c20364.png)

- 一种新的AR模式，图的右边部分，按照分辨率自回归。 
- 超过DiT的性能(DiT做image的工作还没看过，挖坑)，注意到他们的backbone都是transformer
- 接近理论下限的FID结果

# 2 Related Work

## 2.1 Scaling Laws
幂律缩放定律（Power Law Scaling Laws）用数学方法描述了模型参数、数据集大小、计算资源与机器学习模型性能提升之间的关系。这些关系带来了几个明显的好处：

1. **预测模型性能**：通过扩大模型规模、数据规模和计算成本，可以推断更大模型的性能，从而节省不必要的成本，并为分配训练预算提供原则。
2. **持续性能提升**：缩放定律表明模型性能会持续且非饱和地增长，证实了其在增强模型能力方面的持续优势。

基于这些定律的原理，许多大型语言模型被提出，这些模型展示了模型规模与性能之间的正相关关系。以下是一些关键例子：

- **GPT（Generative Pre-trained Transformer）**：基于Transformer，经过生成预训练，将模型规模扩展到前所未有的1750亿个参数。
- **LLama**：发布了一系列预训练和微调的大型语言模型，规模从70亿到700亿个参数不等。

## 2.2 zero-shot generation
Zero-shot generalization是指一种模型，特别是大型语言模型，在没有经过明确训练的情况下执行任务的能力。在视觉领域，对基础模型（如CLIP [47]、SAM [35]、Dinov2 [44]）的零样本学习和上下文学习能力的兴趣日益增长。
以下是一些关键的创新例子：

- **CLIP**: 利用视觉和文本联合训练模型，通过图像和文本匹配实现零样本学习。
- **SAM**: 作为一种视觉基础模型，通过广泛的图像数据训练，能够在未见过的任务中进行泛化。
- **Dinov2**: 在视觉任务中使用零样本学习和上下文学习来提升性能。

## 2.3 Visual Generation 
### 2.3.1 Image tokenizer and autogressive models

VQVAE;VAGAN;ViT-VQGAN

### 2.3.2 Mask Prediction Model

在VQ空间上进行贪心预测。 MUSE,MaskGIT

## 2.3.3 Diffusion models

Imagen; LDM； DiT

# 3 Method
## 3.1 autoregressive modeling via next-token prediction

将图片展开为image token然后做序列预测的方法可以用以下公式表示:
![Image](https://pic4.zhimg.com/80/v2-7af694dbdead2646c01581323ef217ac.png)

这样的方法有三个问题:
1. Image encoder输出的特征图通常和i,j内在依赖，展开破坏了这种依赖性
2. 图片有四个相邻的邻居，天然的有空间的局部性。 (参考卷积的设计思路)。 展开为线性的序列就只有前后两个邻居了。 
3. 序列token generation的复杂度为六次方 
## 3.2 autoregressive modeling via next-level prediction

通过预测不同尺寸的图片，记不同尺寸的图片由分辨力从低到高分别是r1,...,rk,预测任务变成了

![Image](https://pic4.zhimg.com/80/v2-45904a59c56d7d7c66aeb634e639b2a9.png)
VAR是这样解决以上问题的：
1. 为了满足数学前提，我们需要约束每个生成步骤 𝑟𝑘rk​ 仅依赖于其前缀，即 𝑟𝑘rk​ 的生成过程只与 (𝑟1,𝑟2,…,𝑟𝑘−1)(r1​,r2​,…,rk−1​) 有关。
2. 在每个 𝑟𝑘 中的标记是完全相关的，多尺度设计进一步增强了空间结构。
3. 生成一个 𝑛×𝑛n×n 潜在图像的复杂性显著降低到 𝑂(𝑛4)O(n4)。这种效率的提升来自于每个 𝑟𝑘rk​ 中的并行标记生成。

![Image](https://pic4.zhimg.com/80/v2-f8505d0ea7411ecd376375c7c10d9c30.png)

训练了一个多尺度的VQVAE 
# 4 Experiment
## 4.1 Scaling Law
![Image](https://pic4.zhimg.com/80/v2-a68644d7f9ef9ec1b30c3770aa337208.png)

# 5 Summary

在分辨的尺度上进行AR预测，和之前的丢失相邻信息的ViT等AR的方法有了本质的不同。 
证明了这个模型的scaling law.
给后续工作又一次证明了CV可以借鉴LLM的思路

# 6 Future Work
