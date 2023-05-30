import requests
from bs4 import BeautifulSoup

def crawl_text(url):
    # 发起HTTP请求获取网页内容
    response = requests.get(url)
    html_content = response.text

    # 使用BeautifulSoup解析HTML结构
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找文本内容（根据实际情况定位所需的标签和属性）
    text_elements = soup.find_all('p')  # 假设文本内容位于<p>标签内
    text = ' '.join(element.get_text() for element in text_elements)

    # 去除HTML标签和多余的空白字符
    text = ' '.join(text.split())

    # 选择前20个字符
    first_20_chars = text[:95]

    return first_20_chars

# 指定要爬取的URL
#url = "http://www.news.cn/globe/2023-05/19/c_1310718845.htm"

# 爬取文本内容并输出结果
#text = crawl_text(url)
#print(text)
