import math
from typing import List, Tuple

def reduce_fn(key: str, values: List[Tuple[int, int]], N: int) -> Tuple[str, Tuple[int, float]]:
    # 计算tf
    max_tf = max(values, key=lambda x: x[1])[1]
    tf = [(doc_id, tf / max_tf) for doc_id, tf in values]
    # 计算idf
    df = len(tf)
    idf = math.log(N / df)
    # 计算tf-idf
    tf_idf = [(doc_id, tf * idf) for doc_id, tf in tf]
    # 生成倒排索引表
    return (key, tuple(tf_idf))
