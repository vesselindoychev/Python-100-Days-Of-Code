from flask import Flask
from decorators import make_bold, make_italic, make_underlined

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center; font-weight: 22px; color: red">Hello, World</>' \
           '<p style="color: black">Text paragraph</>' \
           '<div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="250" src="https://giphy.com/embed/cwQCUhKible5mGrtMO/video" width="480"></iframe></div>'


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def say_bye():
    return 'Bye'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello, {name}, you are {number} years old"


if __name__ == '__main__':
    app.run(debug=True)
