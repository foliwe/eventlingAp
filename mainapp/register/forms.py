from flask_wtf import FlaskForm
from wtforms import SubmitField


class EventRegistrationForm(FlaskForm):
    submit = SubmitField('Register For Event')
