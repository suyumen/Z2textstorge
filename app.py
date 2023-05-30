
from typing import List, Dict, Any
from flask import Flask, request, jsonify, render_template

from crawltitle import crawl_title
from crawlurl import crawl_text
from search_engine import do_search

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index() -> Any:
    return render_template('index.html', results=[])


@app.route('/search')
def search() -> Any:
    query = request.args.get('q', '')
    results = do_search(query, "tf_idf.csv")
    #print(results)
    result_with_text = []
    for result in results:
        text = crawl_text(result)  # 使用爬虫或其他方式获取文本内容
        title = crawl_title(result)  # 使用爬虫或其他方式获取网页标题
        result_with_text.append({'url': result, 'text': text, 'title': title})
    return render_template('index.html', results=result_with_text)


if __name__ == 'main':
    app.run()