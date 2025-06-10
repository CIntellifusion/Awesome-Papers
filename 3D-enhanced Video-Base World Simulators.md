# Paper CheckList 
- 一边写paper 计划结构
- 一边做实验 
- 怎么样讲故事-把他和实验和方法联系起来，让他们是一致的

- task: video generation (long video generation)
- key observation: 3d consistency improves videos generation consistency 
- world simulator has two aspects: physical law following and 3D consistency

- 3D clouds as **memory** for long video generation 
- aling 3D reconstruction **representation** with 2D generative models 

which is better story: 
- 3D and Video are  of same importance to world simulation 
- adding 3D to video 
synllable marco list: 
{Video-Based World Simulators}

故事从结合video和3D来做world simulator出发，是不是就是另外一个故事了。 
算了先按照一个初稿写出来就行。 

# Introduction (suggested 500 worlds , 3/4 page)
- p1: task, the significance of the task
- p2: limiations, the causes of limiatation 
- p3: solution, how to solve 
- p4: detail method description 
- p5: what do we do 
- p6: solution 

(初稿没看worldmem写的，但是感觉思路非常像，不能和他那么像)
World Simulator aims to model the internal principle of the real world, in other words, predict what the future looks like given the current state. Recent advancement in video generation models has proven video to be an practical (介质）to modeling the world thanks to large scale accisible videos.  However, the data-driven generative models has the nature of inaccurate  3D consitency.  On the other hands, representing real world with 3D sence and dynamics is more effictive way[add ref, worldscore的cite里面找找] but lacks sufficient data to scale up. Thus we propose the combine the two way to get a better world simulator.   

Video Generation Model faces severe 3D inconsistency issues especially in long video generation. The key reason is video generation model often has short context window (8 frames 16 frames) during training.  This issue is more severe when doing downstream tasks like navigation, ego videos when spatial understanding is necessary.  Many methods has been proposed to design different memory mechanism for video generations. Our key insights is we could compress history frames of variable length to a compressed fixed length pointcloud(explicit) or 3D representations(implicitly)

> we argue that the 3D information and diffusion model focus on current informationi and future informatin respectively and cooperates well. 

In this paper, we aims to address the 3D inconsistency caused by accumalation error in long video generation tasks in existing models. We mainly focus on the videos that has obvious camera movement that requires the understaning ability and memory capcabiliyt of spaital scenes.  Our key insights is by leveraging existing powerful and unifed 3D reconstruction models, we could store the video history in 3D latent features, which could be called 3D as memory of video generation. Our extensive experiments shows that 3D information is a good format of storing the spatial memory for video generation thus making it a better world simulator. 

These video generative models has proven helpful in many downstream tasks like automous driving, vision-langague-action models(VPP) and navigation tasks, game generation. 

# Related Work 

- video generation 
	- video foundation models: videocrafter/svd/hunyuan/wan/seedweed/
	- diffusion forcing / diffusion forcing transformer /ar-diffusion 
	- maskflow. mamba cosmos 
	- video accleartion for world modeling: diagd 
	- video post training: videodpo/video-rl/
- world simulator (w/ w/o action)
	- mineworld / kunlun / worldmem / spmem 
	- cosmos 
- 3d Representation 
	- vggt
	- duster
	- MegaSam 


## 2.1 World Simulators 

video-based world simulators.  Sora/Cosmos/xxx uses the 

3D-based world simulators. Viewcrafter, wonder journy , wonder world.. could recon a closure scene and allow navigation in some degree. 

worldscore and other benchmarks.  Decoposes the key features in world generation.  4d-fy 

## 2.1 Memory Mecanism in Video-Based World Simulators 

如果我要用vggt，那么memory这个section就不是那么重要了。 

Video-Based open-ended world models are enhanced by memory mechanism in different ways:  frame-level context(diffusion forcing transfomrer; maskflow, long-context mamba) , explicit 3D representations( worldmem). The basic ideas here is compress (冗余) video context in a more contigous format. 

Context Guidance. History-Guidance Diffusion Forcing transformer apply a dynamic noise on subset of context frames to enhance long-term consistency. WorldMem propose the maintain a memory bank and retrieve history frames according to FOV overlap ratio.  

[World Models with Long-term Spatial Memory] / wan+controlnet 
world consiste 6D diffusion 

Point Cloud Rendering: by extract pointcloud and rerender to image space, these method could handle xx. 
# Method 
现在的方法主要分为两节: 3D-repa 和 3D-controlnet 。 3D-repa是用来解决误差和累积误差的，3D-controlnet是用来增加conherence的，memory机制。 

- [ ] 之前对VGGT feature的analysis可以拿出来放在附录里面，论证我们用这个feature的合理性
- [ ] diffusion feature align 之后 能不能得到点云 可视化出来看看
- [x] 备份repa-loss的checkpoint和训练记录
- [ ] 重新infer video，等着测新的benchmark，现在log的video是gif格式的，而且有后处理。 
- [ ] 更多的benchmark的结果测出来

## 3.1 3D REPA for Video Generation 

> 写这种文章 一般不要把具体用了什么模型放在前面

3D-aware representation. The VGGT provide robust latent features and pointcloud. 

%% 
Why the 3D representation and semantics representation shares same place for generative tasks? Videos can be viewed as a projection on 2D planes with time axis. So the 3D feature is born with videos, in other words, a 先验 of videos. The 3D recon information reveals the connection between 3D space and 2D RGB space. The semantics representation of models like mae,dino, dinov2, can be also viewed as a mapping between language space and 2D RGB space. So the similiarity is clear here, the 3D recon information is another form of undertanding feature of imaes/ videos. 
%%

Insipred by repa/repa-e who shows the semantic representation of images can be helpful to generation, we argue that the 3D information can be helpful for video geneartion. Language semantic representations—such as those learned by MAE, DINO, and DINOv2—have been shown to significantly benefit image generation tasks. These representations act as high-level priors that bridge the gap between visual appearance and abstract concepts.

Interestingly, 3D representations share a similar role. Videos can be viewed as 2D projections over time, but they inherently encode 3D structural information. This makes 3D understanding a natural and strong prior for video data. Moreover, 3D reconstruction features establish a mapping between the physical 3D space and its 2D visual observations, much like how semantic features map between language and 2D images.

Given this similarity, we argue that 3D representations serve as another form of visual understanding—parallel to semantic representations—and are especially suited for video generation. Therefore, aligning video generation with 3D priors could be an effective way to enhance the spatial-temporal coherence and structural realism of generated content.

%% how to perform this alignment  %%

We denote the feature in diffusion transformer block to be xxx, and the videos to be xx, and representation model is xxxx. We use a projector to align the feature map. 

公式的初版先放在这里了，目前有半页左右，有点太长了。 

https://www.overleaf.com/project/68414cbbd41fce74388c8afc

> Comments: 这一段论点是 video generation can be benefit from 3D representation. 
> 但是还没有推到 3D repesentation can benefit long video generation. 
> Long video generation 的效果要怎么被改进呢？ 就是通过context compression by VGGT. 

> 3D rperesentation explicitly (view crafter etcs) implicitly (xx) added to model has been proven to be work. However, the reperesentation alignment yield another brand new method in adding 3D to video generation. 

## 3.2 3D Memory  Compressioner for Long Video Generation

Only align with generation model with 3D feature can result in better video generation result. But our utilmate goal is using 3D feature to generate longer video. The role  of 3D rerepesntation is different here.  The 3D feature in the last section focus on how the 3D feature benefit on current generation. This section, it serves as history compressioner. 

Training stage, we uses context frames.  second step: finetune on re10k with vggt condition
Inference: inital vggt latents is got by initial condition frames. We generate the keyframes of a long video, then interpolate between key frames. The VGGT feature will be updated each time we got new clean frames. The nature of pointcloud makes sure that the condition length is the same with variable length as long as the scene is not exteneded. 



# 4 Experiments

## 4.1 Experiment setup 

- dataset(from high priority to low): re10k, mc , kinetics 

Video Quality Metircs: 
- fvd lipips psnr (prior)
- vbench subdimensions 
- aesthtic (optional)

3D consistency evalution metrics:
- vggt score: given by the liklyhood that the images are sampled from same scene. 
- world score 3D consitency: follow the worldscore's 3D consitency evaluation. 
- Turning around consistency and moving around consitency, inspried from worldmem and extended from it. both 公转和自转我们都考虑了。 

Test Dataset: 
1. re10k 100 video x 256 frame 
2. minecraft(optional since vggt may not work)
3. automous driving dataset(if 2 is )
## 4.2 main results 

baseline: 
- full sequence diffusion 
- diffusion forcing
- ar-diffusion(maybe)
- worldmem
- maskflow(sb文章 复现了那么久 还是可以测测) 在re10k上train一版本就行。 

## 4.3 Ablation Study

Ablation Study Table 1.
- train from scratch w/o VGGT repa 
- train from scrach w/ VGGT repa
- finetune with VGGT repa on setting 1 checkpoints

> 这一步做完之后取最好的checkpoint

Ablation Table 2. 
- w/ controlnet vggt single frame 
- w/ controlnet vggt multi frame(2,3,4 or more) 
- w/o controlnet vggt  


> 如果时间充足可以消融 table1里面的checkpoint哪个效果更好

Analysis Experiment 1. 
Train on context length 8 ;
train on context 16 
train on context 32

with inference setting : 
8 frames/ 32 frames/ 128 frame/ 256 frame

Human Preferece Table. on long video generation 
worldmem
ours best

## 4.2 Qualitative Results 

- visual result comparison on re10k 
- visual result anaylsis on ood data with re10k (follow dfot)

# 5 Analysis on 3D condition for World Model 

The 3D context compressioner may suffer qualit gap when the video domain is different, Here we provide a ananlysi on this. We summary the following situation:  
1. when the scene is fixed but camera move largely. The 3D information will serve a exceelent history compressioner. Eg, walking in an offiice, 
2. When the scene and camera moves largely at the same time. The 3D inforamtion may help less since 3D only work for recon the current result, while the diffusion model is repsonsible for predict the unseen area. Eg. Navigating in a large house(the most common case in re10k). In this situation, the result can be improved by giving more condition frames with different view at some degree. 
3. When the scene is and camera fixed, the 3D information is useless since no spatial challenge for world model. Eg. a video recording a man is talking. 

(this could also serves limiations of this paper.)


## 5.1 Disccusion

## What should world simulator model ?

What we model is the most important question for most mathematical problems. 

As one of the motivation of this paper, which is unify the 3D and video modeling for better world simulator, whether to model 3D representation(mesh,trillius) or videos  is sill an open question. (太繁复了，直接讨论吧)

Video Data is easy to accisible and 
While 3D has what feature xx. 

At this view, the unify of 3D and video is most promising way. While we may propose that 3D mainly to imporve static  accuracy and correct acuumluation eroor and video-prediction model is more sutibale for predict future states. 


# Reference


# Appendix 
