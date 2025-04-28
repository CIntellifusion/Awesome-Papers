# Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers


end-to-end 训练latent video diffusion。 

> Traditional deep learning wisdom dictates that end-to-end training is often preferable when possible. 

过去的经验告诉我们，end-to-end的training如果可能是更好的。 

## Motivation

这个paper想要解决的问题是： end-to-end的训练latent Diffusion和 variantional auto encoder。 

用Repa loss 连着vae进行train。 

![[Pasted image 20250418213042.png]]

![[Pasted image 20250418213136.png]]
用repa-e之后的vae的latent space再做pca之后的结果。 
![[Pasted image 20250418215313.png]]

vae latent的方差会被预测进误差。

## 在VAE上不能apply diffusion loss 
VAE的latent space有一个方差sigma，在SD和MAR都被rescale到1。 LatentLM里面直接给sigma取了一个定值。 

如果你e2e的denoise，vae的latent space的方差会逐渐降低，然后让denoise 预测任务更加简单。 


## REPA Loss和Fix VAE
这样的时候cknna score会收敛到0.4 

## 方差在latent space里面的作用



# Implementation 

在训练diffusion的时候，先对vae做recontruction loss和repa的loss。 repa计算的层是dit里面的层。 
做完这次loss之后，再做diffusion loss 和repa loss更新dit模块。 
## end2end在哪里呢

这个里面是两个optimizer分别优化vae的parameter， 和dit的parameter。 
这样做是有好处的，但是这样做的好处不是end2end，可能是一种joint training





用alignment loss作为final generation的代理 

## repae summary

这篇文章提出end2end去同时优化vae和diffusion。 在训练的时候，先用vae loss和repa loss去优化vae。 再用diffusion loss和repa loss去优化dit。 两次repa的loss共用一组projector。 然后实验结果显示vae和diffusion的效果都可以同时变好。 

e2e-vae和va-vae都对vae的latent space加了dino约束，但e2e-vae能比va-vae效果更好是因为vae和dit是轮流优化的。 但是我感觉是paper里的vae loss和diffusion和repa loss都是分别作用在vae和dit上的，不像是完全的e2e，更接近iteratively优化vae和diffusion model。 

受到这个启发，我在想vae 的latent space还有什么性质可能有用的。 比如让vae对噪声可以是robust的，即有$\text{enc}(x) \cdot \alpha_t + \epsilon \beta_t = \text{enc}(\gamma_t \cdot x + \epsilon \sigma_t)$ 。 但是这个性质就是让vae退化成了一个线性变换，而且会让vae丧失掉语义信息。 


### 受到关于 VAE latent space 结构讨论的启发

我在想，如果给 image space 和 VAE latent space 加上一个同构的约束，比如：

- `x` 是归一化后的图片
- `t` 是 timestep
#### 标准的 Diffusion 流程：
1. $z = \text{enc}(x)$  
2. $z_t = \alpha_t \cdot z + \epsilon \beta_t$  
3. $\hat{\text{noise}} = \text{model}(z_t, t)$
#### 如果先在图片上加噪音，再进行编码（enc）成向量：

1. $z_t = \text{enc}(\gamma_t \cdot x + \epsilon \sigma_t)$  
2. $\hat{\text{noise}} = \text{model}(z_t, t)$

其中，$\gamma_t$ 和 $\sigma_t$ 是加在 image space 上的噪声和方差，表示在输入图像上添加的噪声扰动。

### 关于 Gamma_t 和 Sigma_t 的关系

存在一组满足以下关系的 \( \gamma_t \) 和 \( \sigma_t \)，即：

$\text{enc}(x) \cdot \alpha_t + \epsilon \beta_t = \text{enc}(\gamma_t \cdot x + \epsilon \sigma_t)$

其中，\( \gamma_t \) 和 \( \sigma_t \) 是在图像空间上加的噪声和方差。这个公式的意思是，通过噪声扰动（由 \( \gamma_t \) 和 \( \sigma_t \) 控制）来模拟 Diffusion 过程。

### VAE 在训练 Diffusion 时的目标

VAE 是否在训练过程中学习去输入带有噪声的 latent \( z_t \) 来重建带有噪声的图像 \( x_t \)，或者直接重建没有噪声的原始图像 \( x_0 \)？

#### 关键点：
1. **带噪声的输入：** VAE 在训练过程中，可能会学习如何处理带有噪声的 latent 向量 \( z_t \)。
   
2. **重建带噪声的图像：** 这意味着 VAE 不仅仅是学习重建干净的图像 \( x_0 \)，而是学习如何从带噪声的 \( z_t \) 恢复到一个带噪声的图像 \( x_t \)。
   
3. **鲁棒性：** 如果 VAE 学会了如何处理和重建带有噪声的 latent 表示，理论上它会变得更加鲁棒。这样训练出的 VAE 可能在ldm生成过程中具有更强的抗噪声能力。

### 对噪声更鲁棒的 VAE

- 训练得到的 **鲁棒 VAE**，可能会让模型在生成任务中更稳定，尤其是在处理带有噪声或不完全信息的输入时。
- 更加鲁棒的 VAE 可以更好地生成图像，尤其是在 **LDM（Latent Diffusion Model）** 中，可以作为一个更加有效的tokenizer。

