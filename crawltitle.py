import requests
from bs4 import BeautifulSoup

def crawl_title(url: str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else ''
        return title
    except requests.exceptions.RequestException:
        return ''

# 示例用法
#url = 'http://www.news.cn/globe/2023-05/19/c_1310718845.htm'
#title = crawl_title(url)
#print(title)