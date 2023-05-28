#!/usr/bin/env python
# coding:utf-8
import os

# 获取当前文件夹路径
dir_path = "news_pages"

# 获取当前文件夹下所有文件名
file_names = os.listdir(dir_path)

# 打印所有文件名
for name in file_names:
    print("C:/Users/zhang'yue'ying/Z2textstorge/news_pages/"+name)