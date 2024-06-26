---
Date: 2024-04-02
Title: Latent Diffusion
dg-publish: true
---
Latent Diffusion的贡献在于把扩散-去噪过程从图片转移到了隐空间。 既然是隐空间，这就意味着拥有了在其他任务上推广的潜力。 ，如何将图片生成模型扩展到其他任务上。


# Brief Review
详细的推导看[[Diffusion/Unconditional Diffusion|Unconditional Diffusion]]和[[Diffusion/Classifier-free Diffusion Guidance|Classifier-free Diffusion Guidance]]



方法部分照例还是一个LDM起手，这里就不再赘述，并且偷懒使用模版了。 
扩散模型通常由两个过程组成：前向扩散和逆向去噪。 给定输入信号 $x_0$，前向扩散过程定义如下： 

$$ p_\theta( x_t | x_{t-1} ) = \mathcal{N} \left( \sqrt{\frac{1 - \beta_{t-1}}{\beta_t}} x_{t-1}, \sqrt{\frac{\beta_t}{1 - \beta_{t-1}}} I \right) $$

其中  $t = 1, \ldots, T$ 是时间步， $\beta_t \in (0, 1)$  是噪声计划。当总时间步 $T$ 足够大时，结果  $x_t$最终逼近高斯噪声  $\mathcal{N}(0, I)$。 逆向去噪过程的目的是学习如何逆转前向扩散并逐步去除噪声，如下所示： 

$$ q_\theta( x_{t-1} | x_t ) = \mathcal{N} (x_{t-1}; \epsilon_\theta(x_t, t), \Sigma(x_t, t)) $$

其中  $\Sigma(x_t, t)$ 通常不需要训练，而是基于时间步  $t$  作为固定方差来计算。它只需要预测逆过程中的均值  $\mu_\theta(x_t, t)$ ，并且这一步也可以简化为训练去噪模型  $\epsilon_\theta(x_t, t)$  来预测  x_t  的噪声  $\epsilon$ ： 

$$ L = \mathbb{E}_{q_{\epsilon \sim \mathcal{N}(0,I)}, t} \left[ \left\| \epsilon - \epsilon_\theta(x_t, t, \tau_\theta(y)) \right\|_2^2 \right] $$

其中  $y$ 是文本条件， $\tau_\theta(\cdot)$  是文本编码器。

