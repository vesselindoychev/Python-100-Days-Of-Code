from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, validators, FloatField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.sqlite3'

# all_books = []
bootstrap4 = Bootstrap4(app)

db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


class BookForm(FlaskForm):
    title = StringField(label='Book Name', validators=[validators.DataRequired()])
    author = StringField(label='Book Author', validators=[validators.DataRequired()])
    rating = FloatField(label='Rating', validators=[validators.DataRequired()])
    submit = SubmitField(label='Add Book')


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        # all_books.append({
        #     'title': book_form.title.data,
        #     'author': book_form.author.data,
        #     'rating': book_form.rating.data
        # })
        # print(all_books)
        with app.app_context():
            new_book = Book(title=book_form.title.data, author=book_form.author.data, rating=book_form.rating.data)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', book_form=book_form)


if __name__ == "__main__":
    app.run(debug=True)
