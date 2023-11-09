from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, validators
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.sqlite3'

bootstrap5 = Bootstrap5(app)

db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(25), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class EditMovieRatingForm(FlaskForm):
    rating = FloatField(label='Your rating Out of 10 e.g 7.5', validators=[validators.DataRequired()])
    review = StringField(label='Your Review', validators=[validators.DataRequired()])
    submit = SubmitField(label='Done')


@app.route("/")
def home():
    with app.app_context():
        all_movies = db.session.query(Movie).order_by(Movie.ranking.desc()).all()
    return render_template("index.html", movies=all_movies)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    form = EditMovieRatingForm()
    current_movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()

    if form.validate_on_submit():
        if request.method == 'POST':
            current_movie.rating = form.rating.data
            current_movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('edit.html', form=form, movie=current_movie)


@app.route('/delete-movie/<int:id>')
def delete_movie(id):
    current_movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    db.session.delete(current_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
