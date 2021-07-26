from flask import Blueprint 
from flask import render_template, render_template, request, url_for, redirect,flash, abort
from flask_login import current_user, login_required
from mainapp.events_reg.forms import RegistrationForm
from mainapp.models import db , Event, Registration



event_reg = Blueprint('event_reg',__name__,template_folder='templates' )



@event_reg.route('/event_registration/<event_id>',methods=['GET','POST'])
@login_required
def event_registrations(event_id):
  form = RegistrationForm()
  event= Event.query.get_or_404(event_id)
  if event.organiser == current_user:
    return redirect(url_for('main.index'))

  if form.validate_on_submit():
    source = form.source.data
    user = current_user
    reg_event = event
    terms = form.terms.data
    new_reg = Registration(user_id=user.id, event_id=reg_event.id, source=source, terms_and_conditions=terms)
    db.session.add(new_reg)
    db.session.commit()
    flash('Thanks for your registration','success')
    return redirect(url_for('main.index'))


  return render_template('event_reg.html',form=form, event=event, title=f'Registration for {event.title}')



