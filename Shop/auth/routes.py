from flask import  render_template, session, request, redirect, url_for,flash,session
from flask_login import login_user,current_user,logout_user,login_required
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import app, db ,bcrypt
from Dashboard.models import User
from collection.models import Category,Brand
from Profile.models import Products
from .forms import RegistrationForm,LoginForm





@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        Hash_password = bcrypt.generate_password_hash(form.password.data)
        New_user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                   password=Hash_password,Phone=form.Phone.data)
        db.session.add(New_user)
        db.session.commit()
        db.create_all()
        flash(f'Welcome {form.name.data} Lets login','success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form,title='Registration page')


 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method=="POST" and form.validate():
         CheckUser = User.query.filter_by(email = form.email.data).first()
         if CheckUser and bcrypt.check_password_hash (CheckUser.password , form.password.data):
            login_user(CheckUser)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
         else:
            flash('Wrong Password or email try again','danger')      
    return render_template('admin/login.html', form=form,title='login page')


@app.route ('/logout')
def logout():
    logout_user()
    return redirect("login")


