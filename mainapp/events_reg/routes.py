from flask import Blueprint 
from flask import render_template, render_template, request, url_for, redirect,flash, abort
from flask_login import current_user, login_required
from mainapp.events_reg.forms import EventRegistrationForm
from mainapp.models import db , Event



event_reg = Blueprint('event_registrations',__name__,template_folder='templates' )



@event_reg.route('/event_registration/<event_id>',methods=['GET','POST'])
@login_required
def event_registrations(event_id):
  form = EventRegistrationForm()
  event= Event.query.get_or_404(event_id)
  if form.validate_on_submit():
    pass

  
  return render_template('event_reg.html',form=form, event=event, title=f'Registration for {event.title}')
