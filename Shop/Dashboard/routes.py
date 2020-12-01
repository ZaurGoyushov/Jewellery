from flask import  render_template, session, request, redirect, url_for,flash
from Shop import app, db ,bcrypt
from .forms import RegistrationForm,LoginForm
from .models import User
import os

@app.route("/")
def home():
    return render_template('admin/index.html')
         

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        Hash_password = bcrypt.generate_password_hash(form.password.data)
        New_user = User(name=form.name.data, username=form.username.data,email=form.email.data,
                   password=Hash_password)
        db.session.add(New_user)
        db.session.commit()
        db.create_all()
        flash(f'Welcome {form.name.data} Lets login','success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form,title='Registration page')
 
@app.route('/login', methods=['GET', 'POST'])
def login():
     form = LoginForm(request.form)
     if request.method == 'POST' and form.validate():
         user = User.query.filter_by(email = form.email.data).first()
         if user and bcrypt.check_password_hash (user.password , form.password.data):
            session['email']= form.email.data
            flash(f'welcome {form.email.data} you are logedin now','succes')
            return redirect(url_for('home'))
         else:
          flash('Wrong Password try again','danger')      
     return render_template('admin/login.html', form=form,title='login page')



@app.route('/admin', methods=['GET', 'POST'])
def admin():

    return render_template('/admin.html')



@app.route('/admin/users', methods=['GET', 'POST'])
def users():
    user_info=User.query.all()

    return render_template('admin/user.html', table_info = user_info ,title='Users')
    