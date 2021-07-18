from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import  StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from flask_login import current_user
from mainapp.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                         validators=[DataRequired(),
                          Length(min=2,max=20)])
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    password_confirmation = PasswordField('Password confirmation',
                             validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('This email is already taken ')

    def validate_name(self, name):
      user = User.query.filter_by(name=name.data).first()
      if user:
        raise ValidationError('This username is already taken')


class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Login')


class UpdateUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
      if email.data != current_user.email:
        user = User.query.filter_by(email=email.data).first()
        if user:
          raise ValidationError('This email is already Taken ')

    def validate_name(self, name):
      if name.data != current_user.name:
        user = User.query.filter_by(name=name.data).first()
        if user:
          raise ValidationError('This username is already taken')
