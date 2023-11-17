import datetime
import smtplib
from functools import wraps

import werkzeug

from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap5
from flask_gravatar import Gravatar
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import fields, validators
from flask_ckeditor import CKEditor, CKEditorField
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
ckeditor = CKEditor(app)
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']
PASSWORD = os.environ['PASSWORD']


@login_manager.user_loader
def user_loader(user_id):
    return db.get_or_404(User, user_id)
    # return User


# CONFIGURE TABLE
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = relationship('BlogPost', back_populates='author')
    user_comments = relationship('Comment', back_populates='creator')


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author = relationship('User', back_populates='posts')
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_comments = relationship('Comment', back_populates='post')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = relationship('User', back_populates='user_comments')
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    post = relationship('BlogPost', back_populates='post_comments')


"""
CHANGE NAMES
"""

with app.app_context():
    db.create_all()


class RegistrationForm(FlaskForm):
    first_name = fields.StringField(label='First Name',
                                    validators=[validators.DataRequired(), validators.Length(min=3)],
                                    render_kw={'placeholder': 'Ivan'})
    last_name = fields.StringField(label='Last Name', validators=[validators.DataRequired(), validators.Length(min=3)],
                                   render_kw={'placeholder': 'Petrov'})
    email = fields.EmailField(label='Email', validators=[validators.DataRequired(), validators.Email()],
                              render_kw={'placeholder': 'ivan123@gmail.com'})
    password = fields.PasswordField(label='Password', validators=[validators.DataRequired(), validators.Length(min=5)],
                                    render_kw={'placeholder': f'{5 * "*"}'})
    confirm_password = fields.PasswordField(label='Confirm Password',
                                            validators=[validators.DataRequired(), validators.EqualTo('password')],
                                            render_kw={'placeholder': f'Retype your password'})
    submit = fields.SubmitField(label='Sign up')


class LoginForm(FlaskForm):
    email = fields.EmailField(label='Email', validators=[validators.DataRequired(), validators.Email()],
                              render_kw={'placeholder': 'ivan123@gmail.com'})
    password = fields.PasswordField(label='Password', validators=[validators.DataRequired()],
                                    render_kw={'placeholder': f"{20 * '*'}"})
    submit = fields.SubmitField(label='Login')


class CreateNewPost(FlaskForm):
    title = fields.StringField(label='Blog Post Title', validators=[validators.DataRequired()])
    subtitle = fields.StringField(label='Subtitle', validators=[validators.DataRequired()])
    # author = fields.StringField(label='Your Name', validators=[validators.DataRequired()])
    img_url = fields.URLField(label='Blog Image URL', validators=[validators.DataRequired(), validators.URL()])
    body = CKEditorField(label='Blog Content', validators=[validators.DataRequired()])
    submit = fields.SubmitField(label='Submit Post')


class CreateCommentForm(FlaskForm):
    body = CKEditorField(label='Comment')
    submit = fields.SubmitField('Submit Comment')


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            flash('This email already exists. Please try with another email.')
            return render_template('register.html', form=form)

        hashed_password = generate_password_hash(password, salt_length=16)

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
            flash('Incorrect password, please try again.')
            return render_template('login.html', form=form)
        flash('User with this email does noy exist.')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/view-post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    is_commented = False
    # requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    comment_form = CreateCommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    current_comments_for_post = db.session.execute(
        db.select(Comment).where(Comment.post_id == requested_post.id)).scalars()
    current_comments = requested_post.post_comments
    for comment in current_comments:
        if comment.creator_id == current_user.id:
            is_commented = True

    gravatar = Gravatar(app, size=30, rating='g', default='retro', force_default=False, force_lower=False,
                        use_ssl=False, base_url=None)
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comment(
                body=comment_form.body.data,
                creator=current_user,
                post_id=requested_post.id
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
    return render_template("post.html", post=requested_post, form=comment_form, current_user=current_user,
                           comments=current_comments, gravatar=gravatar, is_commented=is_commented)


def admin_only(f):
    @wraps(f)
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.id != 2:
            return abort(403)
        return f(*args, **kwargs)

    return wrapper


@app.route('/new-post', methods=['GET', 'POST'])
@admin_only
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
                                    author=current_user,
                                    img_url=form.img_url.data)
                db.session.add(new_post)
                db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
    today = datetime.datetime.now()
    month = today.strftime('%B')
    year = today.year
    day = today.day
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = CreateNewPost(
        title=post.title,
        subtitle=post.subtitle,
        author=current_user,
        img_url=post.img_url,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.date = f"{month} {day}, {year}"
        post.body = form.body.data
        # post.author = form.author.data
        post.img_url = form.img_url.data

        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', form=form, is_edit=True)


@app.route('/delete/<int:post_id>')
@admin_only
def delete_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# @app.route('/new-post', methods=['GET', 'POST'])
# def create_comment():
#     comment_form = CreateCommentForm()


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        full_name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone-number')
        message = request.form.get('message')

        print(f'Full Name: {full_name}, \n'
              f'Email: {email},\n'
              f'Phone: {phone},\n'
              f'Message: {message}')

        context = {
            'msg_sent': True,
            'msg': 'Successfully sent your message.'
        }

        send_email(email, message, full_name)
        return render_template('contact.html', **context)
    context = {
        'msg_sent': False
    }

    return render_template('contact.html', **context)


def send_email(sender_mail, text, name):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=RECEIVER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=RECEIVER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f'Subject:Sent message by email: {sender_mail}\n\nName:{name}\n{text}'
        )


@app.route('/secrets')
@login_required
def secrets():
    return render_template('secrets.html', name=f"{current_user.first_name} {current_user.last_name}")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
