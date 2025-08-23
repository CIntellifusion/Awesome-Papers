

# v7 full fintuning
accelerate launch \
  --num_processes 1 \
  --num_machines 1 \
  --mixed_precision bf16 \
  examples/wanvideo/model_training/train_physics_dpo_v7.py \
  --dataset_base_path /root/code_and_model/Wan1.3B/win/ \
  --height 480 \
  --width 832 \
  --dataset_repeat 10000 \
  --model_id_with_origin_paths "Wan-AI/Wan2.1-T2V-1.3B:diffusion_pytorch_model*.safetensors,Wan-AI/Wan2.1-T2V-1.3B:models_t5_umt5-xxl-enc-bf16.pth,Wan-AI/Wan2.1-T2V-1.3B:Wan2.1_VAE.pth" \
  --learning_rate 1e-5 \
  --total_training_steps 100000 \
  --remove_prefix_in_ckpt "pipe.dit." \
  --trainable_models "dit" \
  --output_path "/root/autodl-tmp" \
  --dataset_metadata_path /root/code_and_model/Wan1.3B/dpo_overfitting.json \
  --dataset_base_path_positive /root/code_and_model/Wan1.3B/win/ \
  --dataset_base_path_negative /root/code_and_model/Wan1.3B/lose/ \
  --save_every_steps 50 \
  --log_every_steps 5 \
  --gradient_accumulation_steps 1 \
  --dpo_beta 5000

torchrun  --standalone --nproc_per_node=1 examples/wanvideo/model_training/validate_lora/Wan2.1-T2V-1.3B_tensor_parallel_lora_dpo_overfitting_full.py \
  --weight_path /root/autodl-tmp/state-step-0000020/model.safetensors \
  --output_folder dpo_overfitting_output_v7