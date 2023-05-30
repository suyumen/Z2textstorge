import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

folder = "news_pages"  # 设置文件夹名称
visited_urls = set()

# 读取已爬取的URL记录
visited_file = "visited_urls.txt"
if os.path.exists(visited_file):
    with open(visited_file, "r") as f:
        visited_urls = set(f.read().splitlines())

def get_last_file_counter(folder):
    files = os.listdir(folder)
    if files:
        last_file = max(files, key=lambda f: int(os.path.splitext(f)[0]))
        last_counter = int(os.path.splitext(last_file)[0])
        return last_counter
    else:
        return 0

def save_text_as_file(url, text, folder):
    file_counter = get_last_file_counter(folder) + 1  # 从最后一个文件的计数器值加1开始命名

    # 创建保存文件的文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = str(file_counter) + ".txt"

    # 构造完整的文件路径
    filepath = os.path.join(folder, filename)

    # 保存文本内容到文件
    with open(filepath, "w", encoding="utf-8") as file:
        # 写入URL到第一行
        file.write(url + "\n")
        # 写入文本内容从第二行开始
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

    # 过滤不存在的页面和包含"index.html"的页面
    if "您要访问的页面不存在" in text or "index.html" in url:
        print("该页面不存在或为索引页面，跳过保存")
    else:
        save_text_as_file(url, text, folder)

    # 提取当前网页中的其他 URL
    urls = soup.find_all('a', href=True)
    for link in urls:
        # 构建绝对路径的 URL
        absolute_url = urljoin(url, link['href'])

        # 确保只爬取当前网站的 URL，并且没有被访问过
        if absolute_url.startswith("http://www.xinhuanet.com") and absolute_url not in visited_urls:
            visited_urls.add(absolute_url)
            scrape_jump_pages(absolute_url)

# 爬取跳转子页面并保存内容
scrape_jump_pages("http://www.xinhuanet.com")

# 保存已爬取的URL记录
with open(visited_file, "w") as f:
    f.write("\n".join(visited_urls))