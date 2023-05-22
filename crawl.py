import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import string
# 用于存储已经访问过的 URL，避免重复爬取
from nltk import word_tokenize
from nltk.corpus import stopwords

visited_urls = set()
result_file_name = 'result.txt'

def crawl(url):
    # 发起 HTTP 请求获取网页内容
    response = requests.get(url)
    response.encoding = "utf-8"
    html_content = response.text

    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(html_content, 'html.parser')

    f = open(result_file_name, 'a', encoding='utf-8')
    # 提取当前网页的 URL
    print("当前网页：", url)
    f.write("当前网页 "+url+" ")

    # 提取文本信息
    text = soup.get_text()

    # 标准化处理文本
    # 去除标点符号
    #text = text.translate(str.maketrans("", "", string.punctuation))
    # 转换为小写
    #text = text.lower()
    # 分词
    #tokens = word_tokenize(text)

    # 去除停用词
    #stop_words = set(stopwords.words('english'))  # 停用词表rd
    #filtered_tokens = [token for token in tokens if token not in stop_words]

    # 输出处理后的文本数据
    #print(filtered_tokens)
    #f.writelines(filtered_tokens)
    print(text)
    f.writelines(text)
    f.write("\n")
    f.flush()

    # 提取当前网页中的其他 URL
    urls = soup.find_all('a', href=True)
    for link in urls:
        # 构建绝对路径的 URL
        absolute_url = urljoin(url, link['href'])

        # 确保只爬取当前网站的 URL，并且没有被访问过
        if absolute_url.startswith("http://www.xinhuanet.com") and absolute_url not in visited_urls:
            visited_urls.add(absolute_url)
            crawl(absolute_url)
    f.close()

# 设置起始 URL
start_url = "http://www.xinhuanet.com"
crawl(start_url)