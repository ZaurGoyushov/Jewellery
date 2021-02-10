from flask import  render_template, session, request, redirect, url_for,flash,session,abort
from flask_login import login_user,current_user,logout_user,login_required
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import app, db ,bcrypt
from auth.forms import RegistrationForm,LoginForm
from Dashboard.models import User
from collection.models import Category,Brand
from Profile.models import Products
from collection.forms import AddBrandForm,AddCategoryForm




@app.route("/",methods=['GET', 'POST'])
def index():
    AllData=Products.query.all()
    return render_template('home/index.html',All=AllData)
       



@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def UserDelete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/admin/users/<int:id>', methods=['GET', 'POST'])
def UserUpdate(id):
    if request.method=="post":
        return redirect(url_for('users'))
    else:
        users=User.query.get(id)
        return render_template("admin/user.html",user=users)
        return redirect(url_for('users'))

           
            
         

@app.route('/admin')
@login_required
def admin():
    if current_user.email == "zaur.gyshv@gmail.com":
        return redirect("/admin/users")
    else:
        abort(403)
    return render_template ('admin.html')
        



@app.route('/admin/users', methods=['GET', 'POST'])
def users():
    user_info=User.query.all()
    
    return render_template('admin/user.html', table_info = user_info ,title='Users')

@app.route('/admin/Category', methods=['GET', 'POST'])
def Categories():
    cats=Category.query.all()
    
    return render_template('admin/Category.html',cats=cats )

@app.route('/admin/brand', methods=['GET', 'POST'])
def brand():
    brand=Brand.query.all()

    return render_template('admin/brand.html', brand = brand )


@app.route('/admin/addBrand', methods=['GET', 'POST'])
def AddBrand():
    form=AddBrandForm()
    if request.method=="POST":
        New_Brand = Brand(BrandName=form.name.data)
        db.session.add(New_Brand)
        db.session.commit()
        db.create_all()
        flash(f'THE {form.name.data} ADDED','success')
        return redirect("addBrand")
    return render_template('admin/AddBrand.html', form=form)

@app.route('/admin/AddCat', methods=['GET', 'POST'])
def AddCat():
    form=AddCategoryForm()
    brand=Brand.query.all()
    if request.method=="POST":
        
        New_Cat = Category(CategoryName=form.name.data,brand_id=request.form.get('Brand'))
        db.session.add(New_Cat)
        db.session.commit()
        db.create_all()
        flash(f'THE {form.name.data} ADDED','success')
        return redirect("AddCat")
        

    return render_template('admin/AddCategory.html', form=form,brand=brand)
    