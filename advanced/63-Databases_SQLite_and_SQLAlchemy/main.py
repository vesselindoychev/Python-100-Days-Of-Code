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


class EditBookRatingForm(FlaskForm):
    new_rating = FloatField(label='New Rating', validators=[validators.DataRequired()])
    submit = SubmitField(label='Change Rating')


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        with app.app_context():
            new_book = Book(title=book_form.title.data, author=book_form.author.data, rating=book_form.rating.data)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', book_form=book_form)


@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    edit_form = EditBookRatingForm()
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    print(book)
    if request.method == 'POST':
        book.rating = edit_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit-rating.html', book=book, edit_form=edit_form)


@app.route('/delete/<int:id>')
def delete_book(id):
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
