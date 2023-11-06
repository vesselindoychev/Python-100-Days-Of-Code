import requests
from post import Post
from flask import Flask, render_template

blog_data_response = requests.get(url='https://api.npoint.io/eb6cd8a5d783f501ee7d')
blog_data = blog_data_response.json()

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'blogs': blog_data,
    }
    return render_template("index.html", **context)


@app.route('/post/<int:id>')
def show_blog_data(id):
    current_blog = None
    for blog in blog_data:
        if blog['id'] == id:
            current_blog = blog
    context = {
        'blog': current_blog
    }
    return render_template('post.html', **context)


@app.route('/about')
def show_about_page():
    return render_template('about.html')


@app.route('/contact')
def show_contact_page():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
