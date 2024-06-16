---
Date: 2024-04-02
Title: Unconditional Diffusion公式推导
dg-publish: true
tags:
  - Diffusion
---

# 0 符号定义
记图片为x,在扩散模型中，通过给 $x_0$ 逐步添加噪音得到一个图片序列$x_0,x_1,x_2,...,x_T$。 其中 $x_0$表示输入图片，即不含噪音的初始图片，$x_T$表示各项同性的高斯噪音。
前向加噪音过程:$q(x_t|x_{t-1})$ 表示 以 $q$ 为加噪音方法,对 $x_{t-1}$ 加噪音获得 $x_t$
后向去噪过程: $p(x_{t-1}|x_t)$ 表示 用神经网络 $p$ 表示对 $x_t$去噪得到 $x_{t-1}$ 

# 1 推导

## 1.1 前向过程

设$\beta$为加噪过程的超参数，用来控制加噪音量。 给定 $\beta$ 的最小和最大值，通常为$[0.0001,0.02]$， 加噪音过程可以表示为
$$
\begin{equation}
\begin{split}

q(x_t|x_{t-1}) &= \mathcal{N}(x_t;\sqrt{1-\beta_t} x_{t-1}, \beta_t I)\\
& = \sqrt{1-\beta_t} x_{t-1}+\beta_{t }\epsilon 
\end{split}
\end{equation}
$$
在等式的右边 $\mathcal{N}$ 表示正态分布， $x_t$ 表示输出， $\sqrt{1-\beta_t} x_{t-1}$ 表示均值， $\beta_t I$表示方差, $\epsilon$ 从 $\mathcal{N}(0,1)$ 中采样。

重新整理一下参数:

$$
\begin{split}
\alpha_{t} = 1-\beta_{t}\\
\overline \alpha_{t} = \prod_{s=1}^{t} \alpha_{s}
\end{split}
$$

那么


$$
\begin{equation}
\begin{split}
& q(x_t|x_{t-1}) =\sqrt{ \alpha_{t}  }x_{t-1}+ (1-\alpha_{t})  \epsilon \\ 
& q(x_{t-1}|x_{t-2 })=\sqrt{ \alpha_{t-1}  }x_{t-2}+(1-\alpha_{t-1})   \epsilon \\ 
\end{split}

\end{equation}
$$

从而可以从

$$
\begin{split}
q(x_t|x_{t-1}) &=
\sqrt{ \alpha_{t}  }(\sqrt{ \alpha_{t-1}  }x_{t-2}+ \beta_{t-1} \epsilon)+ \beta_{t}  \epsilon \\ 
& \sqrt{ \alpha_{t} \alpha_{t-1}  }x_{t-2} + \sqrt{ \alpha_{t}} \beta_{t-1} \epsilon+\beta_{t}  \epsilon
\end{split}

$$
最后可以得到:

$$
\begin{split}
q(x_t|x_{0}) &= \sqrt{ \overline \alpha_{t} }x_{0} + \sqrt{  (1-\overline\alpha_{t})} \epsilon
\end{split}
$$

##  1.2 去噪过程

$$
\begin{split}
p_{\theta}(x_{t-1}|x_{t})=\mathcal{N}\left( x_{t-1};\mu_{\theta}(x_{t},t),\Sigma_{\theta}(x_{t},t) \right)
\end{split}
$$
从 $x_{t}$预测 $x_{t-1}$图片的过程是，用神经网络 $\mu_{\theta}$ 预测第t步的噪音，$\Sigma_{\theta}$是不含可学参数的。 

## 1.3 损失函数

计算Varicational Lower Bound 
$$
\begin{split}
L=-log(p_{\theta}(x_{0}))&\leq-log(p_{\theta}(x_{0}))+D_{KL}(q(x_{1:T}|x_{0})||p({x_{1:T}|x_{0}}))\\
\text{改写KL散度可得}&=-log(p_{\theta}(x_{0}))+ log \frac{q(x_{1:T}|x_{0})}{p_{\theta}({x_{1:T}|x_{0}}))}\\
\text{代入}p({x_{1:T}|x_{0}}))&=\frac{p_{\theta}(x_{0}|x_{1:T}) p_{\theta}(x_{1:T})}{p_{\theta}({x_{0}})}得:\\
&=-log(p_{\theta}(x_{0}))+ log \frac{q(x_{1:T}|x_{0})p_{\theta}({x_{0}})}{p_{\theta}(x_{0}|x_{1:T}) * p_{\theta}(x_{1:T}))}\\

\text{消去}-log(p_{\theta}(x_{0}))&= log \frac{q(x_{1:T}|x_{0})}{p_{\theta}(x_{0}|x_{1:T})  p_{\theta}(x_{1:T}))}\\
\text{改为联合概率分布}&= log \frac{q(x_{1:T},x_{0})}{p_{\theta}(x_{0},x_{1:T})}\\
\end{split}
$$
从而我们得到
$$
\begin{split}
L=-log(p_{\theta}(x_{0}))\leq log \frac{q(x_{1:T},x_{0})}{p_{\theta}(x_{0},x_{1:T})}\\
\end{split}
$$
接下来处理等式的右边:
因为:
$$
q(x_{1:T},x_{0})=\prod^T_{t=1}q(x_{t}|x_{t-1})
$$
得到:

