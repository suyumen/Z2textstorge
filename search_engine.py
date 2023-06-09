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
    results.sort(key=lambda x: x[3], reverse=True)
    print(results)
    res = [result[2] for result in results[:100]]
    print(res)
    return res


def load_index(index_file_path):
    index = {}
    with open(index_file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            word, doc_name, doc_url, tf_idf = row
            tf_idf = float(tf_idf)
            if word not in index:
                index[word] = []
            index[word].append([word, doc_name, doc_url, tf_idf])
    return index

if __name__ == '__main__':
    do_search('小', 'tf_idf.csv')
