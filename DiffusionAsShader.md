# [SIGGRPAH25] Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control


![[Pasted image 20250731150037.png]]

project url: https://igl-hkust.github.io/das/

# Summary 

3D-aware video generation: 接受3D tracking video作为video diffusion model的额外条件做生成。 3D tracking video 可以提供物体的准确运动轨迹，物体的变化，相机轨迹。



# Detail
Baseline Method: MotionCtrl, CameraCtrl ; CCEdit,TokenFlow

Data: real-world videos + synthetic data. 视频数据来自MiraData，用里面的mesh和motion sequence来渲染视频。 SpatialTracker得到3D点云。 
