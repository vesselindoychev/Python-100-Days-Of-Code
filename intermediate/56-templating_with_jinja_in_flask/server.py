import datetime
import random

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


if __name__ == '__main__':
    app.run(debug=True)
