
# Why LLM success?

自回归的建模方式和最大化期望的优化方式统一了NLP领域所有的子任务。 

### Why Diffusion Success?

Diffusion把图片生成

## Why Diffusion Not As successful as LLM


## View of signal decomposition 

BERT GPT 等NLP社区等进步确实是显著的，自监督训练似乎是成功的关键因素，但是CV社区做了这么久的自监督，好像始终没有达到GPT一样的效果。 现在又把目光放到自回归上，用自回归的方式做图片生成。 还有把scaling law作为大模型成功的核心，认为model size足够大就好。 但是即便是视频生成任务，最新的sota的模型大小也不过1.x B，远远不如8B以上的LLM模型。 NLP做的地方在：AR的方式做自回归，并且把模型做的很大，除此之外把所有的NLP任务都统一起来了。 如果我们单独把任何一点拿出来，挪到CV上，可能都不会最终的成功。


一个猜想： 我们可不可以把所有的CV任务都规划成为生成任务。 
这个论文为我们提供了一种可能： 
Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation