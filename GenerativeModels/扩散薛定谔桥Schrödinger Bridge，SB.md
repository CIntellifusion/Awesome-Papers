---
Date: 2024-06-16
Title: Template
dg-publish: true
tags:
---
[扩散薛定谔桥和最优传输 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/690392523)

# 1 Introduction

## 1.1 Problem Statement

### 1.1.1 最优传输问题Optimal Transport(OT)

Problem 1 (Optimal Mass Transport). Suppose $(X, \mu),(Y, v)$ are metric space with probabilities measures, which have the same total mass $\int_X \mu d x=\int_Y \nu d y$. A map $T: X \rightarrow Y$ is measure preserving, if for any measurable set $B \subset Y, \mu\left(T^{-1}\right.$ $(B))=v(B)$. Given a transportation cost function $c: X \times$ $Y \rightarrow \mathbb{R}$, find the measure preserving map $T: X \rightarrow Y$ that minimizes the total transportation cost

找到两个分布之间的一个变换使得这个移动成本最小。 

## 1.2 Stated Contribution



# 2 Related Work

# 3 Method

# 4 Experiment
## 4.1 Implementation Details  

# 5 Summary

## 5.1 Relative Position
# 6 Comments

# 7 DSB implementation analysis

https://github.com/checkcrab/SDSB/blob/main/util/runner.py

DSB会有backward_model和forward_model两个部分，分别放进两个独立的优化器中。 

DSB自己实现了一个Noiser，负责创建样本x_0和样本x_1之间变换的每个时间步的取值组成的轨迹,噪音的轨迹，时间步的轨迹。 





