from flask import  render_template, session, request, redirect, url_for,flash
from Shop import app, db ,bcrypt
from .forms import RegistrationForm
import os

@app.route("/")
def home():
    return ('home page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                   # form.password.data)
       # db_session.add(user)
        flash('Thanks for registering')
       # return redirect(url_for('register'))
    return render_template('admin/register.html', form=form,title='Registration page')