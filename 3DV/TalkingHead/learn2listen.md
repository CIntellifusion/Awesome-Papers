---
Date: 2024-10-12
Title: "[CVPR22] Learning to Listen: Modeling Non-Deterministic Dyadic Facial Motion"
dg-publish: true
tags:
  - CVPR22
---

# 1 Introduction

## 1.1 Problem Statement
Input: speaker status(motion+audio) + listener past motion 

Output: listener status(future motion)
(To avoid lose general sense, we summary 3D motion, audio and other information into status)

Problem&research motivation: modeling non-verbal feedback during dyadic(二元的) interaction.

Application scene: human conversation eg. live stream, live interviews. 




## 1.2 Stated Contribution
Observation: listener motion is naturally non-determinstic , multi-modal and discrete, taking a subspace of the whole motion state space. 

Contribution: 
1. collect dual speaker in-the-wild dataset 
2. first using vqvae to model the motion distribution 
# 2 Related Work

# 3 Method

> 这个文章还专门写了problem definition,挺好的

## 3.1 Problem Definition 
这里我们需要定义t时刻的facial motion$f_t$: 
$$
f_t = [\beta_t,{R}_t]
$$
定义T步的facial motion sequence为$F=\{f_i\}_{i=0}^T$,Lisener和Speaker的facial motion sequence分别是$F^L,F^S$,定义语音序列是A。 那么我们需要学习一个listener motion predictor $\mathcal{P}$:
$$
\hat f^s_t = \mathcal{P}(F_{1:t}^S,A_{1:t}^s,\hat F^L_{1:t}) 
$$
,$\mathcal{P}$学习的是这样一个条件概率分布
$$
p(\hat f^s_t|F_{1:t}^S,A_{1:t}^s,\hat F^L_{1:t}) 
$$
## 3.2 Listener motion codebook
这个部分要学的是listener所做出的常见动作的离散的隐式特征。 与图片生成配套的vqvae不同的是，这里是一个时间序列。 
Solution: transformer-based, sequential encoding VAE 
## 3.3 Cross-Modal Attention for Speaker Input
用Cross Attention去实现audio feature和motion feature的交互
## 3.4 Transformer-based Listener Predictor
pass

# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

## 5.1 Relative Position
# 6 Comments

