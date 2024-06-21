---
Date: 2024-04-02
Title: Home
dg-publish: true
dg-home: true
---

# Readme
Intensive reading of papers. Let's start with works of Kaiming! Other interesting and new papers will also be updated. 

1. reading gains insights. 
2. broad reading gains ideas. 
3. Learn to research.
4. Learn to enjoy research. 
5. first stage : 100 papers before august
6. presenting papers using English 



[Diffusion implementation accompanied by this blog](https://github.com/CIntellifusion/SimpleDiffusion)
# Paper Review Overview

## Paper queue 
## version 1 多模态和视觉大模型
- [ ] CapsFusion: rethink data at scale 
- [ ] Flamingo 最早的多模态大模型之一
- [ ] image speaks image 
- [ ] seg gpt 
- [ ] Emu 1 emu2 视觉上下文学习
数据 编码器和预训练是三个最重要的问题。 

编码的不可能三角:紧凑，离散，无损

关于CLIP的问题: 
- [ ] saining xie 的CVPR24工作
- [ ] visual search 
- [ ] Virl 开源的真实世界评测

自回归的生成模型
- [ ] VAR / AR beat diffusion 
- [ ] VQGAN 
- [ ] parti  deepmind 最早scale up 的工作

一般的图片生成模型的探索:
- [ ] photo maker
- [ ] story diffusion 

Diffusion理论
- [ ] DPM-solver
- [ ] RQ-VAE
- [ ] Score-based models 
- [ ] Consistency models 
- [ ] multi-step consistency models 

古老师最近的关于理论的一些工作:关于视觉工作的本质目标
谢赛宁老师关于CLIP表征缺陷的一些探索。 

## version 0 视频生成
- [ ] [[Kaiming/Single Image Haze Removal Using Dark Channel Prior|Single Image Hazing （bit hard for me)]]
- [ ] [[Kaiming/Moco|Moco]]
- [ ] [[RepresentationLearning/Efficient SAM|EfficientSAM]]
- [ ] ScoreBased model 
- [ ] TextDiffuser 1-2 
- [ ] StyleGAN 2 很久之前看的了； DiffusionAE也引用了这个
- [x] [[GenerativeModels/VAR 自回归图片生成|VAR 自回归图片生成]]
- [ ] PYoCo
- [ ] ATE-DM
- [ ] StreamingT2I 
- [ ] ICML23 Consitency Models
- [x] [[Diffusion/Video Diffusion/FIFO-DIffusion无需训练的长视频生成|FIFO-DIffusion无需训练的长视频生成]]
- [ ] llama3 review 
- [x] [[Diffusion/Video Diffusion/VDT GENERAL-PURPOSE VIDEO DIFFUSION TRANSFORMERS VIA MASK MODELING|VDT GENERAL-PURPOSE VIDEO DIFFUSION TRANSFORMERS VIA MASK MODELING]]
- [x] [[RepresentationLearning/CLIP|CLIP]]
- [x] [[Diffusion/Video Diffusion/Vbench|vbench]]
- [x] [[Diffusion/Video Diffusion/Make-Your-Video|Make Your video]] 
- [x] [[Diffusion/Video Diffusion/Follow Your Click|Follow Your Click]]
- [x] [[Diffusion/Video Diffusion/Follow Your Pose|Follow Your Pose]]
- [x] [[Diffusion/Video Diffusion/MagicTime|MagicTime]]
- [x] [[Diffusion/Video Diffusion/DynamiCrafter|DynamiCrafter]]
- [x] [[Diffusion/Video Diffusion/Latte|Latte]]
- [x] [[Diffusion/Video Diffusion/ControlVideo|ControlVideo]]
- [x] [[Diffusion/Video Diffusion/EvalCrafter|EvalCrafter]]
- [x] [[Kaiming/MAE|MAE]]
- [x] [[Diffusion/Classifier-free Diffusion Guidance|Classifier Free Guidance]]
- [x] [[Diffusion/DiffusionRL/Diffusion-DPO|Diffusion DPO]] 
- [x] [[Diffusion/Video Diffusion/Latent Video Diffusion|Latent Video Diffusion]]
- [x] [[Diffusion/Unconditional Diffusion|Unconditional Diffusion (First Part Done)]]
- [x] [[Diffusion/Video Diffusion/VideoCrafter|VideoCrafter]]
- [x] [[Diffusion/Video Diffusion/Stable Video Diffusion|Stable Video Diffusion]]
- [x] [[Diffusion/Video Diffusion/AlignYourLatents|AlignYourLatents]]
- [x] [[PEFT/Lora|Lora]]

