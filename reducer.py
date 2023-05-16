import sys
from collections import defaultdict


def main():
    # 初始化倒排索引表
    inverted_index = defaultdict(list)

    # 读取mapper输出的结果，并将相同单词的tf-idf值放在一起
    for line in sys.stdin:
        # 获取单词、文件名和tfidf值
        word, filename, tfidf = line.strip().split("\t")

        # 将tfidf值和文件名拼接成字符串
        document_tf = "{}:{}".format(filename, tfidf)

        # 向倒排索引表中添加单词及其tfidf值
        inverted_index[word].append(document_tf)

    # 输出倒排索引表
    for word, documents in inverted_index.items():
        print("{}\t{}".format(word, ", ".join(documents)))


if __name__ == "__main__":
    main()
