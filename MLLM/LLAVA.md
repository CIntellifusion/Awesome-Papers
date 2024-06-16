#! https://zhuanlan.zhihu.com/p/703020355
# LLava : visual instruction finetuning
LLaVA: Large Language and Vision Assistant 
# 1 Introduction
## 1.1 Problem Statement
Instruction tuning的在大模型领域用了很多了，但是在多模态领域还没有。 

## 1.2 Stated Contribution

用GPT-4生成的多模态指令数据来训练一般的视觉和语言理解的多模态大模型。 

传统的视觉任务诸如分类检测分割和描述都被语言增强的视觉基础模型得到更好的解决。 

- 提出了多模态指令数据的流程
- 用LMM+CLIP encoder+Vicuna Decoder组成一个多模态大模型。 然后用生成的数据进行端到端的微调。 
- LLava-Bench高质量的多模态指令基准

# 2 Related Work

## 2.1 Multimodal Instruction-following agents

在计算机视觉领域指令-服从的agent可以被分为两类: 一类是不同领域具体的端到端训练的模型。 具身智能里面根据自然语言做出行动的机器人和图片编辑领域里面根据提示词修改图片的模型。 另一类是将视觉模型集成到多个模型中，形成一个工具链。 这个工作的目标是端到端的训练语言-视觉多模态模型以胜任多种任务。 

## 2.2 Instruction Tuning 

LLM领域已经广泛的使用指令数据集来训练模型提升完成真实世界任务的能力。 指令微调可以简单高效的提升zero-shot和few-shot能力。 Flamingo在视觉领域可以被视为是GPT-3一样的模型，因为他有很强的zero-shot，迁移学习和in-context learning的能力。 

基于Llama的多模态大模型诸如OpenFlamingo,Llama-adapter等模型是没有显式的进行过多模态数据的微调的。  所以这就是这篇文章关注的research gap. 


# 3 Method

## 3.1 GPT-assisted Visual Instruction Data 

instruction-following data可以表示为(image,quesiont,anwser)的模型。 作者通过GPT在文本-图片对数据集COCO/LAION上构造了question和anwser，然后再匹配上图片，形成了多模态的指令数据集。 
用GPT-4和chatgpt作为teacher引导视觉内容的生成。 图片通过描述词和检测框符号化。 
指令数据包括三类任务:
- 对话。 用户向模型提出相关图片的问题来解答。 
- 详细描述。 对图片细节进行详细的描述。 
- 复杂推理。 构造带有逻辑困难的多步的问题

## 3.2 Visual Instruction Tuning 

作者用Vicuna负责语言模型，用CLIP ViT-L/14作为视频信息提取器。 用线性层对齐图片空间和文本空间。 Q-former(Crafter系列里面也有用来连接)，CrossAttention等机制来连接这个空间可以有更加详细的探索。 

### 3.2.1 Training

基于多轮对话和原始AR训练目标进行训练。 

1. 第一步：在一个小数据集（600k）的文本图片对生成的单轮问答上冻住CLIP和Vacuna只训练图像和文本空间的连接模型。 
2. 全量微调全数据微调 


# 4 Experiment


## 4.1 Multimodal chatbot 
80k unique image得到的多模态数据集训练出来的LLava和GPT-4有类似效果。 
BLIP-2 and OpenFlamingo对图片敏感，但是对指令不敏感。

## 4.2 Llava Bench 

作者提供了COCO和In-the-wild两个benchmark set 来测试模型能力，分别包括90和60个问题。 在这两个设置上都展示出visual instruction tuning给多模态大模型带来的良好的增益。 

从Llama Bench里面可以分析出来LLama的一个弱点是不能准确的抓住复杂的语义信息和缺乏足够的知识。 不能抓住复杂的图片语义信息部分来自于CLIP处理图片的时候的patch化操作，让模型把图片分割成多个Patch。 

## 4.3 Scientific QA 

Scientific QA 包含21k多模态的多选择，作者在这里对比了CoT和multimodal CoT的方法，结果显示Llava能够超过大多数baseline的模型。 

# 5 Summary

用新的多模态指令数据构造流程构造了新的数据集，并且训练了一个能够解决多种任务的多模态大模型，在ScienficQA和其他任务上超过了现有的多模态大模型。 

# 6 Comments

very insightful work 