## Paper Summary 

| paper                  | year   | field and direction                          | key design                                                            | contribution                                                                                         |
| ---------------------- | ------ | -------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| MAE                    |        | Mask Image Modeling, Vision Pretraining      | decoder smaller than encoder; 75% mask ratio                          |                                                                                                      |
| Lora                   |        | PEFT                                         | Lora layer to reduce fine-tuning resources                            | notice the low rank intrinsic of large models.                                                       |
| ClassifierFreeGuidance |        | text2image,diffusion                         | Setting condition to None following a distribution                    | Training conditional text2image model without classifier.                                            |
| Diffusion-DPO          | 2023   | text2image,diffusion,dpo                     | DPO-loss to replace a trained reward model                            | align human preference with Diffusion models.                                                        |
| LVDM                   | 2022   | text2video,diffusion, pretrained model       | Video VAE; Hierarchical Latent Generation ；                           | generate short and long video at a low consumption                                                   |
| Stable Video Diffusion | 2023   | text2video,diffusion ,pretrained model       | No significant declaration.                                           | Dataset curation analysis and processing pipeline； HQ Image pretrain;  Lora for camera motion video. |
| AlignYourLatents       | 2023   | text2video,diffusion, text2image,finetuning  | Insert Temporal Layers；                                               | Adapting text2image model to text2video                                                              |
| ControlVideo           | 2023   | text2image,diffusion,text2image,finetuning   | Cross frame attention; interleaved smoother; hierarchical generation; | Training free method.                                                                                |
| EvalCrafter            | 2023   | text2video, evaluation metrics               | analysis of video dataset composition.                                | Comprehensive evaluation metric for text2video generation                                            |
| Latte                  | 2024   | text2video,diffusion,transformer             | Transformer with Temporal and Spatial Attention                       | Using Transformer to replace Unet in Diffusion models                                                |
| VideoCrafter1          | 2024   | text2video,diffusion, pretraining            |                                                                       |                                                                                                      |
| VideoCrafter2          | 2024   | text2video,diffusion, training strategy      | Training Strategy of Image pretraining                                | analysis of parameter perturbation                                                                   |
| DynamiCrafter          | 2024   | text2video,diffusion, prior conditioning     | Open-domain Image Animation                                           | add clip image ViT feature as additional control                                                     |
| MagicTime              | 2024   | text2video,diffusion，prior conditioning      | a dataset  that contain phsical process videos.                       | physical process videos for lora adapting.                                                           |
| MakeYourVideo          | 2024   | text2video , diffusion, prior conditioning   | adding depth as control                                               | similar to dynamic crafter                                                                           |
| Follow Your Pose       | 2024   | text2video , diffusion, prior conditioning   | adding keypoints as control                                           | generating pose-controllable videos                                                                  |
| Follow Your Click      | 2024   | text2video , diffusion, prior conditioning   | click and motion prompt                                               | in fact this not a drag. Optical flow is good idea.                                                  |
| VDT                    | ICLR24 | text2video, DiT                              | diffusion transformer; mask modeling                                  |                                                                                                      |
| DiffusionAE            | CVPR22 | Diffusion; AutoEncoder; Latent represetation |                                                                       |                                                                                                      |
| VAR                    |        | AR; image generation                         |                                                                       |                                                                                                      |
| DiffMorpher            | CVPR24 | Diffusion; Image interpolation;              |                                                                       |                                                                                                      |
| StyleGAN2              |        | GAN;Image;                                   |                                                                       | AdaIn                                                                                                |
| HRA                    | 2024   | adapter-based finetune                       |                                                                       | HRA for finetune which can be better than lora                                                       |
| OFT                    |        | adapter-based finetune;                      |                                                                       |                                                                                                      |
| T2Vscore               | CVPR24 | diffusion Benchmark                          |                                                                       |                                                                                                      |
| FIFO-diffusion         |        | video generation; training-free;             |                                                                       |                                                                                                      |
| DreamBooth             | CVPR23 | image generation; few-shot                   |                                                                       | prior-loss;                                                                                          |





