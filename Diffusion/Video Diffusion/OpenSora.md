
# inference

1. 3090不支持apex layernorm 需要在设置里修改 layernorm 为torch默认
2. layernorm不支持半精度推理 需要修改数据类型为float
3. flashattent也先设置不支持
4. 模型的device需要设置到cuda 

- [ ] 4.25 现在有H800了可以重新跑一个opensora 
- [ ] opensora colossalAI又更新了