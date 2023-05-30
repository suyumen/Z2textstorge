#!/usr/bin/env python
# coding:utf-8
import os

# 获取当前文件夹路径
dir_path = "new_pages"

# 获取当前文件夹下所有文件名
file_names = os.listdir(dir_path)

# 打印所有文件名
for name in file_names:
    print("C:/Users/zhongyl1/Desktop/Z2textstorge/Z2textstorge/new_pages/"+name)