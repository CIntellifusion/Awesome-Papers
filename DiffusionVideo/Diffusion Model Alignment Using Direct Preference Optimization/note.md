
# 0 Background

## 0.0 RLHF
人类反馈强化学习 
RLHF 是一个复杂且经常不太稳定的过程，它首先拟合一个**反应人类偏好的奖励模型**，然后通过强化学习对大型无监督 LM 进行微调以最大化评估奖励，并避免与原始模型相差太远
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401165125.png]]
这里$y_1 > y_2$是偏序关系，表示在prompt x下y1好于y2 
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401165133.png]]
## 0.1 DPO for LLM 

在本文中，我们使用奖励函数和最优策略间的映射，展示了约束奖励最大化问题 **完全** 可以通过单阶段策略训练进行 **优化** ，从本质上解决了人类偏好数据上的分类问题。我们提出的这个算法称为直接偏好优化（_Direct Preference Optimization，DPO）。它具有稳定性、高性能和计算轻量级的特点，不需要拟合奖励模型，不需要在微调时从 LM 中采样，也不需要大量的超参调节。
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401165348.png]]
**一个重要的贡献是:跳过显式的奖励建模步骤**
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240402085346.png]]
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240402085355.png]]
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240402085550.png]]
(5)->(1)=(6)
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240402085614.png]]
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240402090030.png]]
# 1 Problem Statement
LLM可以根据人类偏好进行优化，但是在文生图领域很少在训练过程中考虑对人类偏好的优化。


# 2 Method
## 2.1     Diffusion Models

## 2.2 Direct Preference Optimization 

### 2.2.1 奖励函数
用BT模型建模人类偏好，数据集构造为$D=\{(c,x_0^w,x_o^l)\}$ 分别表示条件，好的结果，坏的结果
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401202234.png]]
注意到此处BT模型和[[#0.0 RLHF]]中的BT模型形式不同，但是带入Sigmoid公式
$$
S(x)=\frac{1}{1+e^{-x}}=\frac{e^{x}}{1+e^{x}}
$$
可以得到
$$
P_{BT}(x_0^w>x_o^l|c) = \frac{exp(r(c,x_0^w)-r(c,x_0^l))}{1+exp(r(c,x_0^w)-r(c,x_0^l))}=\frac{e^{r(c,x_0^w)}}{e^{r(c,x_0^l)}+e^{r(c,x_0^w)}}
$$
就和之前的式子是相同结构了。 
然后用二分类问题利用极大似然训练。 
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401203602.png]]

### 2.2.2 RLHF
RLHF训练过程中一方面最小化$r(c,x_0)$的期望，另一方面降低两个分布的KL散度 
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401203955.png]]
### 2.2.3 DPO Objective 
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240401204941.png]]

这里他做了一个没看懂的参数重整化
## 2.3    DPO for Diffusion models 
这一节关注把DPO从LLM改到Diffusion上面,数据集记为$D=\{(c,x_0^w,x_o^l)\}$ 
![[DiffusionVideo/Diffusion Model Alignment Using Direct Preference Optimization/picture/Pasted image 20240402085831.png]]
> 为什么呢

解决这个问题之后，把Loss简化一下，就开始训练。 



# 3 实验

DDPO：参考模型 

| config     | value                                             |
| ---------- | ------------------------------------------------- |
| base model | SD.15 SDXL1.0                                     |
| dataset    | Pick-a-Picv2 851,293 pairs, 58,960 unique prompts |
| evaluation | PickScore Hps CLIP                                |
| GPU        | 16 A100 local batch size of 1 128 steps.          |
|            |                                                   |


