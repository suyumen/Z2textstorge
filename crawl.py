import requests
from bs4 import BeautifulSoup
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def crawl_and_process_text():
    # 发送GET请求获取网页内容
    url = 'http://www.bupt.edu.cn'
    response = requests.get(url)
    response.encoding = "utf-8"
    
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取需要的文本信息
    text = soup.get_text()
    
    # 标准化处理文本
    # 去除标点符号
    text = text.translate(str.maketrans("", "", string.punctuation))
    # 转换为小写
    text = text.lower()
    # 分词
    tokens = word_tokenize(text)
    
    # 去除停用词
    stop_words = set(stopwords.words('english'))  # 停用词表
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # 输出处理后的文本数据
    print(filtered_tokens)

# 执行爬虫和文本处理
crawl_and_process_text()
