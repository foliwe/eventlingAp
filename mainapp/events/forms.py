from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import  StringField, SubmitField,TextAreaField, IntegerField, DecimalField,DateTimeField
from wtforms.validators import DataRequired




class NewEvent(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired()])
    description = TextAreaField('Event Description', validators=[DataRequired()])
    feature_image = FileField('Feature Image', validators=[FileAllowed(['jpg','jpeg','png'])])
    start = DateTimeField('Start Date',format="%Y-%m-%d",validators=[DataRequired()])
    end = DateTimeField('End Date',format="%Y-%m-%d",validators=[DataRequired()])
    start_time = DateTimeField(' Start time',format='%H:%M')
    end_time = DateTimeField('End Time',format='%H:%M')
    location = StringField('Event Location', validators=[DataRequired()])
    total_tickets = IntegerField('Number Of Tickets Available')
    ticket_price = DecimalField('Tiket Price',validators=[DataRequired()])

    submit = SubmitField('Submit')