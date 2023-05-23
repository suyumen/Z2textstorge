#!/usr/bin/env python
# coding:utf-8

import sys
import jieba

def read_file(file_path):
    """读取文件内容并将文件内容标准化处理"""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.strip()  # 去首尾空格
        text = text.lower()  # 转换为小写
        text = ''.join(filter(lambda x: x >= u'\u4e00' and x <= u'\u9fa5', text))  # 去除非中文字符
        return text


def mapper():
    for line in sys.stdin:
        file_path = line.strip()
        file_name = file_path.split('/')[-1].split('.')[0]  # 获取文件名
        text = read_file(file_path)  # 读取文件内容并进行标准化处理

        # 对文本进行分词，得到词汇列表
        words = jieba.lcut(text)
        # 统计单词出现次数
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        # 输出每个单词及其出现次数，key为单词，value为包含文件名和出现次数的字典
        for word, count in word_count.items():
            print(f'{word}\t{file_name}:{count}')


if __name__ == '__main__':
    mapper()
