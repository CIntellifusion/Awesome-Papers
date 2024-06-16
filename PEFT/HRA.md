---
Date: 2024-04-02
Title: HRA
dg-publish: true
tags:
  - PEFT
---

# 1 Introduction

Gaoling RUC and BIT

## 1.1 Problem Statement

大模型微调技术探索。 
LORA 和 OFT 都可以被总结为 adapter-based fine-tuning
LORA假设对预训练模型的微调产生的改变量矩阵($\Delta W$)是低秩的。 (我感觉这句话对LORA的总结非常到位,犹如醍醐灌顶)； [[PEFT/Lora|Lora论文精读]]
OFT(Orthogonal Fine-Tuning） 保留了神经网络向量之间的夹角，惩罚了预训练模型和微调模型之间的差异。 
HRA定义一列可学的的Householder relfections(HRs)相乘到预训练模型权重上。 

## 1.2 Stated Contribution

正交微调和低秩分解是常见的大模型微调技术，本文将两个技术利用HoseHolder reflection统一起来。 
除此之外通过正交约束的强度可以让模型在容量和规范性之间平衡。 

![[picture/Pasted image 20240529202240.png]]
# 2 Related Work

## 2.1 Lora
LoRA将微调的矩阵分解成两个低秩矩阵来进行学习，最后合并到原来的权重矩阵上。 
Lora的改进工作可以分为三个方向
- 结构调整。 VeRA: 把冻结的低秩矩阵共享到所有层，然后学习缩放参数。 DyLoRA学习不同秩的矩阵然后自动选择一个最优的秩。 AdaLoRA基于对原矩阵的重要性进行参数剪枝。 
- 初始化改进。 DoRA把原来的权重矩阵分解为 大小和方向 进行微调。 PiSSA对每个原矩阵做SVD。 
- 参数量化。 QA-LoRA用group-wise quantization vector在模型的调整强度上做了控制。 

（这个总结能力太强了QAQ)
## 2.2 OFT
OFT相比于LORA有更强的理论依据。 用正交性控制了微调模型和预训练模型差异的上界。 
OFT 方法采用 Cayley 参数化生成块对角正交矩阵。
BOFT [30] 引入了蝴蝶因式分解法从一连串结构稀疏矩阵中生成一个更稠密的正交矩阵。

正交性对训练更加鲁棒高效的模型有不错的作用。 

# 3 Method

## 3.0 Householder Reflections
一个 Householder 反射器：H是一个正交矩阵，其作用是将一个向量  x 反射到某个超平面上，使得结果向量在该超平面内。形式上，可以定义为：  
$$H = I - 2 \frac{vv^T}{v^Tv} $$其中I是单位矩阵，v  是一个向量。

- **QR 分解**: Householder 反射器常用于 QR 分解中的正交化步骤。QR 分解是将一个矩阵A  分解为一个正交矩阵Q和一个上三角矩阵R。
- **计算稳定性**: Householder 反射器的使用能够提高数值计算的稳定性，尤其是在处理浮点运算时。
# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

# 6 Comments

