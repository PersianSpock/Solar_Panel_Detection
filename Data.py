import os
import glob
from PIL import Image
from pathlib import Path
import cv2
import torch
import numpy as np
import skimage.measure as km
import matplotlib.pyplot as plt
import shutil
import argparse
import re
import torch.cuda
from scipy.spatial import distance
import detect as yolo_eval
from sklearn.model_selection import train_test_split
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from skimage import io
from skimage.filters import threshold_otsu
from torchvision.ops import nms
from concurrent.futures import ThreadPoolExecutor


#!wget -O Data.zip "https://storage.googleapis.com/kaggle-data-sets/2735184/4778133/compressed/PV03.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230523%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230523T074116Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=a564f5036a888f931a362e3e095d482827b8e47c6be6366bfc7b49224e47fb5b0044050e2d7086bff73ea5b39225af2048551e2d124b4c4fc70663acedddec8d4a32b8e494a60d24c0614e8e986d97335dd066c9ac6fa9ac298a44aee969d6323514cdf904adab98dac4295e2e657be02047d5a438819316ef3c833b300887a8020c038114d2920deddb82ea005e59fc545df622b0bc401ece1e988c43d4889665be741a6fae465463f727885b90bc141dbece88bd1bf21e39a7da00d243ffc125dd3d581071ad8cc58a38f9b0a374a680913afbdb47284a8be7c83cd974a464554c4af7e7e712edc52b104c9575ab46926c1dc0c0684d80fc9de0138dbe88dd"

#!unzip Data.zip

def train_test_dev_folder():

    source = "/content/drive/MyDrive/PV03_Rooftop"
    rootdir = "/content/drive/MyDrive/Solar_Panels/images"
    allFileNames = os.listdir(source)
    np.random.shuffle(allFileNames)

    test_ratio = 0.25


    train_val_FileNames, test_FileNames = np.split(np.array(allFileNames),[int(len(allFileNames)* (1 - test_ratio))])

    train_FileNames, valid_FileNames = np.split(np.array(train_val_FileNames),[int(len(train_val_FileNames)* (1 - test_ratio))])

    train_FileNames = [source+'/'+ name for name in train_FileNames.tolist()]
    test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]
    valid_FileNames = [source+'/' + name for name in valid_FileNames.tolist()]

    for name in train_FileNames:
      shutil.copy(name, rootdir +'/train/')

    for name in test_FileNames:
      shutil.copy(name, rootdir +'/test/')

    for name in valid_FileNames:
      shutil.copy(name, rootdir +'/val/')


def png_paral()
    folder='/content/drive/MyDrive/Solar_Panels'
    for phase in ['train', 'val', 'test']:
            img_path, mask_path = f'{folder}/images/{phase}', f'{folder}/masks/{phase}'
            for img in glob.glob(f'{img_path}/*.bmp'):
                new_name = os.path.splitext(img)[0]
                print(new_name)
                Image.open(img).resize((256,256)).save(os.path.join(img_path, str(new_name) + '.png'))
                os.remove(img)
                print("********")
            for img in glob.glob(f'{img_path}/*label.png'):
                shutil.copy(img, mask_path)
                os.remove(img)
                print("&&&&&&")
      

