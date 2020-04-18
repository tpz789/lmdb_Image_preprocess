import lmdb
import os
from PIL import Image
import numpy as np
import cv2
import io
import xml.etree.ElementTree as ET
from os import getcwd

# ### 存图片到lmdb
# images_path = './JPEGImages'
#
# total_img = os.listdir(images_path)
# num = len(total_img)
# list = range(num)
#
# env = lmdb.open('lmdb_image_dir', map_size=1073741824) #size=1GB
# cache = {}  # 存储键值对
#
# for i in list:
#     image_file_path = os.path.join(images_path, total_img[i])
#     with open(image_file_path, 'rb') as f:
#         # 读取图像文件的二进制格式数据
#         image_bin = f.read()
#
#         # 用两个键值对表示一个数据样本
#         cache['{}'.format(total_img[i][:-4])] = image_bin
#
# for k, v in cache.items():
#     # with env.begin(write=True) as txn:
#     txn = env.begin(write=True)
#     txn.put(k.encode(), v)
#     txn.commit()
#
#     # if isinstance(v, bytes):
#     #     # 图片类型为bytes
#     #     txn.put(k.encode(), v)
#     # else:
#     #     # 标签类型为str, 转为bytes
#     #     txn.put(k.encode(), v.encode())  # 编码
#
# env.close()


#### 从lmdb提取图片到文件夹
# def export_images_to_filefolder(db_path, image_out_dir, limit=-1):
#     print('Exporting', db_path, 'to', image_out_dir)
#     env = lmdb.open(db_path, map_size=1073741824,
#                     max_readers=100, readonly=True)
#     if not os.path.exists(image_out_dir):
#         os.makedirs(image_out_dir)
#     count = 0
#     with env.begin(write=False) as txn:
#         cursor = txn.cursor()
#         for key, val in cursor:
#             image_out_path = os.path.join(image_out_dir.encode(), key + '.jpg'.encode())
#             with open(image_out_path, 'wb') as fp:  # 以字节bytes形式写入
#                 fp.write(val)
#             count += 1
#             if count == limit:
#                 break
#             if count % 1000 == 0:
#                 print('Finished', count, 'images')
#
# db_path = './lmdb_image_dir'
# out_dir = './lmdb_image_dir/expanded'
# limit = -1
# export_images_to_filefolder(db_path, out_dir, limit=-1)


# ### 从lmdb提取图像文件到.npy文件
# def export_images_to_npy(db_path, npy_out_dir, resizeW=64, resizeH=64, gray=False, limit=-1):
#     print('Exporting', db_path, 'to', npy_out_dir)
#     env = lmdb.open(db_path, map_size=1099511627776,
#                     max_readers=100, readonly=True)
#     if not os.path.exists(npy_out_dir):
#         os.makedirs(npy_out_dir)
#     imageArr = []
#     with env.begin(write=False) as txn:
#         cursor = txn.cursor()
#         for key, val in cursor:
#             ### use Image to read image data
#             # if gray:
#             #     image = Image.open(io.BytesIO(val)).convert('L')  # 读取二进制图片文件,转为灰度图片
#             # else:
#             #     image = Image.open(io.BytesIO(val)).convert('RGB')  # 读取二进制图片文件，转为彩色图片
#             # # print(key, image.size)
#             # image = image.resize((resizeW, resizeH))
#             # # print(key,image.size)
#             # imData = np.asarray(image)
#
#             ### use cv2 to read image data
#             image_buf = np.frombuffer(val, dtype=np.uint8)
#             # image_buf = np.fromstring(val, dtype=np.uint8)
#             if gray:
#                 image = cv2.imdecode(image_buf, cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE为灰度图
#             else:
#                 image = cv2.imdecode(image_buf, cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR为彩色图
#             imData = cv2.resize(image, (resizeW, resizeH))
#
#             imageArr.append(imData)
#         print("Shape of imageArr: ", np.shape(imageArr))
#         np.save(os.path.join(npy_out_dir, 'imageArr.npy'), imageArr)
#
# db_path = './lmdb_image_dir'
# out_dir = './lmdb_image_dir/npy'
# limit = -1
# export_images_to_npy(db_path, out_dir, resizeW=64, resizeH=64, limit=-1)


### 从.npy文件读取数据
# npy_path='./lmdb_image_dir/npy/imageArr.npy'
# X_train = np.load(npy_path)
# print(X_train.shape)


# ### 存xml标注文件到lmdb
# xml_path = './Annotations'
#
# total_xml = os.listdir(xml_path)
# num = len(total_xml)
# list = range(num)
#
# env = lmdb.open('lmdb_xml_dir', map_size=1073741824)  # size=1GB
# cache = {}  # 存储键值对
#
# for i in list:
#     image_file_path = os.path.join(xml_path, total_xml[i])
#     with open(image_file_path, 'rb') as f:
#         # 读取xml文件的二进制格式数据
#         xml_bin = f.read()
#
#         # 用两个键值对表示一个数据样本
#         cache['{}'.format(total_xml[i][:-4])] = xml_bin
#
# for k, v in cache.items():
#     # with env.begin(write=True) as txn:
#     txn = env.begin(write=True)
#     txn.put(k.encode(), v)
#     txn.commit()
#
#     # if isinstance(v, bytes):
#     #     # 图片类型为bytes
#
#     #     txn.put(k.encode(), v)
#     # else:
#     #     # 标签类型为str, 转为bytes
#     #     txn.put(k.encode(), v.encode())  # 编码
#
# env.close()


# ### 从lmdb提取xml文件到文件夹
# def export_xmls_to_filefolder(db_path, xml_out_dir, limit=-1):
#     print('Exporting', db_path, 'to', xml_out_dir)
#     env = lmdb.open(db_path, map_size=1073741824,
#                     max_readers=100, readonly=True)
#     if not os.path.exists(xml_out_dir):
#         os.makedirs(xml_out_dir)
#     count = 0
#     with env.begin(write=False) as txn:
#         cursor = txn.cursor()
#         for key, val in cursor:
#             xml_out_path = os.path.join(xml_out_dir.encode(), key + '.xml'.encode())
#             with open(xml_out_path, 'wb') as fp:  # 以字节bytes形式写入
#                 fp.write(val)
#             count += 1
#             if count == limit:
#                 break
#             if count % 1000 == 0:
#                 print('Finished', count, 'xmls')
#
# db_path = './lmdb_xml_dir'
# out_dir = './lmdb_xml_dir/expanded'
# limit = -1
# export_xmls_to_filefolder(db_path, out_dir, limit=-1)



