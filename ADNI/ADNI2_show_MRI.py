#  --*--  encoding:utf-8 --*--

from nibabel.viewers import OrthoSlicer3D
from nibabel import nifti1
import nibabel as nib
from matplotlib import pylab as plt
import matplotlib


# matplotlib.use('TkAgg')
# 需要查看的nii文件名文件名.nii或nii.gz
#filename = r'H:\graduation project\datafile\AD_001\AD_001.nii'
#filename = r'E:\GoogleDownloads\TBM_Jacobian_Maps_MDT-SC\ADNI\099_S_0880\TBM_Jacobian_Maps_[MDT_-_Screening]\2006-10-05_07_03_06.0\S19744\ADNI_099_S_0880_MR_TBM_Jacobian_Maps_[MDT_-_Screening]_Br_20140425145318774_S19744_I421787.nii' 
filename = r'E:\GoogleDownloads\ADNI1_Complete_3Yr_3T\ADNI\100_S_0930\TBM_Jacobian_Maps_[MDT_-_Screening]\2006-10-03_13_27_14.0\S19654\ADNI_100_S_0930_MR_TBM_Jacobian_Maps_[MDT_-_Screening]_Br_20140425145351325_S19654_I421792.nii'
img = nib.load(filename)
# 打印文件信息
print(img)
print(img.dataobj.shape)
#shape不一定只有三个参数，打印出来看一下
#width, height, queue, sam = img.dataobj.shape
width, height, queue = img.dataobj.shape
# 显示3D图像
OrthoSlicer3D(img.dataobj).show()
# # 计算看需要多少个位置来放切片图
# x = int((queue/10) ** 0.5) + 1
# num = 1
# # 按照10的步长，切片，显示2D图像
# for i in range(0, queue, 10): 
#     img_arr = img.dataobj[:, :, i]
#     plt.subplot(x, x, num)
#     plt.imshow(img_arr, cmap='gray')
#     num += 1
# plt.show()
 
 
# 
# '''
# 
# import nibabel as nib
# import matplotlib.pyplot as plt
# from numpy import size, shape, array
# from PIL import Image
# 
# 
# def read_data(path):
#     image_data = nib.load(path).get_data()
#     return image_data
#  
# def show_img(ori_img):
# #     for i in range(0, (ori_img.shape)[2]):
# #         plt.imshow(ori_img[:,:,i], cmap = 'gray') #channel_last
# #         plt.show()
#     #plt.imshow(ori_img[ : , : , 100 , 0 ], cmap = 'gray') #channel_last
#     plt.imshow(ori_img[ 100 , : ,: ,0 ], cmap = 'gray') #channel_last
#     #ndarray to picture
# #     a = array(ori_img[ : , : , 100 , 0 ])
# #     print(type(a))
# #     ndarray_convert_img= Image.fromarray(a)
# #     plt.imshow(ndarray_convert_img, cmap = 'gray') #channel_last
#     plt.show()
# #path = 'E:\\GoogleDownloads\\ADNI1_Annual_2_Yr_1.5T\\ADNI\\027_S_0408\\MPR__GradWarp__B1_Correction__N3__Scaled\\2006-05-10_13_41_42.0\\S14231\\ADNI_027_S_0408_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070129173016787_S14231_I37548.nii'
# path = r'H:\graduation project\datafile\AD_001\AD_001.nii'
# data = read_data(path)
# print(shape(data))#(176, 240, 256, 1)//////(220, 220, 220)
# show_img(data)
# '''