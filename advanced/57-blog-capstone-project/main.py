import datetime
import smtplib

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import fields, validators
from flask_ckeditor import CKEditor, CKEditorField
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
Bootstrap5(app)

ckeditor = CKEditor(app)
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']
PASSWORD = os.environ['PASSWORD']

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
    img_url = fields.URLField(label='Blog Image URL', validators=[validators.DataRequired(), validators.URL()])
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
                                    img_url=form.img_url.data)
                db.session.add(new_post)
                db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    today = datetime.datetime.now()
    month = today.strftime('%B')
    year = today.year
    day = today.day
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = CreateNewPost(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.date = f"{month} {day}, {year}"
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data

        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', form=form, is_edit=True)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


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


if __name__ == "__main__":
    app.run(debug=True, port=5003)
