from cProfile import label
from operator import length_hint
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message='You must enter a valid email address.')])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember_me = BooleanField(label="Remember me")
    submit = SubmitField(label='Log In')

class SignUpForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message='You must enter a valid email address.')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=25)]) 
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(message="You must confirm your password."), Length(min=8, max=25), EqualTo(fieldname='password', message='Password and Confirm Password doesn\'t match.')]) 
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    submit = SubmitField(label='Submit')