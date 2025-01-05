---
Date: 2024-06-16
Title: I2V improvement
dg-publish: false
tags:
---
This should be the script of the paper presentation. 

Today I would like to introduce a paper from THU machine learning group, Identifying and Solving Conditional Image Leakage in Image to  Video Diffusion Models. 

Video Diffusion Models has gained much attention and progress recently. Image-to-Video DIffusion models receive a text prompt and a conditional image as input, and aims to generate videos with good visual quality and natural motions. The paper identify the overlooked issue that these models tend to generate videos with static motion. 

The authors attribute this issue to be Conditional Image leakage which means the model over depend on the condition image to generate videos and ignored the motion infromation from noisy input. 

They identify and validate this image leakage by examine the one-step denoising results at different timesteps. First they predict the noise from an noisy input, and recover X_0.  

Here is an illustration of the experiment. From left to right, represents the timestep t gets larger. The noisy input is gradually perturbed to pure noise, but the conditional image stays the same. As for the recoverd video, at small timesteps, I2V-DM can generate natural motions. But at larger timesteps, it falls. There are less difference between video frames so the video looks more and more static.  

Two conclusion could be draw from this experiment. 
1. 