$$
\begin{split}
log \frac{q(x_{1:T},x_{0})}{p_{\theta}(x_{0},x_{1:T})}&=
\log \frac{\prod^T_{t=1}q(x_{t}|x_{t-1})}{p({x_{T})}\prod^T_{t=1}p_{\theta}(x_{t-1}|x_{t})}\\
&=
-\log p({x_{T})+\log \frac{\prod^T_{t=1}q(x_{t}|x_{t-1})}{\prod^T_{t=1}p_{\theta}(x_{t-1}|x_{t})}}\\
连乘对数换序&=
-\log p({x_{T})+\sum^T_{t=1}\log\frac{  q(x_{t}|x_{t-1})}{p_{\theta}(x_{t-1}|x_{t})}}\\
提出第一项&=
-\log p({x_{T})+\sum^T_{t=2}\log\frac{  q(x_{t}|x_{t-1})}{p_{\theta}(x_{t-1}|x_{t})}}+\log\frac{  q(x_{1}|x_0)}{p_{\theta}(x_{0}|x_{1})}\\
贝叶斯重写&=
-\log p({x_{T})+\sum^T_{t=2}\log\frac{  q(x_{t-1}|x_{t},x_{0})q(x_{t}|x_{0})}{p_{\theta}(x_{t-1}|x_{t})q(x_{t-1}|x_{0})}}+\log\frac{  q(x_{1}|x_0)}{p_{\theta}(x_{0}|x_{1})}\\
分解中间项&=
-\log p({x_{T})
+\sum^T_{t=2}\log\frac{q(x_{t-1}|x_{t},x_{0})}{p_{\theta}(x_{t-1}|x_{t})}}
+\sum^T_{t=2}\log \frac{q(x_{t}|x_{0})}{q(x_{t-1}|x_{0})}
+\log\frac{  q(x_{1}|x_0)}{p_{\theta}(x_{0}|x_{1})}\\
化简第三项&=
-\log p({x_{T})
+\sum^T_{t=2}\log\frac{q(x_{t-1}|x_{t},x_{0})}{p_{\theta}(x_{t-1}|x_{t})}}
+\log \frac{q(x_{T}|x_{0})}{q(x_{1}|x_{0})}
+\log\frac{  q(x_{1}|x_0)}{p_{\theta}(x_{0}|x_{1})}\\

化简&=
\log \frac{q(x_{T}|x_{0})}{p(x_{T})}
+\sum^T_{t=2}\log\frac{q(x_{t-1}|x_{t},x_{0})}{p_{\theta}(x_{t-1}|x_{t})}
-\log p_{\theta}(x_{0}|x_{1})\\
改写为KL&=D_{KL}(q(x_{T}|x_{0})||p(x_{T}))
+\sum^T_{t=2}D_{KL}(q(x_{t-1}|x_{t},x_{0})||p_{\theta}(x_{t-1}|x_{t}))
-\log p_{\theta}(x_{0}|x_{1})\\



\end{split}
$$
第一个KL散度里面q不含可学习参数，可以忽略不计。
第二个KL散度地面，在“贝叶斯重写”的步骤中，加上了x_0的条件，使得KL散度里有两个$x_{t-1}|x_{t}$ 存在。 然后我们要把这个KL散度规划成一个均方误差。 
> 你们会推公式的人真的像在变魔法。

