import numpy as np

TAR_H = 401
TAR_W = 401

NUM_GPUS = 1
BATCH_SIZE = 10
PREFETCH_SIZE = 50
SHUFFLE_SIZE = 50
REPEAT_COUNT = 2


NUM_RECURRENT = 2

RADIUS = 32
STRIDE = 8

MAX_FRAME_SIZE = 10

HEATMAP_LOSS_WEIGHT = 4.0
SHORT_OFFSET_LOSS_WEIGHT = 1.0
MIDDLE_OFFSET_LOSS_WEIGHT = 0.5

TRAIN_DATA_BASE_DIR = 'dataset/surreal/cmu/train/'
VAL_DATA_BASE_DIR = 'dataset/surreal/cmu/val/'
# TRAIN_DATA_BASE_DIR = '/tmp/cmu/train/'
#VAL_DATA_BASE_DIR = 's3://syd-surreal/cmu/train'