# AutoEncoderKL
直接看diffusers的官方实现[code reference](https://github.com/huggingface/diffusers/blob/main/src/diffusers/models/autoencoders/autoencoder_kl.py)

vae在stablediffusion生成图片中的作用，以伪代码展示:
```python 
#during train 
latents=vae.encode(feed_pixel_values.to(weight_dtype)).latent_dist.sample()
latents = latents * vae.config.scaling_factor
```

在`encoding`的过程中分为以下几步:
1. 利用encoder将image编码成一个隐向量
2. 用quant_conv进行离散化
3. 用对角高斯分布采样一个后验
4. 构造一个AutoencoderKLOutput

AutoencoderKLOutput包含一个last_latent属性，赋值为对角高斯分布采样的后验

看完之后要带着断点跑一遍这个vae

训练过程中的latents实际上是从对角高斯分布里面采样出来的随机向量。  此处通过固定随机数种子可以固定。 

decode的代码应该在pipeline里面

# VAE 
VAE的实现中，每个样本都会预测一个均值和一个方差。 
```python 
Class VAE()：
	def __init__(self):
		# omit 
		# https://github.com/AntixK/PyTorch-VAE/blob/master/models/beta_vae.py
    def encode(self, input: Tensor) -> List[Tensor]:
        """
        Encodes the input by passing through the encoder network
        and returns the latent codes.
        :param input: (Tensor) Input tensor to encoder [N x C x H x W]
        :return: (Tensor) List of latent codes
        """
        result = self.encoder(input)
        result = torch.flatten(result, start_dim=1)

        # Split the result into mu and var components
        # of the latent Gaussian distribution
        mu = self.fc_mu(result)
        log_var = self.fc_var(result)

        return [mu, log_var]
    def reparameterize(self, mu: Tensor, logvar: Tensor) -> Tensor:
        """
        Will a single z be enough ti compute the expectation
        for the loss??
        :param mu: (Tensor) Mean of the latent Gaussian
        :param logvar: (Tensor) Standard deviation of the latent Gaussian
        :return:
        """
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return eps * std + mu
    def forward(self, input: Tensor, **kwargs) -> Tensor:
        mu, log_var = self.encode(input)
        z = self.reparameterize(mu, log_var)
        return  [self.decode(z), input, mu, log_var]
```

损失函数包括:
```python 
    def loss_function(self,
                      *args,
                      **kwargs) -> dict:
        self.num_iter += 1
        recons = args[0]
        input = args[1]
        mu = args[2]
        log_var = args[3]
        kld_weight = kwargs['M_N']  # Account for the minibatch samples from the dataset

        recons_loss =F.mse_loss(recons, input)

        kld_loss = torch.mean(-0.5 * torch.sum(1 + log_var - mu ** 2 - log_var.exp(), dim = 1), dim = 0)

        if self.loss_type == 'H': # https://openreview.net/forum?id=Sy2fzU9gl
            loss = recons_loss + self.beta * kld_weight * kld_loss
        elif self.loss_type == 'B': # https://arxiv.org/pdf/1804.03599.pdf
            self.C_max = self.C_max.to(input.device)
            C = torch.clamp(self.C_max/self.C_stop_iter * self.num_iter, 0, self.C_max.data[0])
            loss = recons_loss + self.gamma * kld_weight* (kld_loss - C).abs()
        else:
            raise ValueError('Undefined loss type.')

        return {'loss': loss, 'Reconstruction_Loss':recons_loss, 'KLD':kld_loss}

```

一个MSE重建损失，一个分布损失

采样函数
```python 
    def sample(self,
               num_samples:int,
               current_device: int, **kwargs) -> Tensor:
        """
        Samples from the latent space and return the corresponding
        image space map.
        :param num_samples: (Int) Number of samples
        :param current_device: (Int) Device to run the model
        :return: (Tensor)
        """
        z = torch.randn(num_samples,
                        self.latent_dim)

        z = z.to(current_device)

        samples = self.decode(z)
        return samples
```

## VAE Implementation

## VAE training on MNIST

[Jackson-Kang/Pytorch-VAE-tutorial: A simple tutorial of Variational AutoEncoders with Pytorch (github.com)](https://github.com/Jackson-Kang/Pytorch-VAE-tutorial)
30 epochs 
![[picture/Pasted image 20240508202327.png]]



## findings

1. the distribution of the model is really crucial 

```python 
        if transform is None :

            transform = transforms.Compose([

                transforms.ToTensor(),

                # transforms.Normalize((0.1307,), (0.3081,)) #

            ])
```
simply uncomment the line 7 will lead to heavy performance decrease 


2. pin_memory could be useful for little dataset , with 2x iteration during training 
3. 