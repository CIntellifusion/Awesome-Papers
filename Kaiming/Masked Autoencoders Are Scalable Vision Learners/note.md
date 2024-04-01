掩码自编码器

# 1 Introduction 
本文提出了两个核心设计: 非对称的编码解码架构。 一个只编码可见部分，没有masked token的编码器，一个从隐向量重建原图的轻量解码器； 75%的掩码会生成不平凡有意义的掩码。 

作者从自监督学习任务在NLP领域的成功开始思考，如何可以把masked autoencoders的思想引入计算机视觉任务。 他们提出思考：什么因素导致masked autoencoders在NLP和CV领域的不同：
1. **架构问题.** 在视觉领域卷积神经网络天然不适合加入诸如"mask token"和"position embedding" 这样的"indicators",但是ViT架构弥补了这样的缺陷。
2. **信息密度.** 图片的信息密度要低于自然语言的信息密度。
3. **解码器角度.** 图片解码器重建的是像素，文本解码器重建的是单词。 The decoder design plays a key role in determining the semantic level of the learned latent representations.


# 2 Related Work 

1. Masked Language Modeling. Bert:双向掩码  ； GPT: 单项掩码
2. Autoencoding. 此处作者把PCA和k-means也认为是自编码机制。 并且把MAE归为一种新的DAE(Denoising autoencoders)
3. Masked Image Encoding. ViT ; BEiT; 
4. Self-supervised learning. 自监督学习-对比学习




他的方法一页就写完了 剩下做了一堆实验验证有效性。 
