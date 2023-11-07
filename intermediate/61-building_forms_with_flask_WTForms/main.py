from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms import validators

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = 'some secret string'

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[validators.DataRequired(), validators.Email()], render_kw={'placeholder': 'Enter email'})
    password = PasswordField(label='Password', validators=[validators.DataRequired(), validators.Length(min=8)], render_kw={'placeholder': 'Enter password'})
    submit_btn = SubmitField(label='Log in')


if __name__ == '__main__':
    app.run(debug=True)
