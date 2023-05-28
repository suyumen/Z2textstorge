import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

folder = "txt_files"  # 设置文件夹名称
visited_urls = set()
file_counter = 1 # 文件计数器

def save_text_as_file(url, text, folder):
    global file_counter
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

    # 更新文件计数器
    file_counter += 1

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
        save_text_as_file(url, text, "news_pages")

    # 提取当前网页中的其他 URL
    urls = soup.find_all('a', href=True)
    for link in urls:
        # 构建绝对路径的 URL
        absolute_url = urljoin(url, link['href'])

        # 确保只爬取当前网站的 URL，并且没有被访问过
        if absolute_url.startswith("http://www.xinhuanet.com") and absolute_url not in visited_urls:
            visited_urls.add(absolute_url)
            scrape_jump_pages(absolute_url)

# 创建保存页面的目录
os.makedirs("news_pages", exist_ok=True)

# 爬取跳转子页面并保存内容
scrape_jump_pages("http://www.xinhuanet.com")
