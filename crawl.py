import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

folder = "txt_files"  # 设置文件夹名称
visited_urls = set()

def save_text_as_file(url, text, folder):
    # 创建保存文件的文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 从 URL 中提取有效的文件名
    filename = url.replace("http://", "")
    # 替换文件名中的特殊字符
    valid_chars = "-_.()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    filename = "".join(c if c in valid_chars else "_" for c in filename)
    # 添加扩展名
    filename += ".txt"

    # 构造完整的文件路径
    filepath = os.path.join(folder, filename)

    # 保存文本内容到文件
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"已保存文件：{filepath}")

def scrape_jump_pages(url):
    # 发起 HTTP 请求获取网页内容
    response = requests.get(url)
    response.encoding = "utf-8"
    html_content = response.text

    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取当前网页的 URL
    print("当前网页：", url)

    # 提取文本信息
    text = soup.get_text()

    print(text)

    # 提取当前网页中的其他 URL
    urls = soup.find_all('a', href=True)
    for link in urls:
        # 构建绝对路径的 URL
        absolute_url = urljoin(url, link['href'])

        # 确保只爬取当前网站的 URL，并且没有被访问过
        if absolute_url.startswith("http://www.xinhuanet.com") and absolute_url not in visited_urls:
            visited_urls.add(absolute_url)
            save_text_as_file(absolute_url, text,"news_pages")
            scrape_jump_pages(absolute_url)


# 创建保存页面的目录
os.makedirs("news_pages", exist_ok=True)

# 爬取跳转子页面并保存内容
scrape_jump_pages("http://www.xinhuanet.com")
