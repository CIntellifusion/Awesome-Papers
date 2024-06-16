---
Date: 2024-06-08
Title: 
dg-publish: true
tags:
  - RLHF
  - LLM
---

# 1 Introduction

## 1.1 Problem Statement

DPO是一种离线的偏好学习优化算法，通过重参数化强化学习中的奖励函数来学习人类偏好，同时加强训练的稳定性和简单性。 SimPO是一种更加简单有效的方法:用一个序列的平均对数概率作为隐式的奖励。 
- 更好的和模型生成过程对齐，不需要reference model 
- 计算更加简单，内存消耗更少 

## 1.2 Stated Contribution
![Image](https://pic4.zhimg.com/80/v2-fe6ded1590b23ee9da45724848128c1a.png)

DPO的公式
$$
\begin{aligned}
& \mathcal{L}_{\mathrm{DPO}}\left(\pi_\theta ; \pi_{\mathrm{ref}}\right)= \\
& -\mathbb{E}\left[\log \sigma\left(\beta \log \frac{\pi_\theta\left(y_w \mid x\right)}{\pi_{\mathrm{ref}}\left(y_w \mid x\right)}-\beta \log \frac{\pi_\theta\left(y_l \mid x\right)}{\pi_{\text {ref }}\left(y_l \mid x\right)}\right)\right]
\end{aligned}
$$

SIMPO公式
$$
\begin{aligned}
& \mathcal{L}_{\mathrm{SimPO}}\left(\pi_\theta\right)= \\
& -\mathbb{E}\left[\log \sigma\left(\frac{\beta}{\left|y_w\right|} \log \pi_\theta\left(y_w \mid x\right)-\frac{\beta}{\left|y_l\right|} \log \pi_\theta\left(y_l \mid x\right)-\gamma\right)\right]
\end{aligned}
$$

注意，SimPO不需要一个reference model，这意味着这个训练的时候需要的显存的数量可以大大减少了。 



# 2 DPO preliminaries
r是一个奖励函数，一个带有闭式解的表达式作为优化策略：
$$
r\left(\boldsymbol{x}, \boldsymbol{y}\right)=\beta \log \frac{p_\theta^*\left(\boldsymbol{y} \mid \boldsymbol{x}\right)}{p_{\text {ref }}\left(\boldsymbol{y} \mid \boldsymbol{x}\right)}+\beta \log Z(\boldsymbol{x})
$$

然后用Bradly-Terry排序目标 
$$
p(y_{w}> y_{l}|x) = \sigma(r(x,y_{w}),r(x,y_{l}))
$$
得到DPO的优化目标：最小化负对数的BT:
$$L_{\mathrm{DPO}}(\theta)=-\mathbb{E}_{\boldsymbol{c}, \boldsymbol{x}_0^w, \boldsymbol{x}_0^l}\left[\log \sigma\left(\beta \log \frac{p_\theta\left(\boldsymbol{x}_0^w \mid \boldsymbol{c}\right)}{p_{\mathrm{ref}}\left(\boldsymbol{x}_0^w \mid \boldsymbol{c}\right)}-\beta \log \frac{p_\theta\left(\boldsymbol{x}_0^l \mid \boldsymbol{c}\right)}{p_{\mathrm{ref}}\left(\boldsymbol{x}_0^l \mid \boldsymbol{c}\right)}\right)\right]$$


# 3 SimPO: Simple Preference Optimization

## 3.1 DPO奖励和LM生成目标之间的差异
语言模型生成一个序列的时候是通过最大化平均对数似然(maximizes the average log likelihood)：
$$
p_\theta(y \mid x)=\frac{1}{|y|} \log \pi_\theta(y \mid x)=\frac{1}{|y|} \sum_{i=1}^{|y|} \log \pi_\theta\left(y_i \mid x, y_{<i}\right) .
$$
这个目标和奖励函数r有不一致的地方，也就是说$r(x,y_{w})>r(x,y_{l})$推导不出$p_{\theta}(x,y_{w})>p_{\theta}(x,y_{l})$

如下图所示，直观的可以看书r大的不一定概率大 
![Image](https://pic4.zhimg.com/80/v2-86bdee4ffd2f6caf65b627faf61f0141.png)

## 3.2 长度归一化的奖励函数

为了解决这个问题，SimPO改了奖励函数
从：
$$
r\left(\boldsymbol{x}, \boldsymbol{y}\right)=\beta \log \frac{p_\theta^*\left(\boldsymbol{y} \mid \boldsymbol{x}\right)}{p_{\text {ref }}\left(\boldsymbol{y} \mid \boldsymbol{x}\right)}+\beta \log Z(\boldsymbol{x})
$$
到
$$
r_{\mathrm{SimPO}}(x, y)=\frac{\beta}{|y|} \log \pi_\theta(y \mid x)=\frac{\beta}{|y|} \sum_{i=1}^{|y|} \log \pi_\theta\left(y_i \mid x, y_{<i}\right),
$$

这个平均最小的奖励函数和LM生成的时候的式子类似，然后就可以解决3.1里提到的问题

![Image](https://pic4.zhimg.com/80/v2-84b65c3bc49e2a2dbf102880d0d4890d.png)

## 3.3 最小奖励差距$\gamma$

$$
p(y_{w}> y_{l}|x) = \sigma(r(x,y_{w}),r(x,y_{l})-\gamma)
$$

方法部分结束
# 4 Experiment
## 4.1 Implementation Details  

![[picture/DPO-variants.png]]
# 5 Summary

从语言模型的生成过程的目标推导出了减小generation和reward之间差异的新的reward function 
去掉了对ref_model的依赖
加入了一个最小的奖励差距
得到一个简单的preference optimization loss 
# 6 Comments
有几个问题:
1. alignment对于llm的重要性要高于其对于其他模态的大模型吗？
2. 3.1的分析很有insight.

