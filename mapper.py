import jieba
import nltk

# 英文分词器
en_tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

def map_fn(_, line):
    # 标准化处理
    # 拆分标点
    line = line.translate(str.maketrans('', '', string.punctuation))
    # 转小写
    line = line.lower()
    # 中文分词
    words = jieba.lcut(line)
    # 英文分词
    en_words = en_tokenizer.tokenize(line)
    words.extend(en_words)
    # 输出键值对
    for word in set(words):
        yield (word, (doc_id, words.count(word)))
