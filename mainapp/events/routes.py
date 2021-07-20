from flask import Blueprint 
from flask import render_template, render_template, request, url_for, redirect,flash, abort
from flask_login import current_user, login_required
from mainapp.events.forms import NewEvent
from mainapp.models import Event
from mainapp import db
from mainapp.events.utils import event_picture


events = Blueprint('events',__name__,template_folder='templates' )



@events.route('/event/new',methods=['GET','POST'])
@login_required
def new_event():
  form = NewEvent()
  if form.validate_on_submit():

    title = form.title.data
    description = form.description.data
    location = form.location.data
    ticket_price = form.ticket_price.data
    total_tickets = form.total_tickets.data
    start_date = form.start.data
    end_date = form.end.data
    start_time = form.start_time.data
    end_time = form.end_time.data
    if form.feature_image.data:
      image= event_picture(form.feature_image.data) 
      image = image

    event = Event(title=title,
                  description=description,
                  location=location, 
                  ticket_price=ticket_price, 
                  total_tickets=total_tickets, 
                  start=start_date, 
                  end=end_date, 
                  start_time=start_time, 
                  end_time=end_time,
                  user_id = current_user.id
                  )
    db.session.add(event)
    db.session.commit()
    return redirect(url_for('events.event',event_id=event.id))

  return render_template('new_event.html',form=form,title='Create New Event', legend='Create New Event')

@events.route('/event/<event_id>')
def event(event_id):
  event= Event.query.get_or_404(event_id)
  nearby_events = Event.query.filter_by(location=event.location).all()
  poster_img = url_for('static',filename='images/event_images/' + event.feature_image)
  return render_template('event.html', title=f"{event.title}", event=event,nearby_events=nearby_events, poster_img=poster_img)


@events.route('/event/<event_id>/update',methods=['GET','POST'])
def update_event(event_id):
  form = NewEvent()
  event= Event.query.get_or_404(event_id)
  if event.organiser != current_user:
    abort(403)
  if form.validate_on_submit():
    if form.feature_image.data:
      image = event_picture(form.feature_image.data)
      event.feature_image = image
    event.title = form.title.data
    event.location = form.location.data
    event.description = form.description.data
    event.start =  form.start.data
    event.end =  form.end.data
    event.start_time = form.start_time.data
    event.end_time = form.end_time.data
    event.ticket_price = form.ticket_price.data
    event.total_tickets = form.total_tickets.data
    db.session.commit()
    flash('Event Updated successfully', 'success')
    return redirect( url_for('events.event', event_id=event.id))
  elif request.method == 'GET':
    form.title.data = event.title
    form.description.data = event.description
    form.location.data = event.location
    form.start.data = event.start
    form.end.data = event.end
    form.start_time.data = event.start_time
    form.end_time.data = event.end_time
    form.ticket_price.data = event.ticket_price
    form.total_tickets.data = event.total_tickets
    form.feature_image.data = event.feature_image
  
  return render_template('new_event.html',
          title=f"Updating {event.title} Event",
          legend=f"Updating {event.title} Event",
           event=event,form=form
           )
  

@events.route('/event/<int:event_id>/delete', methods=['POST','GET'])
@login_required
def delete_event(event_id):
  event = Event.query.get_or_404(event_id)
  if event.organiser != current_user:
    abort(403)
  db.session.delete(event)
  db.session.commit()
  flash('event delete successfully','success')
  return redirect(url_for('users.account'))


@events.route('/city/<string:name>')
def city_loc(name):
  locate = request.args.get('filter', default = name, type = str)
  print(locate)
  events = Event.query.filter_by(location=name).order_by(Event.start.asc()).all()
  return render_template('city_view.html', title='Events in',events=events,locate=locate )
  


@events.route('/calender')
def calender():
  return render_template('calender.html', title='All Events')



