#! https://zhuanlan.zhihu.com/p/703724768
<!-- ---
Date: 2024-06-16
Title: TIFA
dg-publish: true
tags:
  - EvalMetric
  - T2I
--- -->

# 【ICCV23】TIFA: text-to-image faithfulness Evaluation with QA
# 1 Introduction

## 1.1 Problem Statement

文生图模型的文图一致性评价是非常困难的。 图片在什么程度上反应了文本提示词是评测文生图模型的重要指标。 

## 1.2 Stated Contribution

- TIFA比CLIP更精准
- 更加精准
- 更加可解释

# 2 Related Work

## 2.1 Prior Image Generation Evaluation
生成类任务的最终级的指标是满足用户需求。 图片生成任务就是要符合人类观感。 FID和IS指标通过抽取在imagenet上预训练的网络的特征来评价图片质量。 这种指标最根本的问题在于预训练网络究竟好到什么程度。 文图之间的一致性通常通过CLIP及其变种模型，通过比较图片和文本之间的余弦相似度来评价文图一致性。 另一种方法是用图生文再将这个文本和输入的文本进行比较。  SOA和DALL-EVAL通过检测网络来对物体和属性信息进行细粒度的评估。 但是仍然可能漏掉其他一些方面的信息。 

## 2.2 Summary evaluation in NLP 
在QA问题中，大模型会生成一系列关于一个文本的问题，一个QA模型会检查根据问题是否可以得到同一个答案。 这种QA-based的方法和人类指标之间是有高度一致的，这也启发了TIFA这个方法。 


# 3 Method
文本输入T，生成的图片I,对于这个图片我们提出N个问题，每个问题配多个选项，并且得到答案。 记为$\{Q_{i},C_{i},A_{i}\}_{i=1}^N$ 。 所以文本图片的一致程度就被记为回答问题的准确率。 


$$
\text { faithfulness }(T, I)=\frac{1}{N} \sum_{i=1}^N \mathbb{1}\left[A_i^{\mathrm{VQA}}=A_i\right]
$$

> 这个setting是比较合理的，下一个问题就是生成合理的问题和答案。 

## 3.1 Question-Anwser Generation

要全面的衡量图片和文本的一致性，并且解决之前CLIP特征空间不够好的问题，就需要提出多样的，并且有难度的问题。 这里的QA构造用GPT做in-context-learning的方法从文本提示里面生成一系列问题。 首先做实体抓取(element extraction),然后提出几个分类问题。 如下：
- 把文本提示词里面的实体提取出来
- 对实体进行分类:object, activity, animal, food, counting, color, material, spatial, location, shape, attribute, and other
- 条件问题生成，先做二分类，再做多分类
- 用Pormpting的方式生成问题

值得注意的是，这里的QA构造是纯文本模态的，text-in-text-out。 和LLava构造visual instrution tuning的方式一样。 


## 3.2 Question Filtering
用Unified QA验证GPT-3生成的问题。 然后用人工筛选。 

## 3.3 VQA models 

# 4 Experiment

## 4.1 TIFA指标结果和人类偏好一致性程度更高

![Image](https://pic4.zhimg.com/80/v2-5f7ec3e4104d2489654ffe68b724ac5a.png)

## 4.2 Entity 和consistency的关系
实体数量越多，TIFA score越低
![Image](https://pic4.zhimg.com/80/v2-e8dbdd72af70e5c1f53767b3e4cf2032.png)


## 4.3 评测结果

![Image](https://pic4.zhimg.com/80/v2-768fb4466789773a3bf66f2776ecbfa3.png)

# 5 Summary

## 5.1 Relative Position
benchmark，提供了一种新的指标，提出了对CLIP指标问题的解决方案。 

# 6 Comments



