from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, validators, FloatField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret'
all_books = []
bootstrap4 = Bootstrap4(app)


class BookForm(FlaskForm):
    title = StringField(label='Book Name', validators=[validators.DataRequired()])
    author = StringField(label='Book Author', validators=[validators.DataRequired()])
    rating = FloatField(label='Rating', validators=[validators.DataRequired()])
    submit = SubmitField(label='Add Book')


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        all_books.append({
            'title': book_form.title.data,
            'author': book_form.author.data,
            'rating': book_form.rating.data
        })
        print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html', book_form=book_form)


if __name__ == "__main__":
    app.run(debug=True)
