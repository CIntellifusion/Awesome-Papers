# Summary
This paper focus on the naturalness and realism issue caused by ignoring emotion in speech-driven 3d facial animation. They propose a new dataset consisting of 8 emotion categories called Emolib， cooperating teeth model into the original face model.  Then they propose a framework to animate emotion controllable talking head. Finally, texture of input person is added to photo realistic rendering. 

# Strengths
- A new large dataset of 10736 emotional face is proposed. Creatively adding mouth structure for better animation. 
- Using UV texture for talking head animation is a good attempt and has a clear future application.
- Experiments conducted on diverse datasets using different methods have demonstrated consistent and promising results for the proposed approach.
# Limitations
- The detailed analysis of the proposed dataset should be provided to prove its quality.
- The texture extraction method is relatively old and coupled with light. Maybe some newer method can be considered for better looking. 
- The design of sub modules in section 4.1 and 4.2 is not clear enough to demonstrate innovative design if there is any.  


# Rate
BA or WA 
- a completed work 



# Confidence
- confident 



# Other comments 
> this part is written for reference. 

他们的texture用的是最naive的texture实现，就是直接根据landmark从image上抓的像素。 
maybe some better skin can be adopted for better looking. 
![[picture/Pasted image 20240430135509.png]]