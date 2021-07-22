from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField,BooleanField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired




class RegistrationForm(FlaskForm):
    source = SelectField(u'Where is you hear about this event?',
                           choices=[('google', 'Google Search'),
                          ('newpaper', 'New Paper'),
                          ('tv', 'Televison'),
                          ('friend', 'Fromn a Friend'),
                          ('other', 'Others')
                          ], validators=[DataRequired()])
    terms = BooleanField('Accepts Terms and Conditions', validators=[DataRequired()])
    submit = SubmitField('Register To Event')