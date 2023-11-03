import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    blog_data_response = requests.get(url='https://api.npoint.io/ae124e0a00e39c2791f2')
    blog_data = blog_data_response.json()
    context = {
        'blog_data': blog_data,
    }
    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
