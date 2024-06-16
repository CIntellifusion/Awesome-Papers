# Summary
The author use dual VAE structure to decouple upper face and lower face and learn two emotional latent feature space separately. Then a latent diffusion model is trained to generate blendshape of talking head. The authors creatively  apply a discriminator on the latent space for better motion generation quality. Moreover, the author capture a 3D-BEF datasets to enrich the variety of facial expressions.   

# Strengths
- The author successfully identify the research gap in audio-to-face task to be “scarcity of emotionally varied, high-quality datasets and the complex task of capturing subtle emotional nuances accurately”.
- The author creatively train a latent diffusion model on the facial motion latent space with a discriminator to enhance generation ability. 
- The author propose a new dataset named 3D-BEF for emotional audio-to-face task.  



# Limitations
- the lines in overviews in not clear and confusing while the modules painted fail to illustrate the most important innovation of this work. 
- section 3.1 the input of VAE is not described. The encoder encodes the input sequence in a frame-by-frame manner, how can it learn inter-frame features. The q,k,v of cross-attention in decoder is also not mentioned.  So the quality of latent space z seems completely not guaranteed. 
- Section 3.2 no explanation about the added discriminator.  Section 3.2 and section 3.3 seems duplicated and not organised well.  The contributions and motivations almost not described at all but full of preliminaries. 
- The essay is not carefully written. It 4.1 and 3.1 should both be section or subsection regarding to line 557 and line 322.
- Lack of experiments on other datasets (3D-ETF). The dataset proposed by the author is lack of description and analysis. With the result in supp., I doubt the model overfits on the 3D-BEF.  


如果上面的太多 下面的就不交了吧
- the author state the research gap as scarcity of emotionally varied, high-quality datasets and the complex task of capturing subtle emotional nuances accurately at the beginning. But they did not mention a single word to solve this gap after introduction. 


# Rate
reject. 
The author pretend to do research.  Despite the obvious typo in essay, the content is avoid talking about their work but borrowing sentences and formulas from previous work. 


# Confidence
confident 




# A proposal to apply DM on Audio-to-Face 
> This part is written for reference. 
> This section is not meant to be submitted to CMT.


- talking head generation可以被做成一个视频生成的任务 ； 因为两个任务都是时序的生成。 
- 我们都用diffusion了 输入直接用处理过的原视频，然后把抓到的blendshape系数配合文字提示(就是替换下图中的CLIP image encoder) 最后生成一个白模也可 生成photo realistic也可

![[picture/Pasted image 20240429111632.png]]