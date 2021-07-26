from flask import Blueprint, render_template ,flash, redirect, url_for
from mainapp.models import Event
import  datetime


main = Blueprint('main',__name__,template_folder='templates' )

@main.route('/')
def index():
  now = datetime.datetime.now()
  events = Event.query.filter(Event.start > now).order_by(Event.start.asc()).paginate(per_page=12)
  return render_template('index.html', title='Index',events=events)

