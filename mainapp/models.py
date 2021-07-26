from datetime import datetime
from mainapp import  db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))





class User(db.Model,UserMixin):

  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(20), nullable=False, unique = True)
  email = db.Column(db.String(120), nullable=False, index=True, unique=True)
  password = db.Column(db.String(60), nullable=True)
  created_date = db.Column(db.DateTime,default=datetime.utcnow, index=True)
  user_profile_img = db.Column(db.String, default='pic.png')
  registrations = db.relationship('Registration',backref='member', lazy=True)
  events = db.relationship('Event',backref='organiser', lazy=True)
  
 
 

  
  def __repr__(self) -> str:
      return  self.name


class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String, nullable=False)
    feature_image = db.Column(db.String, nullable=True, default='event.png')

    start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    end = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,index=True)
    total_tickets =db.Column(db.Integer,nullable=False , default=1)
    ticket_price = db.Column(db.Float, nullable=False, default=0.01)

    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    location = db.Column(db.String(60), nullable=False)

    created_date = db.Column(db.DateTime,default=datetime.utcnow, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self) -> str:
      return self.title




class Registration(db.Model):

    __tablename__ = 'registrations'

    id = db.Column(db.Integer,primary_key = True)
    source = db.Column(db.String(120),)
    terms_and_conditions = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)


    def __repr__(self) -> str:
      return self.user_id



