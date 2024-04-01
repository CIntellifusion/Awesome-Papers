

拨云见雾-做物理的人想问题和做计算机的人想问题有什么不一样 

irradiance:辐照度
attenuated:衰减的

# 1    问题陈述
烟雾等大气现象直接导致相机接收到景点反射光的辐照度衰减，在图片上呈现出低对比和颜色失真问题。 
去雾因此成为了重要研究课题。 

有句话没看懂,这里提到的假设是什么意思：
> from low-level image analysis to high-level object recognition, usually assume that the input image is scene radiance. 

去雾后的图片可以提供深度信息，但是去雾前的图片缺乏深度信息。 多张图片的去雾工作，例如基于极化的方法取得了不错的进展。 在单张图片去雾方法上，作者举了两个工作。 一个假设正常图片比含雾的图片有更高对比度，因此采用了最大化图像局部对比度的方法。 另一个假设透光和表面遮光是局部不相关的。 

这两个假设的共同缺陷是太强了因而不能符合所有情况。 所以作者提出了Dark Channel Prior。 从统计数据中发现dark pixels至少在rgb中的一个通道是非常低的强度。 而这通常是由空气中的光引起的(airlight)。 因此可以从dark pixels中建立haze's transmission的估计。 最后结合haze imaging model和soft matting interpolation method进行图片去雾和深度图估计。 


# 2     实现方法
### 2.1    Dark Channel Prior 
定义暗通道为一个像素及其附近邻域像素值最小的通道。 
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240329193908.png]]
暗通道的先验是指:一个图片如果不包含雾霾，那么暗通道值应该接近于0
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240329194148.png]]

#### 2.1.1    暗通道先验 补充

| 颜色 | RGB         | 特点                       |
| ---- | ----------- | -------------------------- |
| 灰色 | 180 180 180 | 典型雾霾颜色               |
| 红色 | 255 0 0     | 双通道为0 饱和度最高的红色 |
| 紫色 | 128 0 128   | 纯紫色 单通道为0 纯紫色    |
| 绿色 | 0 128 0     | 双通道为0 纯绿色           |
考虑一个三维空间，坐标轴分别是R,G,B的值，将空间中每个点标记为RGB值，那么在这个正方体中心是纯灰色。 正方体面上的点都是存在暗通道的点。 


这一节的写作逻辑是：首先发现Dark Channel Prior，然后通过实验证明这个先验的有效性。 既给出了统计检验结果又给出了可视化结果。 

### 2.2    使用暗通道先验去雾

#### 2.2.1 Transmission estimation 
这个先验的使用方法带有非常强烈的物理学特征。 我们首先将图片分为天空和非天空两个区域。在非天空的区域：
假设在图片中，transmission是恒定的，环境光A是已知的。 设transmission为t(x)
一张带有噪音的图片记为
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111059.png]]
然后在I(x)上每个通道的x的邻域上进行最小化操作，

![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111231.png]]
此处需要带入我们之前的暗通道先验为0 
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111259.png]]
所以还需要在（6）式子中取每个channel的最小值
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111415.png]]
然后可以带入暗通道为0得到
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111448.png]]

在天空区域，天空的颜色接近于环境光A，而且几乎不反射，从而有![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111621.png]]

因此公式11同时满足天空和非天空区域。 

最后由于haze对人眼深度估计具有重要作用，并且天空不是完全纯净的，所以加入一个超参数控制去除的haze的比例
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/Pasted image 20240401111749.png]]
作为我们最后的transmission map


#### 2.2.2 Soft Matting
![[Kaiming/Single Image Haze Removal Using Dark Channel Prior/picture/19114d326a41a7a2b86671dda68fe38.png]]
> attention is all you need

看不懂 好难 


