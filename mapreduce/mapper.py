#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import jieba

# 加载停用词表
stop_words = set()
with open(os.path.join(os.path.dirname(__file__), "new_stopwords.txt"), "r", encoding="utf-8") as f:
    for line in f:
        stop_words.add(line.strip())

for line in sys.stdin:
    # 获取url和文本
    file_id,url,text = line.strip().split("\t")
    text = text.strip()  # 去首尾空格
    text = ''.join(filter(lambda x: x >= u'\u4e00' and x <= u'\u9fa5', text))  # 去除非中文字符    
    # 对文本进行分词、标准化、统计词频
    words = jieba.lcut(text)
    words = [word for word in words if word not in stop_words]
    # 统计单词出现次数
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print(f'{word}\t{file_id}\t{url}:{count}')