from flask import Flask, app, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post1', 
        'content':'This is the content of post1.'
    },
    {
        'title': 'Post2', 
        'content':'This is the content of post2.'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

"""
@app.route('/home/users/<string:name>/posts/<int:id>') #malformed url rule!!
def hello(name,id):
    return "Hello, " + name + " your id is "+ str(id)
"""



# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__。 当模块
# 被直接运行，代码将被运行；当模块被导入时，代码不被运行。
if __name__=="__main__": 
    app.run(debug=True) #you can review your changes immediately
