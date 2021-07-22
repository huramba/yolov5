#!/bin/sh

python3 train.py --img $IMG_SIZE --batch $BATCH_SIZE --epochs $EPOCHS --data ${CONFIG_PATH:-/srv/dataset/config.yaml} --weights $TL_WEIGHTS --iou-thres $IOU_THRES --cache
