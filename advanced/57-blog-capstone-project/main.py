import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, fields, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
Bootstrap5(app)

ckeditor = CKEditor(app)
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class CreateNewPost(FlaskForm):
    title = fields.StringField(label='Blog Post Title', validators=[validators.DataRequired()])
    subtitle = fields.StringField(label='Subtitle', validators=[validators.DataRequired()])
    author = fields.StringField(label='Your Name', validators=[validators.DataRequired()])
    image_url = fields.URLField(label='Blog Image URL', validators=[validators.DataRequired(), validators.URL()])
    body = CKEditorField(label='Blog Content', validators=[validators.DataRequired()])
    submit = fields.SubmitField(label='Submit Post')


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/view-post/<int:post_id>')
def show_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def create_new_post():
    form = CreateNewPost()
    if request.method == 'POST':
        if form.validate_on_submit():
            with app.app_context():
                today = datetime.datetime.now()
                month = today.strftime('%B')
                year = today.year
                day = today.day
                new_post = BlogPost(title=form.title.data,
                                    subtitle=form.subtitle.data,
                                    date=f"{month} {day}, {year}",
                                    body=form.body.data,
                                    author=form.author.data,
                                    img_url=form.image_url.data)
                db.session.add(new_post)
                db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
