# NTU ADL 2023 Fall HW1
## Paragraph selection + Span selection
### Step 1. Format data
```
python formatting.py \
  --context_file ./ntuadl2023hw1/context.json \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --test_file ./ntuadl2023hw1/test.json
```
### Step 2. Training model (Paragraph selection)

```
python paragraph_selection.py \
  --model_name_or_path hfl/chinese-macbert-large \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --max_seq_length 512 \
  --per_device_train_batch_size 1 \
  --learning_rate 1e-5 \
  --num_train_epochs 3 \
  --gradient_accumulation_steps 8 \
  --output_dir /tmp/paragraph_selection \
  --seed 11151033 \
  --gpu 0
```
#### ****Not Pre-trained***
```
python paragraph_selection.py \
  --model_name_or_path bert-base-chinese \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --max_seq_length 512 \
  --per_device_train_batch_size 1 \
  --learning_rate 3e-5 \
  --num_train_epochs 1 \
  --gradient_accumulation_steps 2 \
  --output_dir /tmp/paragraph_selection \
  --seed 11151033 \
  --gpu 0 \
  --no_pretrain
```
### Step 3. Training model (Span selection)
```
python span_selection.py \
  --model_name_or_path hfl/chinese-macbert-large \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --max_seq_length 512 \
  --per_device_train_batch_size 1 \
  --learning_rate 1e-5 \
  --num_train_epochs 10 \
  --gradient_accumulation_steps 8 \
  --output_dir /tmp/span_selection \
  --seed 11151033 \
  --gpu 0
```
#### ****Not Pre-trained***
```
python span_selection.py \
  --model_name_or_path bert-base-chinese \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --max_seq_length 512 \
  --per_device_train_batch_size 1 \
  --learning_rate 3e-5 \
  --num_train_epochs 1 \
  --gradient_accumulation_steps 2 \
  --output_dir /tmp/span_selection \
  --seed 11151033 \
  --gpu 0 \
  --no_pretrain
```
### Step 4. Model prediction (Paragraph selection)
```
python paragraph_selection.py \
  --test_file ./ntuadl2023hw1/test.json \
  --model_name_or_path /tmp/paragraph_selection \
  --per_device_eval_batch_size 1 \
  --num_train_epochs 0 \
  --max_seq_length 512 \
  --seed 11151033 \
  --do_predict \
  --gpu 0
```
### Step 5. Model prediction (Span selection)
```
python span_selection.py \
  --test_file ./ntuadl2023hw1/test.json \
  --model_name_or_path /tmp/span_selection \
  --per_device_eval_batch_size 1 \
  --num_train_epochs 0 \
  --max_seq_length 512 \
  --seed 11151033 \
  --do_predict \
  --gpu 0 \
  --prediction_path /tmp/prediction.csv
```
## End-to-End
### Step 1. Format data
```
python formatting.py \
  --context_file ./ntuadl2023hw1/context.json \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --test_file ./ntuadl2023hw1/test.json \
  --end_to_end 
```
### Step 2. Training model and prediction
```
python span_selection.py \
  --model_name_or_path hfl/chinese-xlnet-base \
  --train_file ./ntuadl2023hw1/train.json \
  --validation_file ./ntuadl2023hw1/valid.json \
  --test_file ./ntuadl2023hw1/test.json \
  --max_seq_length 2048 \
  --per_device_train_batch_size 1 \
  --per_device_eval_batch_size 1 \
  --learning_rate 3e-5 \
  --num_train_epochs 3 \
  --gradient_accumulation_steps 2 \
  --output_dir /tmp/chinese_extractive_QA \
  --seed 11151033 \
  --do_predict \
  --gpu 0 \
  --prediction_path /tmp/prediction.csv
```
## download
```
bash ./download.sh
```
## run
```
bash ./run.sh ./adl2023_hw1_m11151033/ntuadl2023hw1/context.json ./adl2023_hw1_m11151033/ntuadl2023hw1/test.json ./prediction.csv
```