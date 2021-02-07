from flask import  render_template, session, request, redirect, url_for,flash,session
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
         CheckUser = User.query.filter_by(email = form.email.data).first()
         if CheckUser and bcrypt.check_password_hash (CheckUser.password , form.password.data):
            session['email']= form.email.data
            flash(f'welcome {form.email.data}','succes')
            return redirect(url_for('profil'))
         else:
          flash('Wrong Password try again','danger')      
     return render_template('admin/login.html', form=form,title='login page')