$$
=D_{KL}(q(x_{T}|x_{0})||p(x_{T}))
+\sum^T_{t=2}D_{KL}(q(x_{t-1}|x_{t},x_{0})||p_{\theta}(x_{t-1}|x_{t}))
-\log p_{\theta}(x_{0}|x_{1})\\
$$
从1.2节[[#1.2 去噪过程]]可知
$$
\begin{split}
p_{\theta}(x_{t-1}|x_{t})=\mathcal{N}\left( x_{t-1};\mu_{\theta}(x_{t},t),\Sigma_{\theta}(x_{t},t) \right)\\
q(x_{t-1}|x_{t})=\mathcal{N}( x_{t-1};\mu_{t}(x_{t},t), \beta_{t}I )\\
\end{split}
$$

经过一些省略的操作最后将损失函数化简为
$$
L_{simple}=||\epsilon-\epsilon_{\theta}(x_{t},t)||^2
$$
# 2 Training and Sampling
![[picture/Pasted image 20240404143558.png]]

训练时: 随机采样加噪步数1-T，前向传播得到$x_t$,将$x_t$,T输入到网络中得到噪音$\epsilon'$,用MSE做损失函数。 

**注意网络预测到的是噪音$\epsilon$**

推断时:随机生成一个正态分布的图片，进行T步循环。 循环体内 预测出噪音后，用t步图片减去噪音，再除去方差得到t-1步图片。  
- Algorithm 2中 $\sigma_{t}z$是在去噪过程中逐步加入噪音，可以增加图片多样性，但是会让生成过程无法收敛。为了保证生成结果可以复现，也可以不加
- 在推断过程中，可以用simple_var策略，即把噪音方差假设为1，则去噪过程简化为$x_{t}-\epsilon_{\theta}(x_{t},t)$

# 3 Comments

为什么余弦的加噪音过程要比线性的加噪音过程效果更好？
我认为直观的解释有两点:
1.  参考cosine positional encoding,余弦噪音可以让模型学习一个潜在的和t相关的噪音预测能力
2. 余弦噪音在每一步上噪音量不同，模型需要对输入的图片的噪音量有所感知，换句话说，避免模型short cut

# 4 DDPM implementation

> To fill the gap between formulas and codes

注意： $x_0$是归一化后的图片,范围在[-1,1]

## 4.1 前向过程
前向过程最终的目标是给定按照给定策略加噪音得到第t步图片的过程。
给定第t-1步的图片，可以得到第t步的图片:

$$
\begin{equation}
\begin{split}

q(x_t|x_{t-1}) &= \mathcal{N}(x_t;\sqrt{1-\beta_t} x_{t-1}, \beta_t I)\\
& = \sqrt{1-\beta_t} x_{t-1}+\beta_{t }\epsilon 
\end{split}
\end{equation}
$$

$\sqrt{ 1-\beta_{t} }x_{t-1}$为均值，$\beta_{t}I$为方差。 

前向过程的输入是图片$x_{0}$,最大前向传播步数:N。按照上式计算$x_{t}$需要进行n次迭代。 但是参考1.1的推导，可以得到将循环优化掉: 

$$
\begin{split}
q(x_t|x_{0}) &= \sqrt{ \overline \alpha_{t} }x_{0} + \sqrt{  (1-\overline\alpha_{t})} \epsilon
\end{split}
$$

因此这个函数可以定义为:
```python
def sample_forward(x_0,t,alpha_bars):
	eps = torch.rand_like(x_0)
	x_t = torch.sqrt(alpha_bars[t]) * x_0 + \
			torch.sqrt(1-alpha_bars) * eps 
	return x_t 
```
其中`alpha_bars`是由采样策略决定的数组，长度为t。 

这个函数是一个torch style的伪代码，为了简洁所以没有用常见的类定义方法。

### 4.1.1 采样策略

采样策略即决定第t步噪音的方差和均值的超参数，不同的采样策略会影响加噪音的最大步数N。 举例两种最简单的采样策略：线性采样和余弦采样 

超参数: 
- min_beta :  2e-2
- max_beta : 1e-4
- time_step : 1000
- strategy: linear
#### 线性采样

```python
betas =torch.linspace(min_beta, max_beta,\
		n_timestep, dtype=torch.float64)
```

#### 余弦采样

```python
timesteps = (torch.arange(n_timestep + 1, dtype=torch.float64) / 
			 n_timestep + cosine_s)
alphas = timesteps / (1 + cosine_s) * np.pi / 2
alphas = torch.cos(alphas).pow(2)
alphas = alphas / alphas[0]
betas = 1 - alphas[1:] / alphas[:-1]
betas = np.clip(betas, a_min=0, a_max=0.999)
```

采样完成`betas`之后，还需要预先计算`alpha_bars`的值备用:
$$
\begin{split}
\alpha_{t} = 1-\beta_{t}\\
\overline \alpha_{t} = \prod_{s=1}^{t} \alpha_{s}
\end{split}
$$
实现为:
```python
alphas = 1- betas
alpha_bars  = alphas.cumprod(dim=0)
#视情况可以给alpha_bars首位插入一个1，对齐下标用
```


## 4.2 后向过程

后向过程的目标是从噪音中进行N步去噪生成一张图片:
由加噪音过程：

$$
x_{t}= \sqrt{1-\beta_t} x_{t-1}+\beta_{t }\epsilon 
$$

得到去噪音过程:

$$
\frac{x_{t} - \beta_{t }\epsilon_{\theta}(x_{t-1},t)}{\sqrt{1-\beta_t} } = x_{t-1}
$$

在实验中，简化噪音方差为1可以减少计算量和提升效果
从而得到:
```python
def sample_backward(self,x,t)
        if t== 0:
            noise = 0
        if simple_var:
            var = self.betas[t]
        else:
            var = self.betas[t] * self.alpha_bars[t] * (1-self.alpha_bars_prev[t])/(1-self.alpha_bars[t-1])

        noise = torch.rand_like(x_t) * torch.sqrt(var)
        eps = net(x_t,t)

        mean = (x_t -(1 - self.alphas[t]) / torch.sqrt(1 - self.alpha_bars[t]) *eps) / torch.sqrt(self.alphas[t])

        x_t_prev = mean + noise
        return x_t_prev
```


# 5 DDIM implementation
DDIM是对DDPM采样进行加速的实现


# MNIST 实验结果
400个epoch batch_size=512 
![[picture/Pasted image 20240502121304.png]]

1200个epoch batch_size=512 
![[picture/Pasted image 20240502154537.png]]



# 参考文献

https://zhuanlan.zhihu.com/p/642006035