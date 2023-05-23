from flask import Flask, render_template, request
from search_engine import QueryProcessor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = search_engine.search(query)
        return render_template('results.html', results=results)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
