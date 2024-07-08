---
Date: 2024-06-16
Title: Fine-tuning Diffusion Models for Enhancing Face Quality in Text-to-image Generation
dg-publish: true
tags:
  - Diffusion
  - Human
  - RLHF
  - Benchmark
---
Fine-tuning Diffusion Models for Enhancing Face Quality in Text-to-image Generation
# 1 Introduction

## 1.1 Problem Statement
DM生成的人脸有各种各样的问题，五官模糊，错位，比例不协调，纹理不自然等等。 
对人脸质量的评估不完善，没有和人类偏好对齐。 

## 1.2 Stated Contribution



# 2 Related Work
## 2.1 DM

## 2.2 RLHF


# 3 Method

## 3.1 Evaluation of DM 

1. 选1k具有代表性和多样性的图片作为测试
2. 用三个模型分别生成3张图
3. 人类标注
4. 投票决定标签
![[picture/Pasted image 20240708123747.png]]
## 3.2 Face Score benchmark


## 3.2 Preference Dataset Construction
真实图片作为正例子，补全的例子作为负例子

ranking loss： 
![[picture/Pasted image 20240708123835.png]]

![[picture/Pasted image 20240708123924.png]]
# 4 Experiment

![[picture/Pasted image 20240708124205.png]]
这个实验肯定是真的，但是效果有点碎啊 
## 4.1 Implementation Details  

# 5 Summary

## 5.1 Relative Position
# 6 Comments

太乱了写作，插图和表跟正文差十万八千里。
应该先构造benchmark
再讲方法测试
再说比较方法
然后说ft DM
然后是ft DM的实验

尝试把所有东西都塞进去，但是太拥挤了 


