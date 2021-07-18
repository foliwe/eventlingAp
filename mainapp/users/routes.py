from flask import Blueprint ,render_template, render_template, request, url_for, redirect,flash
from mainapp.users.forms import  RegistrationForm, LoginForm, UpdateUserForm
from flask_login import login_user, current_user, logout_user, login_required
from mainapp import bcrypt, db
from mainapp.models import User
from mainapp.users.utils import save_picture


users = Blueprint('users',__name__,template_folder='templates')



@users.route('/register',methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  if form.validate_on_submit():
    hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(name=form.name.data, email=form.email.data, password=hash_password)
    db.session.add(user)
    db.session.commit()

    flash('Your registration was successfully','success')
    return redirect(url_for('users.login'))
  return render_template('register.html',form=form,title='Register')




@users.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user,remember=form.remember_me.data)
      next_page = request.args.get('next')
      return redirect( next_page ) if next_page else redirect(url_for('main.index'))
    else:
      flash('Wrong Credentails. try again', 'danger')

  return render_template('login.html',form=form,title='Login' ,methods=['GET','POST'])

@users.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))



@users.route('/account', methods=['GET','POST'])
@login_required
def account():
  events = current_user.events
  form = UpdateUserForm()
  if form.validate_on_submit():
    if form.picture.data:
      profile_file = save_picture(form.picture.data)
      current_user.user_profile_img = profile_file
    current_user.name = form.name.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Account successfully updated','success')
    return redirect( url_for('users.account'))
  elif request.method == 'GET':
    form.name.data = current_user.name
    form.email.data = current_user.email

  profile_img = url_for('static',filename='images/' + current_user.user_profile_img)

  return render_template('account.html', title=f'Account for {current_user.name}', form=form, profile_img=profile_img, events=events)
