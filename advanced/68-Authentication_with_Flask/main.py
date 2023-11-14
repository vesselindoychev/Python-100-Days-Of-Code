import json
import os.path

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session, current_app
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

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    authenticated = db.Column(db.Boolean, default=False)

    def is_authenticated(self):
        return self.authenticated


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


class LoginForm(FlaskForm):
    email = fields.EmailField(validators=[validators.DataRequired(), validators.Email()],
                              render_kw={'placeholder': 'Email'})
    password = fields.PasswordField(validators=[validators.DataRequired()], render_kw={'placeholder': 'Password'})
    submit = fields.SubmitField('Log in')


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

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            return render_template('register.html', form=form, is_existing=True)

        hashed_password = generate_password_hash(password, salt_length=16)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('secrets'))
        # data = json.dumps({'name': new_user.name})
        # session['data'] = data
        # return redirect(url_for('secrets', data=data))

    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            if check_password_hash(user.password, password):
                user.authenticated = True
                db.session.commit()
                login_user(user)
                return redirect(url_for('secrets'))
    return render_template("login.html", form=form)


@app.route('/secrets')
@login_required
def secrets():
    # data = request.args['data']
    # data = session['data']
    # name = json.loads(data)['name']
    # print(name)
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    pass


@app.route('/download', methods=['GET', 'POST'])
@login_required
def download():
    path = 'files/cheat_sheet.pdf'
    return send_from_directory('static', as_attachment=True, path=path)


if __name__ == "__main__":
    app.run(debug=True)
