from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length ,AnyOf
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required'), Length(min=5, max=15, message='Must be between 5 and 15')])
    password = PasswordField('Password', validators=[InputRequired('A username is required'), AnyOf(values=['password', 'secret'])])
    submit = SubmitField('Sign In')
    