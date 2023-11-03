import requests
from post import Post
from flask import Flask, render_template

blog_data_response = requests.get(url='https://api.npoint.io/ae124e0a00e39c2791f2')
blog_data = blog_data_response.json()

blog_objects = []

for blog in blog_data:
    blog_obj = Post(blog['id'], blog['title'], blog['subtitle'], blog['body'])
    blog_objects.append(blog_obj)

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'blogs': blog_objects,
    }
    return render_template("index.html", **context)


@app.route('/post/<int:id>')
def show_blog_data(id):
    current_blog = None
    for blog in blog_objects:
        if blog.id == id:
            current_blog = blog
    context = {
        'blog': current_blog
    }
    return render_template('post.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
