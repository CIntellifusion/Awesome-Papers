- 不发布code还没release
# modification
1. 首先改pretrained model和SD model的`绝对路径`，相对路径
2. Dataset config没有 
	- [x] 检查follow lvdm 的config 
	- [x] 下载web10m 等数据集
	- [x] 看dataset类的实现方式: 需要一个metadata并且转化为mp4数据
	- [ ] 


# 1 Implementation 

VideoCrafter基于pytorch_lightning写的预训练代码，利用DDPS进行加速。 
核心就是一个`trainer.fit(model,data)`

## 1.1 config 
这里的target是按照文件夹里面的类写的和import语法一样
后面params作为字典传进去的，和类初始化需要接受的参数一致。 
```python folder title="config example"
unet_config:

      target: lvdm.modules.networks.openaimodel3d.UNetModel

      params:

        freeze: True

        in_channels: 4
        
```

`config.yaml`分为`model`,`data`,`lightning`三部分

`model`里面写了`pretrained_checkpoint`的位置，`DiffusionModel`框架的实现，主要有Unet,First_stage_condition,second_stage_condition三个子神经网络模块组成，其余还有损失函数等设置。 

`data`里面写了数据集构造，`resolution`,`dataset_warpper`和具体负责加载数据的dataset类实现。 这里的两层实现支持了多个不同的数据集一起训练，也支持了微调阶段更改数据集。 


`lightning`里面写了训练设置，包括`batch_size`,`max_epoch`,`logging`,`gradient accumulation`等等，整体是用来初始化工作区的，里面包含trainer的设置。 trainer和args里面设置合并之后得到trainer的总设置。  trainer只有参数没有自定义类 

## 1.1.1 Config到类的初始化

```python title:instantiate_from_config
def instantiate_from_config(config):
    if not "target" in config:
        if config == '__is_first_stage__':
            return None
        elif config == "__is_unconditional__":
            return None
        raise KeyError("Expected key `target` to instantiate.")
    return get_obj_from_str(config["target"])(**config.get("params", dict()))

def get_obj_from_str(string, reload=False):
    module, cls = string.rsplit(".", 1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module, package=None), cls)
```

找到target和params分别用来导入类和初始化类，返回的是实例化的对象


> 以前没发现这样写很方便，要改config的话不用改import代码和实例初始化的代码



## 1.2 Models
这里的模型是基类是DDPM，DDPM负责前向和后向的传播过程，Model类是一个Unet


在pytorch_lightning框架下，模型是直接返回损失函数值的,如果要修改的话需要:
- 更改DDPM.get_loss(pred,target,mean=True) 277行
- 更改config.model.loss_type

![[picture/Pasted image 20240411233525.png|videocrafter设置loss的地方，把else实现了就可以]]

![[picture/Pasted image 20240411233757.png|Diffusion DPO的loss实现,这个If-else分支只能说一模一样]]


### 1.2.1 DDPM And LatentDIffusion

[[Diffusion/Unconditional Diffusion|Unconditional Diffusion]]我们实现了一个DDPM和DDIM

#### register schedule
负责定义加噪过程中根据时间步t变化的超参数$\alpha_{t} \beta_{t}$数组

![[picture/Pasted image 20240505225732.png|不是吧兄弟，你定义一堆这样代码真的让人很男改训练精度的啦。而且这个函数还在这个文件的不同地方分别定义了两次]]




这是一个基于LDM的对3D数据即video的实现

所以这个类里面还包含了condition的实现


### 1.2.2  Cast DDPM3D
- 上图里面的`ref_unet`在lightning框架下要写成DDPM的一个子模块`self.ref_model`
- 在config里面加入一个超参数`beta_dpo`
- 在`self.get_loss`里面实现一个分支`dpo_loss`
- 在`self.p_losses`里面计算`ref_pred`


### 1.2.2 Diffusion Wrapper
diffusion model是unet model 
类在`lvdm.modules.networks.openaimodel3d.UNetModel`

包含的参数
in channel和out channel都是4,这和video一致

video crafter 默认的condition类型是cross_attention

这个Warpper是用来包裹Unet的，负责调用不同的condition添加形式，包括cross_attention / concat / hybird concat 等等




## 1.3 Dataset 
原来取出来是[channel,length,H,W]
现在应该是[2channel,length,H,W]


Dataset: data.lightning_data.DataModuleFromConfig
这个lightning data加载子数据集用的是`instantiate_from_config`。 
所以需要重写一个子类来加载数据。 

### 1.3.1 Cast Dataset 
现在新建一个类`MacVidDPO`，在这个类接受包含['video1','video2','label0','caption']的列表。 
然后从`MacVid`类里面取数据，整合，返回一个并列的`Video Tensor`和`Caption`。

在构造DataLoader的时候加入一个新的`collate_fn`

- 改config.data.params.target改成DPO数据集的实现
- pair.json从metapath构造即可，不需要更改配置文件
- 改`train_data_yaml`路径
- 构造数据集: 把同一个视频重复写一下路径、甚至不用，index设置来一样就可以了。 加载同一个视频可能会有竞争问题，但是考虑这事一个rr竞争，我就不考虑了。 
- 打印一下data pair 数量
- 

## 1.4 train.py
这个脚本里主要包括从命令行和配置文件接收参数，构造dataset,model,trainer，加载checkpoint,开始训练。 

训练默认DDPshare的方式进行并行；可以选用DeepSpeed进行加速。 

## Debug
## bug1 DDPM3D加了refmodel之后state_dict对不上

看`train_utils`里面的`load_checkpoint`函数。 里面给了
- pretrained checkpoint 
- sd checkpoint 
- adapter only 
- train temporal 
几个选项。 

现在我需要加载sd checkpoint两次,一个训练用，一个ref用；同时没有pretrained_checkpoint

- [x] 没有refmodel的时候，删掉config里的pretrained_ckpt字段，会只加载stable diffusion
   Num of parameters of target model: 2039
	Num of parameters of source model: 1240
- [ ] 如果加上ref model，希望把sd加载两次
	Num of parameters of target model: 3523
	Num of parameters of source model: 1240
- [ ] 检查 target models和 source model的keys
	在`/home/haoyu/research/LVDM-UST-VideoCrafterft/keys.txt`里面，注意到
	两个unet只有model和refmodel字段的区别，
	所以加载的时候复制一个ckpt将前缀替换为ref_model
	注意此处的ref_model是有关于属性名的
- [ ] config里面加入ref_model_checkpoint字段
- [ ] ref model的参数应该全冻住

ref model加载基本上完成
加载正确性或许需要进一步检查

## bug2 张量维度问题
`Given groups=1, weight of size [128, 3, 3, 3], expected input[1, 6, 320, 512] to have 3 channels, but got 6 channels instead`
然后我回去看dpo的代码
- 首先确实在channel dim堆叠
- 其次都是F.cov2d报错
所以回去看代码发现:
`feed_pixel_values = torch.cat(batch["pixel_values"].chunk(2, dim=1))`

- [ ] 实际上用的是`LatentDiffusion`类
- [ ] 但是`LatentDiffusion`类继承了`DDPDM`的`get_loss`方法，因此dpoloss的实现有效
- [ ] 但是需要修改`LatentDiffusion`的`p_losses`方法
	- [ ] 注意需要duplicate encoder hidden states 1次 
	- [ ] 每一个分支都需要检查是否是dpo策略
	- [ ] dpo loss还有个reduction问题 之后可能整合一下 不然太丑陋了
- [ ] `first_staget_model`对应`vae`
- [ ] `cond_stage_model`对应`text_encoder`




