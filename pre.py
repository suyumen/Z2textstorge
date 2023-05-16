from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import math

WORD_RE = re.compile(r"\w+")

class MRWordFrequency(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_tfidf)
        ]

    def mapper(self, _, line):
        # 提取文档ID
        doc_id = re.findall(r"bupt\.txt\w*", line)[0]

        # 提取单词
        for word in WORD_RE.findall(line):
            yield word.lower(), (doc_id, 1)

    def reducer(self, word, doc_counts):
        # 计算单词在每个文档中的出现次数
        doc_word_counts = {}
        for doc_id, count in doc_counts:
            if doc_id in doc_word_counts:
                doc_word_counts[doc_id] += count
            else:
                doc_word_counts[doc_id] = count

        # 输出键值对，其中键是单词，值是包含该单词的文档信息
        for doc_id, count in doc_word_counts.items():
            yield word, (doc_id, count)

    def reducer_tfidf(self, word, doc_counts):
        # 计算单词在所有文档中的出现次数
        total_docs = 0
        doc_word_counts = {}
        for doc_id, count in doc_counts:
            total_docs += 1
            doc_word_counts[doc_id] = count

        # 计算单词的逆文档频率
        idf = math.log(total_docs / (len(doc_word_counts) + 1))

        # 计算单词在每个文档中的词频-逆文档频率值
        for doc_id, count in doc_word_counts.items():
            tf = count
            tfidf = tf * idf
            yield word, (doc_id, tfidf)

if __name__ == '__main__':
    MRWordFrequency.run()
