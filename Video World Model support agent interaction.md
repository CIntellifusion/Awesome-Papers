https://enigma.inc/blog
## Motivation 
现有world model基本只支持模拟single agent actions. 但是world/environment里面天然有很多agent. 即便是最新的Genie3也只是simulate single actor的行为。 所以我想做一个支持multiple agent同时在这个环境里面活动的video world model. 

# Prelimilaries: World Simulator 
现有的world simulator可以抽象为 p(o'|o,a), 即 predict future states based on current observations and actions. Most exsiting method hypothesis there is only one actor, and simulates directly from the perspective of given actor. 

## Targets

- support more than 2 player 
- actors should be permutation equalvilent 
- environment simulation and actor perspective should disentangle 
- global superior information for environment, but limited information for agents. 

## Data Preparation 
考虑Minecraft为例： 
在一个限定大小的区域内，比如一个竞技场，有N个玩家在活动。 环境应该知道他们的状态位置信息。 玩家可以输出他们的action。 然后环境对于每个时刻输出的所有action做出反馈，生成下一个时刻environment的状态。 然后agents的画面再根据这个状态进行输出。 

感觉trajctory会更简单一点。 

我们需要采集的有： 
For each actor: 
- videos 
- actions sequence 
- poistion and other states 

For environment: 
environment states 

## Method 

Actor Simulator: 

input: 
actor states: {position, action, actor states}
actor observation: partial environment states 

output: actor observation' 

Environment Simulator: 

input: environment states, all actor states ,all actor actions 

output: environment states' ,all actions states,


Pipeline: 

actor -> environment -> actor 


# Result 

video generation model can simulate based on multiple agent actions 

the actors could fight each other or build a house together. 








