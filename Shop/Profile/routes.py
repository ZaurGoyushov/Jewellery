from flask import  render_template, session, request, redirect, url_for,flash,session
from flask_login import login_user,current_user,logout_user,login_required
from Shop import app, db ,bcrypt
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from auth.forms import RegistrationForm,LoginForm
from Dashboard.models import User
from collection.models import Category,Brand
from Profile.models import Products



@app.route("/profil", methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('customer/profile.html')

@app.route("/AddProduct", methods=['GET', 'POST'])
@login_required
def addProduct():
    if request.method == 'POST':
        Product=Products(products_ProductName=request.form['ProductName'],products_Brand=request.form['Brand'],
        products_Price=request.form['Price'],products_ProductInfo=request.form['info'],products_ProductImage="3.jpg")
        db.session.add(Product)
        db.session.commit()
        db.create_all()
        flash('product successfully added','success')
        return redirect('/profile')
        
    return render_template('customer/AddProduct.html')