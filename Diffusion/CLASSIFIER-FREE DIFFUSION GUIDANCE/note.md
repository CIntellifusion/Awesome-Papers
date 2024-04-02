
2022年谷歌提出**Classifier-Free Guidance方**案，可以规避上述问题，而且可以通过调节引导权重，控制生成图像的逼真性和多样性的平衡，DALL·E 2和Imagen等模型都是以它为基础进行训练和推理

但这两个模型可以用同一个模型表示，**训练时只需要以一定概率将条件置空即可。**

**推理时，最终结果可以由条件生成和无条件生成的线性外推获得，生成效果可以引导系数可以调节，控制生成样本的逼真性和多样性的平衡。**

# 1 Introduction 
Motivation: 训练Classifier会让Difffusion训练更加复杂，希望没有Classifier也可以做Guidance的方法。  混合一个conditional diffusion 的score和一个unconditional diffusion 



## Imagen
Imagen流程如下：

1. 首先，把prompt输入到**frozen text encoder**中，得到text embedding（这个表达已经蕴含了所有文本信息）
2. 把text embedding输入到生成模型中，其实就是给模型信息，让他基于这个信息去生成图像。第一步先成低分辨率的图像，然后再串联2个super-resolution网络，这两个网络的输入是前面的低质量图像和text embedding。最终就可以输出高质量的图像。