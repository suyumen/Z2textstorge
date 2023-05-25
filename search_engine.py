import jieba
import csv


def do_search(sent, index_file_path):
    # 分词
    words = jieba.lcut(sent)
    # 加载倒排索引表
    index = load_index(index_file_path)
    # 找到所有包含搜索参数的条目
    results = []
    for word in words:
        if word in index:
            results.extend(index[word])
    # 按tf-idf值从高到低排序
    results.sort(key=lambda x: x[2], reverse=True)
    res = [result[1][:-4] for result in results[:100]]
    re = ["http://"+re.replace('_', '/') for re in res]
    
    print(re)
    return re


def load_index(index_file_path):
    index = {}
    with open(index_file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            word, doc_name, tf_idf = row
            tf_idf = float(tf_idf)
            if word not in index:
                index[word] = []
            index[word].append([word, doc_name, tf_idf])
    return index

# if __name__ == '__main__':
#     search('安徽', 'tf_idf.csv')
