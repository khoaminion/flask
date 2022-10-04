from ast import Pass
import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired

class SignUpForm(FlaskForm):
    inputFirstName = StringField('First Name', [DataRequired(message="Please enter your first name!")])
    inputLastName = StringField('Last Name', [DataRequired(message="Please enter your last name!")])
    inputEmail = StringField('Email address', [Email(message="Not a valid email address!"), DataRequired(message="Please enter your your email address!")])
    inputPassword = StringField('Password', [InputRequired(message="Please enter your password!"), EqualTo('inputComfirmPassword', message="Passwords does not match!") ])
    inputComfirmPassword = PasswordField('Confirm password')
    submit = SubmitField('Sign Up')