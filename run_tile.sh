python run_infer.py \
--gpu='0' \
--nr_types=6 \
--type_info_path=type_info.json \
--batch_size=64 \
--model_mode=fast \
--model_path=./pretrained/hovernet_fast_pannuke_type_tf2pytorch.tar \
--nr_inference_workers=0 \
--nr_post_proc_workers=0 \
tile \
--input_dir=F:/CHFE/Virtual_Staining/cycleGAN/trainA \
--output_dir=F:/CHFE/Virtual_Staining/hovernet/test \
--mem_usage=0.1 \

