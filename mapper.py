import jieba
import nltk

# 英文分词器
en_tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

def map_fn(_, line):
    # 标准化处理
    words = jieba.lcut(line)
    # 将标点符号和空格过滤掉
    words = [word.lower() for word in words if (word.isalnum() and not word.isspace())]
    for word in set(words):
        yield (word, (doc_id, words.count(word)))
