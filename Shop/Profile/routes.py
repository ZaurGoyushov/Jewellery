from flask import  render_template, session, request, redirect, url_for,flash,session,abort
from flask_login import login_user,current_user,logout_user,login_required
from Shop import app, db ,bcrypt,photos
import os,sys,secrets
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from auth.forms import RegistrationForm,LoginForm
from Dashboard.models import User
from collection.models import Category,Brand
from Profile.models import Products
from Profile.forms import UpdateAccount



@app.route("/profil", methods=['GET', 'POST'])
@login_required
def profile():

    return render_template('customer/profile.html')

@app.route("/profil/MyAccount", methods=['GET', 'POST'])
@login_required
def MyAcc():
    if current_user.is_authenticated:
        UserID=str(current_user.id)
        user=User.query.filter_by(id=UserID).first()
        return render_template('customer/MyAccountDetail.html',user=user)
    return render_template('customer/MyAccountDetail.html')



@app.route('/profil/updateAcc/<int:id>', methods=['GET', 'POST'])
@login_required
def AccountUpdate(id):
    form=UpdateAccount(request.form)
    users=User.query.get(id)
    if current_user.email != "zaur.gyshv@gmail.com" and users.email!="zaur.gyshv@gmail.com":
        if request.method=="POST":
            users.name=form.name.data
            users.username=form.username.data
            users.Phone=form.Phone.data
            users.email=form.email.data          
            db.session.commit()
            return redirect(url_for('profile'))
        return render_template('customer/UpdateAccount.html',form=form,users=users)
    else:
        abort(403)
    return render_template('admin/UpdateUser.html')

@app.route("/profil/Product", methods=['GET', 'POST'])
@login_required
def UserProduct():
     if current_user.is_authenticated:
        UserID=str(current_user.id)
        product=Products.query.filter_by(user_id=UserID).all()
        return render_template('customer/products.html',product=product)
     return render_template('customer/products.html')



@app.route('/profil/updateProfil/<int:id>', methods=['GET', 'POST'])
@login_required
def updateProfil(id):
    form=UpdateUser(request.form)
    users=User.query.get(id)
    if current_user.email == "zaur.gyshv@gmail.com":
        if request.method=="POST":
            users.name=form.name.data
            users.username=form.username.data
            users.Phone=form.Phone.data
            db.session.commit()
            return redirect(url_for('users'))
        return render_template('admin/UpdateUser.html',form=form,users=users)
    else:
        abort(403)
    return render_template('admin/UpdateUser.html')

@app.route("/AddProduct", methods=['GET', 'POST'])
@login_required
def addProduct():
    brand=Brand.query.all()
    cat=Category.query.all()
    if request.method == 'POST':
        image_1=photos.save(request.files.get('image_1'),name=secrets.token_hex(10) + '.')
        image_2=photos.save(request.files.get('image_2'),name=secrets.token_hex(10) + '.')

        Product=Products(ProductName=request.form['ProductName'],Color=request.form['Color'],brand_id=request.form['Brand'],
        Price=request.form['Price'],ProductInfo=request.form['info'],ProductImage_1=image_1,ProductImage_2=image_2,
        cat_id=request.form['Cat'],user_id=current_user.id,Size=request.form['Size'],Material=request.form['Material'],Stock=request.form['Stock'])
        db.session.add(Product)
        db.session.commit()
        db.create_all()
        flash('product successfully added','success')
        return redirect('/AddProduct')
        
    return render_template('customer/AddProduct.html',brands=brand,cats=cat)


@app.route("/UpdateProduct/<int:id>", methods=['GET', 'POST'])
@login_required
def UpdateProduct(id):
    pro=Products.query.get(id)
    cat=Category.query.all()
    brand=Brand.query.all()
    if request.method == 'POST':
        pro.ProductImage_1=photos.save(request.files.get('image_1'),name=secrets.token_hex(10) + '.')
        pro.ProductImage_2=photos.save(request.files.get('image_2'),name=secrets.token_hex(10) + '.')
        pro.ProductName=request.form['ProductName']
        pro.brand_id=request.form['Brand']
        pro.Price=request.form['Price']
        pro.ProductInfo=request.form['info']
        pro.cat_id=request.form['Cat']
        pro.Color=request.form['Color']
        pro.user_id=current_user.id
        pro.Size=request.form['Size']
        pro.Material=request.form['Material']
        pro.Stock=request.form['Stock']
        db.session.commit()
        flash('product successfully added','success')
        return redirect(url_for('UserProduct'))  
    return render_template('customer/UpdateProduct.html',pro=pro,cat=cat,brand=brand)

@app.route("/profil/Product/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def deletePro(id):
    products=Products.query.get(id)
    db.session.delete(products)  
    db.session.commit() 
    return redirect(url_for('UserProduct'))




    
   
