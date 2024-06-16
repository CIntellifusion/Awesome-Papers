
a diffusion-based generative model 036 037 designed for 3D volumetric head.


# 1Motivation

contribution:
- a novel representation for 3D volumetric head 
- auto-decoding fitting algorithm for training data generation
- experiments on several tasks 

# 2 Related Work
## 2.1 3D-aware GAN
generating multi-view consistent portraits with volumetric rendering. 
Editing latent space through auto-decoding. 

## 2.2 Diffusion Models 
pass

## 3 Method
## 3.1 Avatar Representation
represent each point by a 3D gaussian. Using volumetric rendering method. 

# Summary
A method for 3D head generation and manipulation.  The author proposed a new implicit representation of 3D volumetric geometry anchored on 3DMM. The representation is trained on a generated multi-view dataset using an auto-decoder. Then a 2D-unet is trained in the tri-plane UV space in a diffusion manner.  Finally, the model is able to edit the shape and expression of 3D heads.
Experiments on several tasks shows competitive results. 
## Strengths
1. The rendering results on large poses and other extreme locations are clear and sound. 
2. Adapting diffusion models into 3D representation space of 3D head is novel and reasonable compared to previous GANs. 
3. The proposed method can be applied to several downstream applications like editing and inpainting which is charming. 

## Weakness
1. How tri-plane representation and UV space are aligned is not clear. line213-215 the dimension of the target space need further illustration. 
2. The method used to render the rgb image in section 3.2, volumetric rendering or rasterize, is not mentioned. 
3. While the ID and Depth is both worse than Pano-Head, the dataset construction method may not work as expected. Real world data seems necessary which is not discussed at all.  Even single view real data is worth trying. 
## Rating
Borderline or WR
if the illustration of weakness 1,2 are clear enough, then:
Borderline.
If the training result on real world data or hybrid data is added, then:
WA
## Recommendation confidence
very confident. 
## Justification of rating
1. The illustration of each step performed in the method. 
2. The comparison result and downstream application. 

## Societal Impact 
no. 

## dataset contribution
他有个数据集，但是没做contribution说

## Additional Comments to authors
1.How could the hair and teeth be rendered in the Image while it is not in 3DMM? 
2 Whether the detailed dataset construction method or the training dataset itself will be released?
