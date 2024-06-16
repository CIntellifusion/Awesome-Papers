

# 1 Introduction

## 1.1 Problem Statement

长视频生成
## 1.2 Stated Contribution
无需训练的长视频生成推理技术-对角去噪+Latent partitioning and lookahead denoising 
基于videocrafter2;
无论Unet还是DiT都生效
# 2 Related Work

视频生成模型主要分为Unet和DiT两种架构； 

## 2.1 Long Video Generation
长视频生成主要的技术路线:
1. mask frame 
2. auto regressive 
3. hierarchical approach 


# 3 Method

## 3.1 Diagonal denoising 


![Image](https://pic4.zhimg.com/80/v2-c07a60f19fc1ea83834f3d878a2c6b53.png)
用一个队列维护正在去噪过程中的图片，队列头的图片达到去噪次数的时候出队，同时加入新的噪音。 

> 还没看代码，但是我记得moco也用队列维护了一个memory bank来做这个事情。 

## 3.2 Latent Partitioning 
![Image](https://pic4.zhimg.com/80/v2-a04a96452eb510b8934918c02ffd68ad.png)
去噪音的时候queue里面的带噪音的图片有不同的噪音程度(每一步噪音的方差不同，处于每一步的隐向量的噪音的方差也不同)，而denoiser训练的时候是用相同的噪音的图片训练的。 为了更好的符合这个性质，作者将queue分割为n块，每块是f帧（f是backbone模型支持的大小)，每块的隐向量处于同一个时间步 ，用分治思想进行去噪。 



从算法上比较得来的就是: 每次仍然去噪f帧，只是先进先出的帧数变成的f，每次去噪的f帧都是同时入队，同时出队的。  
这样也可以提高推理的效率。 

## 3.3 Lookahead Denoising 
![Image](https://pic4.zhimg.com/80/v2-0fa493913abf6017be5cfd0dffb0ac39.png)25.png
去噪的时候用没有噪音的图片提供参考。 

这样的策略在[[Diffusion/Video Diffusion/DynamiCrafter|DynamiCrafter]]等系列中都有用到，只是这里FIFO的过程中反复用到了不同的帧作为干净的图片参考。 



# 4 Experiment
视频效果建议参考project page: 确实做的不错 [FIFO-Diffusion (jjihwan.github.io)](https://jjihwan.github.io/projects/FIFO-Diffusion)

## 4.1 Implementation Details  
核心代码就在这里，对DDIM的一些改进

![Image](https://pic4.zhimg.com/80/v2-b0fbe9fff3f59e04d51c9d7f7d51e1f3.png)
[FIFO-Diffusion_public/scripts/evaluation/funcs.py at main · jjihwan/FIFO-Diffusion_public (github.com)](https://github.com/jjihwan/FIFO-Diffusion_public/blob/main/scripts/evaluation/funcs.py#L158)
# 5 Summary
方法简单，效果显著

# 6 Comments

