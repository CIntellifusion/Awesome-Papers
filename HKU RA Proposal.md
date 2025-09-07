# Multi-Agent Robot World Model 

Top-to-down pipeline:

world model for robtics 有什么好处

world model 做simulator或者做policy是两种方法

world model做simulator的好处:  真机采集数据有陈本和安全问题， 仿真环境有gap，基于规则的物理引擎有局限

Pipeline: 
1. 获取大量的video-action pair。 潜在问题: 获取到合理的action。 
2. 训练world model。 潜在问题： 生成视频和real world的gap。 multi-agent 的world model的结构设计。 
3. 基于world model 去simulate出更多数据。 潜在问题：获取更多合理的action。  合成数据的diversity。 
4. 在生成数据上训练policy model. 这一步暂时没有技术问题
5. 做真机和仿真机的评测。 仿真和真机的gap，world model的数据是否能绕开sim2real的gap 

第一阶段目标： 完成pipeline的前三步，做出一个能生成足够diverse，模拟物理规律的simulator. 实验验证: 对于任意的action, simulator都能模拟和follow。 

技术设计: multi-agent world simulator 



# Survey

## Video World Model for robotics

Robotics在追求的什么东西： 在不同的任务上泛化更好的机器人或者说action model


### Video Prediction Policy:  用video diffusion latents做action prediction的condition


### Unified video action model:  joint video action representation 和 decoupled video action prediction. 

![[Pasted image 20250812131136.png]]

### EgoAgent: A Joint Predictive Agent Model in Egocentric Worlds

![[Pasted image 20250812195806.png]]

![[Pasted image 20250829104124.png]]

![[Pasted image 20250829110954.png]]
### Unified World Model:
左边两个小图： 一个是给o,a 预测o' 是属于environment， 另一个o,o'预测a的逆运动模型。policy是给o测a， video prediction是给o测o' . 用一个统一的diffusion同时做action和video的生成。 
![[Pasted image 20250812131426.png]]


### IRASim: A Fine-Grained World Model for Robot Manipulation

![[Pasted image 20250812200914.png]]

### DreamVLA: 一个具有metaquery结构的VLA model

![[Pasted image 20250812132127.png]]

### 3DFLowAction:  用3D的轨迹信息来帮action prediction

![[Pasted image 20250812133619.png]]

### GWM: Towards Scalable Gaussian World Models for Robotic Manipulation


![[Pasted image 20250812200107.png]]
### HERMES: A Unified Self-Driving World Model for Simultaneous  3D Scene Understanding and Generation

![[Pasted image 20250812200340.png]]

## World Model For Autonomous Driving 

### Pysical Informed Driving World Model
![[Pasted image 20250812201023.png]]

### ReSim: Reliable World Simulation for Autonomous Driving

![[Pasted image 20250813140417.png]]


![[Pasted image 20250813140441.png]]

![[Pasted image 20250813140453.png]]

### Epona

![[Pasted image 20250813140611.png]]
![[Pasted image 20250813140645.png]]

### RoboTron-Sim: Improving Real-World Driving via Simulated Hard-Case


![[Pasted image 20250812201101.png]]


## 3D 4D based World Model 

### GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction

![[Pasted image 20250812195931.png]]

### I2-World: Intra-Inter Tokenization for Efficient Dynamic 4D Scene Forecasting

![[Pasted image 20250812195955.png]]

### InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene  Generation with World-Guided Video Models
![[Pasted image 20250812200700.png]]


### A Recipe for Generating 3D Worlds From a Single Image

![[Pasted image 20250812195349.png]]


![[Pasted image 20250812195325.png]]
## World Model
### HOW FAR IS VIDEO GENERATION FROM WORLD  MODEL: A PHYSICAL LAW PERSPECTIVE

![[Pasted image 20250812200558.png]]


### What Has a Foundation Model Found?  Using Inductive Bias to Probe for World Models
![[Pasted image 20250812193221.png]]
## Summary

Memory的方式： 
1.  2D memory retrival : 本质上是在提升frame condition的质量； context-as-memory, worldmem, framepack. 
2. 3D memory scene + rendering: videospm 
3. 3D representation alignment 


## ICCV 25 world model 总结

robots manipulation和autonomous driving 上的paper最多。 

关于video world model的结论： 有in-domain的良好能力，没有抽象规律的能力，没有out-of-distribution的能力

world model 设计上倾向于video gen 和action planning 同时进行。 

guassian 和voxel是常见的两种3D/4D的表征方式。 


对于一个enviroment system来说他不需要记忆就可以做出推演。 但是对于一个video based world simulator来说，他需要记忆作为全局信息。 

我们能不能有两个agent的world model. 
