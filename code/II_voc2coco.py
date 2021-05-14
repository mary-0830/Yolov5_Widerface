# coding:utf-8
import os
import shutil
from tqdm import tqdm
# 根据/data/data/UAV2017/ImageSets/Layout里面的trainval.txt和test.txt挑选出训练集和测试集
 
SPLIT_PATH = "/home/jjliao/faceDetection/data/wider_voc/ImageSets/Main"
IMGS_PATH = "/home/jjliao/faceDetection/data/wider_voc/JPEGImages"
TXTS_PATH = "/home/jjliao/faceDetection/data/wider_voc/Annotations"
 
TO_IMGS_PATH = '/home/jjliao/faceDetection/data/wider_coco/images'
TO_TXTS_PATH = '/home/jjliao/faceDetection/data/wider_coco/xml_annotations'
 
 
data_split = ['train.txt', 'val.txt']
to_split = ['train', 'val']

train_file = '/home/jjliao/faceDetection/data/wider_yolo/images_train.txt'
val_file = '/home/jjliao/faceDetection/data/wider_yolo/images_val.txt'
train_file_txt = ''
val_file_txt = ''
 
for index, split in enumerate(data_split):
    split_path = os.path.join(SPLIT_PATH, split)
    # import pdb; pdb.set_trace()
 
    to_imgs_path = os.path.join(TO_IMGS_PATH, to_split[index])
    if not os.path.exists(to_imgs_path):
        os.makedirs(to_imgs_path)
 
    to_txts_path = os.path.join(TO_TXTS_PATH, to_split[index])
    if not os.path.exists(to_txts_path):
        os.makedirs(to_txts_path)
 
    f = open(split_path, 'r')
    count = 1

    for line in tqdm(f.readlines(), desc="{} is copying".format(to_split[index])):
        # 复制图片
        src_img_path = os.path.join(IMGS_PATH, line.strip() + '.jpg')
        # import pdb; pdb.set_trace()
        dst_img_path = os.path.join(to_imgs_path, line.strip() + '.jpg')
        if os.path.exists(src_img_path):
            shutil.copyfile(src_img_path, dst_img_path)
        else:
            print("error file: {}".format(src_img_path))
        if to_split[index] == 'train':
            train_file_txt = train_file_txt + dst_img_path + '\n'
        elif to_split[index] == 'val':
            val_file_txt = val_file_txt + dst_img_path + '\n'
 
        # 复制txt标注文件
        src_txt_path = os.path.join(TXTS_PATH, line.strip() + '.xml')
        dst_txt_path = os.path.join(to_txts_path, line.strip() + '.xml')
        if os.path.exists(src_txt_path):
            shutil.copyfile(src_txt_path, dst_txt_path)
        else:
            print("error file: {}".format(src_txt_path))
    with open(train_file, 'w') as out_train:
        out_train.write(train_file_txt)

    with open(val_file, 'w') as out_val:
        out_val.write(val_file_txt)