#!/bin/sh


python3 -m torch.distributed.launch --nproc_per_node 2 train.py --img $IMG_SIZE --batch $BATCH_SIZE --epochs $EPOCHS --data ${CONFIG_PATH:-/srv/dataset/config.yaml} --iou-thres $IOU --weights $TL_WEIGHTS --cache
ls -la /srv/runs/train/exp
