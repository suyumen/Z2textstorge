from flask import Flask,request,render_template # request是请求前端数据相关的包，render_template是路由映射相关的包

app = Flask(__name__,template_folder='./templates')

@app.route("/search",methods=["POST","GET"])         # 设置访问的域名，默认5000端口的化，访问检索页面就是127.0.0.1:5000/search
def search():
    if request.args.get('key_word',None) == None:    # 如果没有检测到关键字提交，就停留在检索页面
        print("未传参")
        return render_template("Search.html")        # 映射到检索页面
    else:                                            # 如果有关键词提交
        key_words = request.args.get('key_word')     # 将传来的关键词赋给key_word
        


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
