from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import fields, validators


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
