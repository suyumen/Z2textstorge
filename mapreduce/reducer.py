#!/usr/bin/env python
# coding:utf-8
import sys
import csv

# 记录每个单词在具体文件中的出现次数
word_doc_count = {}

# 记录每个文件中的单词总数
doc_total_words = {}

# 读取之前的倒排索引文件
with open('index.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    inverted_index = [row for row in reader]

for line in sys.stdin:
    doc_info, count = line.strip().rsplit(':', 1)
    word, doc_name = doc_info.split('\t', 1)
    count = int(count)

    # 统计每个单词在不同文件中的出现次数
    if word not in word_doc_count:
        word_doc_count[word] = {}
    word_doc_count[word][doc_name] = count

    # 统计每个文件的总单词数
    if doc_name not in doc_total_words:
        doc_total_words[doc_name] = 0
    doc_total_words[doc_name] += count

# 更新倒排索引并将结果输出到csv文件中
with open('index.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    for word, doc_count in word_doc_count.items():
        for doc_name, count in doc_count.items():
            # 在之前的倒排索引中查找该单词是否已经出现过
            index = -1
            for i, row in enumerate(inverted_index):
                if row[0] == word and row[1] == doc_name:
                    index = i
                    break
            # 如果单词已经在该文件中出现过，则更新出现次数
            if index != -1:
                inverted_index[index][2] = int(inverted_index[index][2]) + count
            # 如果单词没有在该文件中出现过，则添加新的倒排索引项
            else:
                inverted_index.append([word, doc_name, count])
    # 将更新后的倒排索引写入文件
    for row in inverted_index:
        writer.writerow(row)

with open('tf_idf.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'doc_name', 'doc_url', 'tf_idf'])
        for word, doc_count in word_doc_count.items():
            for doc_name, count in doc_count.items():
                tf = count / doc_total_words[doc_name]
                idf = len(doc_total_words) / len(doc_count.keys())
                tf_idf = tf * idf
                doc_id, doc_url = doc_name.split('\t')
                writer.writerow([word, doc_id, doc_url, tf_idf])