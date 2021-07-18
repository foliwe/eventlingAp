import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from mainapp.config import Config
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category ='info'



def create_app(config_class=Config):
  app = Flask(__name__)
  migrate = Migrate(app, db)
  app.config['SECRET_KEY']='bc4f4df3e44187dabf55937743d47b4c'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'eventdatabase.db')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  from mainapp.users.routes import users
  from mainapp.events.routes import events
  from mainapp.main.routes import main
  from mainapp.errors.handlers import  errors
  from mainapp.register.routes import  register

  app.register_blueprint(users)
  app.register_blueprint(events)
  app.register_blueprint(main)
  app.register_blueprint(errors)
  app.register_blueprint(register)

  return app