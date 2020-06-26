'''
Created on 2020��1��10��

@author: 21970
'''
import tensorlayer as tl
import numpy as np 
import os
import nibabel as nib
import threading  
import tensorflow as tf
import matplotlib.pyplot as plt
import scipy
from tensorlayer.prepro import *
import skimage.measure

nib.Nifti1Header.quaternion_threshold = - np.finfo(np.float32).eps * 10  # �ɳ�һ������
training_data_path = "Training_100"
preserving_ratio = 0.25 # filter out 2d images containing < 25% non-zeros


f_train = tl.files.load_file_list(path=training_data_path,
                                      regx='.*.gz',
                                      printable=False)  # ��test���Լ����е�������list��ʽ������
X_train = []  # ����ѵ��������
for fi, f in enumerate(f_train):   # �൱��ȡ���±������Լ�list������ص�����
    img_path = os.path.join(training_data_path, f)
    # print(img_path)
    img = nib.load(img_path).get_data()  
    # print(img.shape)
    img_3d_max = np.amax(img)  
    img = img / img_3d_max * 255  # ����������ؽ��й�һ�����0-255��Χ,���������ά����
    for i in range(img.shape[2]):   # ����Ƭ����ѭ��
        img_2d = img[:, :, i]  # ȡ��һ��ͼ��
       # plt.imshow(img_2d) ��ʾͼ��
       # plt.pause(0.001)
        # filter out 2d images containing < 10% non-zeros
        # print(np.count_nonzero(img_2d))
        #print("before process:", img_2d.shape)
        if float(np.count_nonzero(img_2d)) / img_2d.size >= preserving_ratio:  # ��ʾһ��ͼ���0������������ͼ���10%���ǲŰѸ�ͼ��������
            img_2d = img_2d / 127.5 - 1  # �������0-255ͼ����й�һ����[-1, 1]��Χ֮��
            img_2d = np.transpose(img_2d, (1, 0))  # ����൱�ڽ�ͼ�������ת90��
            # plt.imshow(img_2d)
            # plt.pause(0.01)
            X_train.append(img_2d)
        # print(len(X_train)) 
X_train = np.asarray(X_train, dtype=np.float32)  # ��ѵ����ͼ������ԭ����list���ڱ��np.array��ʽ
X_train = X_train[:, :, :, np.newaxis]  # ���4ά����
