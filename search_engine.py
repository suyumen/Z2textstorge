import re


class QueryProcessor:

    def __init__(self, inverted_index):
        self.inverted_index = inverted_index

    def process_query(self, query):
        # 标准化查询，如拆分标点、转换为小写、分词等
        query = query.lower()
        words = re.findall(r'\w+', query)
        # 使用倒排索引查找包含查询词的文档列表
        doc_lists = []
        for word in words:
            if word in self.inverted_index:
                doc_lists.append(self.inverted_index[word])
        # 对文档列表进行合并和排序，得到最终的搜索结果
        result = self.merge_and_sort(doc_lists)
        return result

    def merge_and_sort(self, doc_lists):
        # 合并文档列表
        merged_list = []
        for doc_list in doc_lists:
            merged_list.extend(doc_list)
        # 对文档列表按照TF-IDF值进行排序
        sorted_list = sorted(merged_list, key=lambda x: x[1], reverse=True)
        # 去除重复的文档ID
        result = []
        seen = set()
        for doc_id, tf_idf in sorted_list:
            if doc_id not in seen:
                result.append(doc_id)
                seen.add(doc_id)
        return result
