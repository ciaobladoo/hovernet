python run_infer.py \
--gpu='0' \
--nr_types=6 \
--type_info_path=type_info.json \
--batch_size=64 \
--model_mode=fast \
--model_path=pretrained/hovernet_fast_pannuke_type_tf2pytorch.tar \
--nr_inference_workers=8 \
--nr_post_proc_workers=16 \
wsi \
--input_dir=F:/CHFE/TCGA/HNSC/slides/$1 \
--output_dir=F:/CHFE/TCGA/HNSC/hovernet \
--input_mask_dir=F:/CHFE/TCGA/HNSC/tissue_masks \
--save_thumb \
--cache_path=F:/CHFE/TCGA/HNSC/cache
