#!/usr/bin/env python
# coding:utf-8
import os

def print_files_in_folder(folder):
    # 获取目标文件夹下所有文件的路径
    file_paths = [os.path.join(folder, file) for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]

    # 打印文件路径
    for file_path in file_paths:
        print(file_path)

# 示例用法
folder = "C:/Users/zhang'yue'ying/Z2textstorge/news_pages"  # 设置文件夹名称

print_files_in_folder(folder)
