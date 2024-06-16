# 1 Introduction
总结一下现在的VideoDiffusion的基本结构，技术路线对比

## 2 Architecture

## 2.x VideoVAE
### Latent Video Diffusion
轻量级的只包含几层3D conv的自编码器，三个方向都采用repeat padding
训练损失函数:

$$
\newcommand{\encoder}{\mathcal{E}}
\newcommand{\decoder}{\mathcal{D}}
\newcommand{\bx}{\mathbf{x}}
\begin{aligned}
\mathcal{L}_{AE} = \min_{\encoder,\decoder}\max_{\psi}\bigl (\mathcal{L}_{rec}(\bx_0, \decoder(\encoder(\bx_0)))  \\+ \mathcal{L}_{adv}(\psi(\decoder(\encoder(\bx_0)))\bigr ).
\end{aligned}

$$
包含1. MSE 2. LPIPS loss 3. adversarial loss 

- [ ] 这个repeat padding 意味着什么
### AlignYourLatents
Encoder是没有做出改变的。 Decoder在解码一个时间上连续的序列(temporally coherent sequence)的时候会有不自然的因素。 所以用一个3D卷积Discriminator对AE的Decoder进行带有时序信息的微调。 

### VideoCrafter
从SD继承了VAE用来压缩图片尺寸。 VAE将每一帧独立的压缩成latent $z$, 又独立重建回图片，没有添加时序信息。 



## 4 Training Strategy

## 4.1 Mixed quality Dataset for Training

## VideoCrafter2

## Stable Video Diffusion


## 5 Implementation


# IDEA
Given that the image quality can be improved through training on high quality image dataset in [[Code Review/Project/VideoCrafter|VideoCrafter]], it's very natural to directly train DPO to improve video quality using Image Preference Dataset using Pick-a-Pic. 


 4.9
- [ ] 上手开始训一个模型
- [ ] 对于大规模的video的模型的训练问题仍然是一个incremental的东西
- [ ] 预训练至少需要100张卡
- [x] Alignyourlatents发知乎

Video和Image差一个纬度T
           如果认为这个T和HW是一样的，那么就不应该有TS和SS的设计。而应该是3Dcov的模式。 
           之前的工作基本认为T和HWC是不一样的，因此有TS和SS的设计。

所以我很好奇一个问题 如果对视频进行permute会有怎么样的结果呢？  We get image of traces！
这个纬度的差异会带来什么样的问题？
从信息的角度来看 FPS越高 帧间变化越小


Vae需不需要对视频这个类型做出调整

首先我们考虑FPS对视频的影响：
模型需要对现实世界的时间有感知，也就是说我生成30帧图片做成一秒的视频和做成2秒的视频是有区别的。

这个问题导致positional embedding或者temporal layer会默认一个fps。

那么考虑一个video latent diffusion model 
Latent code z 属于(B，T，C，H，W)要重建一个视频出来，这个结果是受到vae压缩的影响的。

对T进行下采样或者上采样 对重建效果是有影响的。

VAE是预测图片的分布的，起到压缩图片信息的作用。

如果我们把视频压缩整个latents呢？

Video VAE应该预测视频的分布，压缩整个视频成一整个latets

那么这个视频解码肯定会快
其次自带时序信息 加入fps控制之后可以实现自我插帧？



问题定位实验

首先我们拿出几个videoVAE出来测试

我们采用抽帧和插值的方式在T纬度上进行长视频的变化

那么解码的时候视频预期会有什么样的结果：
他会固定fps然后渲染出对应的视频

是不是还可以解决清晰度的问题？？？


align your latents

可以是一个peft的类型
模型没有改 只是插入了一些层