# Implementation analysis
- [ ] Vision Transformer
- [x] Diffusion-Unet-Attention-Resnet-convnet
- [ ] StyleGAN
- [x] VideoCrafter and LVDM 
- [x] VAEs
- [ ] DIffusion Transformer 

# Blog Design
- [ ] Add tags : Diffusion Contrastive Learning etc. 
- 外链必须要存在才可以加入 否则会报错 
- svg图片
# Practical Advise

## Tips for Review Papers 
- All sections need to be read.  所有的部分都值得去读
- Read critically. 辩证的阅读， 慢慢学会评价
- write summary. 每篇文章小总结，关键的想法和关键的做法。 几篇类似的文章总结在一起
- 技术报告和实验分析会是很有用的部分，可以指导自己设计合理和有效的实验 
- 这个博客不是为了更新而更新，需要保证更新的质量

在进行科研文献阅读时，为了深入理解和评估每篇论文的价值和意义，可以采用以下问题框架来引导自己的思考：

1. **文献领域定位**：
   - 首先确定文章所属的研究领域或具体方向。这有助于你将论文放置在正确的知识背景中，并理解其在整个研究领域中的位置。
   - 越底层的东西越有可能产生Impact。 至少可以把论文分成application和strategy两种。 一个新的论文可以是application和strategy的新组合。 Video Generation是一个Topic或者task，diffusion是方法。 Dance是应用。 


2. **问题重要性分析**：
   - 识别并理解文章解决的具体问题，以及这个问题为何重要。这通常涉及到问题的现实意义、对现有研究的影响，以及它可能带来的理论和实践上的改进。
   - 找到正确而有意义的问题是做好科研的第一步

3. **方法和模型评估**：
   - 分析文章所采用的方法和模型，并思考这些方法为何能够有效解决问题。这包括对方法的理论基础、创新点、以及与现有方法的比较分析。

4. **核心结论提炼**：
   - 总结文章的核心结论，这通常是作者通过研究得出的主要发现或观点。理解这些结论对于把握论文的精髓至关重要。

5. **未来研究方向探索**：
   - 思考论文可能的延伸和未来的研究方向。这可能包括对当前研究的局限性的讨论、潜在的改进空间，以及新的问题和挑战。

通过上述问题框架，你可以系统地分析和评估每篇论文，不仅能够加深对文献的理解，还能够激发自己的思考，为未来的研究工作提供方向和灵感。这种方法论有助于你在科研领域中快速成长，形成批判性思维和独立研究的能力。

1. **文献阅读优先级**：
   - 首先阅读近一至两年的文献综述，以获得领域概览。
   - 其次，研读近五年内的经典和高引用文章。
   - 重点关注近两年的顶级会议中带有开源代码的研究成果。
   - 最后，阅读无开源代码但重要的顶级会议论文。

2. **结合代码学习**：
   - 对于重要论文，边阅读边学习其源代码，将motivation-idea-implementation联合起来。 

3. **记录与反思**：
   - 记录论文的核心要点和潜在的研究方向。
   - 反思论文的缺陷和改进空间。

4. **与导师沟通**：
   - 在有充分理由和文献支持的情况下，与导师讨论研究方向的调整。

5. **实践参与**：
   - 主动参与师兄师姐的科研项目，以获得实际操作经验。

6. **跨领域探索**：
   - 阅读相关领域的文献，以获得新的研究灵感。
   - Related Work和Literature Review的重要性。 如果对2-3个领域有足够好的感觉，将他们结合起来，就可以组成非常好的工作。 

通过这些方法，你可以更高效地吸收知识，提升研究能力，并为未来的科研工作打下坚实的基础。

## Tips for Presentation

currently only for presentation of papers. 
- High level idea or motivation is more important. 
- Ready to be challenged, those may rise interesting topics 
- Be organized for you language 
- More fluently 