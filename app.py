
from typing import List, Dict, Any
from flask import Flask, request, jsonify, render_template
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
    return render_template('index.html', results=results)

if __name__ == 'main':
    app.run()