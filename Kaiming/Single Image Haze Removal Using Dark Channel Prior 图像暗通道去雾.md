

拨云见雾-做物理的人想问题和做计算机的人想问题有什么不一样 

irradiance:辐照度
attenuated:衰减的

# 问题陈述
烟雾等大气现象直接导致相机接收到景点反射光的辐照度衰减，在图片上呈现出低对比和颜色失真问题。 
去雾因此成为了重要研究课题。 

有句话没看懂,这里提到的假设是什么意思：
> from low-level image analysis to high-level object recognition, usually assume that the input image is scene radiance. 

去雾后的图片可以提供深度信息，但是去雾前的图片缺乏深度信息。 多张图片的去雾工作，例如基于极化的方法取得了不错的进展。 在单张图片去雾方法上，作者举了两个工作。 一个假设正常图片比含雾的图片有更高对比度，因此采用了最大化图像局部对比度的方法。 另一个假设透光和表面遮光是局部不相关的。 

这两个假设的共同缺陷是太强了因而不能符合所有情况。 所以作者提出了Dark Channel Prior。 从统计数据中发现dark pixels至少在rgb中的一个通道是非常低的强度。 而这通常是由空气中的光引起的(airlight)。 因此可以从dark pixels中建立haze's transmission的估计。 最后结合haze imaging model和soft matting interpolation method进行图片去雾和深度图估计。 


# 实现方法
### Dark Channel Prior 
定义暗通道为一个像素及其附近邻域像素值最小的通道。 
![[Pasted image 20240329193908.png]]
暗通道的先验是指:一个图片如果不包含雾霾，那么暗通道值应该接近于0
![[Pasted image 20240329194148.png]]
### 使用暗通道先验去雾
