import random

from flask import Flask

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def play_game():
    return '<h1>Guess a number between 0 and 9</>' \
           '<p><iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC"></a></p></>'


@app.route('/<int:number>')
def guess_the_number(number):
    if number < random_number:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               '<iframe src="https://giphy.com/embed/jD4DwBtqPXRXa" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/work-digging-jD4DwBtqPXRXa">via GIPHY</a></p>'
    if number > random_number:
        return '<h1 style="color: purple;">Too high, try again!</h1>' \
               '<iframe allow="fullscreen" frameBorder="0" height="853" src="https://giphy.com/embed/3z1q2o94CELGbMPBzm/video" width="480"></iframe>'
    return '<h1 style="color: green;">You found me!</h1>' \
           '<iframe src="https://giphy.com/embed/Y4pAQv58ETJgRwoLxj" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dog-eyebleach-im-flying-Y4pAQv58ETJgRwoLxj">via GIPHY</a></p>'


if __name__ == '__main__':
    app.run(debug=True)
