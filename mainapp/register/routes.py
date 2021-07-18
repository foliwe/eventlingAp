from flask import Blueprint, render_template ,flash, redirect, url_for
from mainapp.models import Event
from mainapp.register.forms import EventRegistrationForm
from flask_login import  current_user


register = Blueprint('register',__name__,template_folder='templates' )

@register.route('/apply',methods=['GET','POST'])
def apply():
  form = EventRegistrationForm()
  if form.validate_on_submit():
    user = current_user
    return user.name
  return render_template('apply.html', title='Register For Event', form=form)


