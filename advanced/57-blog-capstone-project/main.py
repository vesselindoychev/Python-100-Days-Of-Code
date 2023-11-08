import os
import smtplib
from dotenv import load_dotenv
import requests
from post import Post
from flask import Flask, render_template, request

load_dotenv(verbose=True)

blog_data_response = requests.get(url='https://api.npoint.io/eb6cd8a5d783f501ee7d')
blog_data = blog_data_response.json()

RECEIVER_EMAIL = os.environ['RECEICER_EMAIL']
PASSWORD = os.environ['PASSWORD']

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'blogs': blog_data,
    }
    return render_template("index.html", **context)


@app.route('/post/<int:id>')
def show_blog_data(id):
    current_blog = None
    for blog in blog_data:
        if blog['id'] == id:
            current_blog = blog
    context = {
        'blog': current_blog
    }
    return render_template('post.html', **context)


@app.route('/about')
def show_about_page():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def show_contact_page():
    if request.method == 'POST':
        full_name = request.form.get('full-name')
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
    app.run(debug=True)
