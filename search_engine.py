def search(query: str, inverted_index: Dict[str, List[Tuple[int, float]]], N: int) -> List[Tuple[int, float]]:
    # 对查询字符串进行标准化处理
    words = standardize_query(query)
    # 计算查询向量
    q_tf_idf = {}
    for word in words:
        if word in inverted_index:
            idf = math.log(N / len(inverted_index[word]))
            q_tf_idf[word] = 1 * idf
    # 计算余弦相似度
    scores = {}
    for word, tf_idf in q_tf_idf.items():
        for doc_id, doc_tf_idf in inverted_index[word]:
            if doc_id not in scores:
                scores[doc_id] = 0.0
            scores[doc_id] += tf_idf * doc_tf_idf
    # 排序
    sorted_scores = [(k, v) for k, v in scores.items()]
    sorted_scores.sort(key=lambda x: x[1], reverse=True)
    # 返回结果
    return sorted_scores
