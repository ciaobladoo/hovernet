python run_infer.py \
--gpu='0' \
--nr_types=6 \
--type_info_path=type_info.json \
--batch_size=16 \
--model_mode=fast \
--model_path=pretrained/hovernet_fast_pannuke_type_tf2pytorch.tar \
--nr_inference_workers=8 \
--nr_post_proc_workers=8 \
wsi \
--input_dir=$1 \
--output_dir=/home/ec2-user/projects/nuclear_identification/hovernet/MDA-output \
--input_mask_dir=/home/ec2-user/projects/nuclear_identification/hovernet/masks \
--save_thumb \
--cache_path=/home/ec2-user/cache
