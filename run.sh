python ./adl2023_hw1_m11151033/formatting.py \
  --context_file $1 \
  --test_file $2

python ./adl2023_hw1_m11151033/paragraph_selection.py \
  --test_file $2 \
  --model_name_or_path ./adl2023_hw1_m11151033/paragraph_selection \
  --per_device_eval_batch_size 1 \
  --num_train_epochs 0 \
  --max_seq_length 512 \
  --seed 11151033 \
  --do_predict \
  --gpu 0

python ./adl2023_hw1_m11151033/span_selection.py \
  --test_file $2 \
  --model_name_or_path ./adl2023_hw1_m11151033/span_selection \
  --per_device_eval_batch_size 1 \
  --num_train_epochs 0 \
  --max_seq_length 512 \
  --seed 11151033 \
  --do_predict \
  --gpu 0 \
  --prediction_path $3
