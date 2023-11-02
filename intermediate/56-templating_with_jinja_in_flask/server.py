import datetime
import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    context = {
        'random_number': random_number,
        'year': current_year,
    }
    return render_template('index.html', **context)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response2 = requests.get(url=f"https://api.agify.io?name={name}")

    data = response.json()
    data2 = response2.json()

    name = data['name'].title()
    gender = data['gender']
    years = data2['age']

    context = {
        'name': name,
        'gender': gender,
        'years': years,
    }

    return render_template('dashboard.html', **context)


@app.route('/blog')
def blog():
    response = requests.get(url='https://api.npoint.io/ae124e0a00e39c2791f2')
    posts = response.json()
    context = {
        'posts': posts,
    }
    return render_template('blog.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
