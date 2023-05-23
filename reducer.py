#!/usr/bin/env python
# coding:utf-8
import sys
import csv

#记录每个单词在具体文件中的出现次数
word_doc_count = {}

#记录每个文件中的单词总数
doc_total_words = {}

for line in sys.stdin:
    # 获取输出结果中的单词和文件名
    word, file_info = line.strip().split('\t')
    # 获取文件名和单词在文件中的出现次数
    doc_name, count = file_info.split(':')
    count = int(count)

    # 统计每个单词在不同文件中的出现次数
    if word not in word_doc_count:
        word_doc_count[word] = {}
    word_doc_count[word][doc_name] = count

    # 统计每个文件的总单词数
    if doc_name not in doc_total_words:
        doc_total_words[doc_name] = 0
    doc_total_words[doc_name] += count
    #计算每个单词在不同文件中的tf-idf值，并将结果输出到csv文件中
    with open('tf_idf.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'doc_name', 'tf_idf'])
        for word, doc_count in word_doc_count.items():
            for doc_name, count in doc_count.items():
                tf = count / doc_total_words[doc_name]
                idf = len(doc_total_words) / len(doc_count.keys())
                tf_idf = tf * idf
                writer.writerow([word, doc_name, tf_idf])
