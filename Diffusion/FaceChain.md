---
Date: 2024-06-26
Title: FaceChain
dg-publish: true
tags:
  - Diffusion
  - Human
  - Personalization
---

# FaceChain: A Playground for Human-centric Artificial Intelligence Generated Content

# 1 Introduction

## 1.1 Problem Statement

Existing issues:
- unique charateristics,shape-feature positioning 
- 生成的人脸可能会有翘曲，模糊，崩塌的部分


## 1.2 Stated Contribution

Solution：
融合现存的人脸的大量SOTA模型（人脸检测，人脸特征提取，人脸属性识别），提升个性化人脸生成的过程中的label-tagging,data-processing andmodel post processing的效果。 

# 2 Related Work

# 3 Method

## 3.1  Dataprocessing

### 3.1.1 Face Extraction
首先做人脸的旋转，先旋转整个图片，然后根据关键点旋转人脸区域。 
第二步是做人脸裁剪和分割，将人脸区域裁剪成合适大小
第三部做Face retouching，修复人脸上不光滑的区域。 

### 3.2.2 Label Tagging

给人脸图片标注出性别，年龄等人脸特征，供lora学习


## Model Training

Style-LoRA模型是生成稳定风格的肖像画的基石。对于个人肖像生成来说非常重要，因为它为图像生成模型设定了边界。主要的Style-LoRA模型与FaceChain结合使用，专门针对个人肖像，并使用大量相同风格的肖像图像（如身份证照片）进行训练。这里公开了训练LoRA模型时使用的超参数：LoRA模型的秩设置为32，学习率设置为1e-4，并且采用了余弦重启调度策略。LoRA模型训练了20个周期以产生最终模型。为了节省训练硬件，我们部署了8位的AdamW优化器。

至于face-LoRA模型的训练，首先根据图像旋转模型预测的角度对用户上传的图像进行旋转。然后，使用基于人脸检测和关键点输出的人脸对齐方法，以获取包含正面看向镜头的人脸图像。接下来，我们使用人体解析模型和人像美化模型来获取高质量的人脸训练图像。之后，我们使用人脸属性模型和文本注释模型，结合标签后处理方法，为训练图像生成细粒度的标签。最后，我们使用上述图像和标签数据对Stable Diffusion模型进行微调，以获得face-LoRA模型。

![[picture/Pasted image 20240626172949.png]]

在Stable Diffusion模型生成初步肖像后，FaceChain通过以下几个后期处理模块来提高肖像的细节和相似度：
1. **模板人脸选择**：使用Face Quality Assessment (FQA)模型评估用户上传图像中所有人脸的质量得分，并选择得分最高的人脸作为融合模板。
2. **人脸融合**：利用选定的模板人脸对生成的肖像进行人脸融合，以改善面部细节，使输出肖像保留主要外观特征，同时展现更精细的面部细节。
3. **相似度排名**：通过与模板人脸的面部相似度比较来选择最终输出的肖像。
4. **随机温度缩放（RTS）**：使用RTS模型计算生成肖像与输入图像之间的面部相似度，选择相似度高的肖像作为输出。
这些模块的目的是确保生成的肖像在保持用户特征的同时，具有高质量和逼真的细节。


# 4 application
![[picture/Pasted image 20240626173646.png]]


# 5 Summary

帮我们验证了几个事情
1. text condtion是需要的
2. 多种图片预处理是需要的 retouching也是
3. audio driven也是有效的 
# 6 Comments

citable

