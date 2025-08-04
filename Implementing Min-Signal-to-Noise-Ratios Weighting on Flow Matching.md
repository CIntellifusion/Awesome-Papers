**Summary:**  
This paper proposes applying the Min-SNR weighting strategy to Flow Matching (FM) models. The authors introduce a new definition of SNR to the FM. Experimental validation is conducted on the CIFAR-10 dataset.

---

**Pros:**

- The proposed definition of SNR for flow-based models is intuitive and aligns well with the linear interpolation structure in FM.
    
- The paper is clearly written and easy to follow.
    

---

**Cons:**

- The paper lacks technical novelty. The original Min-SNR paper ("Efficient Diffusion Training via Min-SNR Weighting Strategy") has already shown that Min-SNR can be applied across various prediction targets. Extending it to FM is a straightforward step.
    
- The experimental validation is weak. The reported FID on CIFAR-10 is surprisingly high, suggesting that the model capacity may be insufficient, the training schedule may be inadequate, and the inference strategy is outdated (e.g., DDIM is not even used). These issues undermine the credibility of the experimental conclusions.
    

---

**Overall Recommendation:**  
**Reject.** While the proposed idea is reasonable, it lacks novelty and the experimental results are not strong enough to support the claims.