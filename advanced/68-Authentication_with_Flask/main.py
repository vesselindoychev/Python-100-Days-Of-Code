import json

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import fields, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


class RegistrationForm(FlaskForm):
    name = fields.StringField(validators=[validators.DataRequired(), validators.Length(min=3, max=20)],
                              render_kw={'placeholder': 'Name'})
    email = fields.EmailField(validators=[validators.DataRequired(), validators.Email()],
                              render_kw={'placeholder': 'Email'})
    password = fields.PasswordField(validators=[validators.DataRequired(), validators.Length(min=5)],
                                    render_kw={'placeholder': 'Password'})
    confirm_password = fields.PasswordField(validators=[validators.DataRequired(), validators.EqualTo('password')],
                                            render_kw={'placeholder': 'Confirm Password'})
    submit = fields.SubmitField('Sign up')

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        new_user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        data = json.dumps({'user_name': new_user.name})
        session['data'] = data
        return redirect(url_for('secrets', data=data))
    return render_template("register.html", form=form)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    data = request.args['data']
    data = session['data']
    user_name = json.loads(data)
    name = user_name['user_name']
    print(name)
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
