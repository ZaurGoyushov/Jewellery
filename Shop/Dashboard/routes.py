from flask import  render_template, session, request, redirect, url_for,flash,session,abort
from flask_login import login_user,current_user,logout_user,login_required
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import app, db ,bcrypt
from auth.forms import RegistrationForm,LoginForm
from Dashboard.forms import UpdateUser,UpdateCategory,UpdateBrand
from Dashboard.models import User
from collection.models import Category,Brand
from Profile.models import Products
from collection.forms import AddBrandForm,AddCategoryForm




@app.route("/",methods=['GET', 'POST'])
def index():
    AllData=Products.query.all()
    return render_template('home/index.html',All=AllData)
       

@app.route('/admin')
@login_required
def admin():
    if current_user.email == "zaur.gyshv@gmail.com":
        return render_template ('admin.html')
    else:
        abort(403)
    return render_template ('admin.html')
        

@app.route('/admin/users', methods=['GET', 'POST'])
@login_required
def users():
    user_info=User.query.all()
    if current_user.email == "zaur.gyshv@gmail.com":
        return render_template('admin/user.html',table_info = user_info ,title='Users')
    else:
        abort(403)
    return render_template('admin/user.html')

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def UserDelete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/updateUser/<int:id>', methods=['GET', 'POST'])
@login_required
def UserUpdate(id):
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
    
        


@app.route('/admin/Category', methods=['GET', 'POST'])
@login_required
def Categories():
    cats=Category.query.all()
    if current_user.email == "zaur.gyshv@gmail.com":
        return render_template('admin/Category.html',cats=cats)
    else:
        abort(403)
    return render_template('admin/Category.html' )

@app.route('/admin/brand', methods=['GET', 'POST'])
@login_required
def brand():
    brand=Brand.query.all()
    if current_user.email == "zaur.gyshv@gmail.com":
        return render_template('admin/brand.html', brand = brand)
    else:
        abort(403)
    return render_template('admin/brand.html' )


@app.route('/admin/addBrand', methods=['GET', 'POST'])
@login_required
def AddBrand():
    form=AddBrandForm(request.form)
    if current_user.email == "zaur.gyshv@gmail.com":
        if request.method=="POST" and form.validate():
            New_Brand = Brand(BrandName=form.name.data)
            db.session.add(New_Brand)
            db.session.commit()
            db.create_all()
            flash(f'THE {form.name.data} ADDED','success')
            return redirect("addBrand")
        return render_template('admin/AddBrand.html',form=form)
    else:
        abort(403)
    return render_template('admin/AddBrand.html')


@app.route('/updateBrand/<int:id>', methods=['GET', 'POST'])
@login_required
def BrandUpdate(id):
    form=UpdateBrand(request.form)
    brand=Brand.query.get(id)
    if current_user.email == "zaur.gyshv@gmail.com":
        if request.method=="POST":
            brand.BrandName=form.name.data
            db.session.commit()
            return redirect(url_for('brand'))
        return render_template('admin/UpdateBrand.html',form=form,brand=brand)
    else:
        abort(403)
    return render_template('admin/UpdateBrand.html')

@app.route('/deleteBrand/<int:id>', methods=['GET', 'POST'])
def BrandDelete(id):
    brand=Brand.query.get(id)
    db.session.delete(brand)
    db.session.commit()
    return redirect(url_for('brand'))

@app.route('/admin/AddCat', methods=['GET', 'POST'])
@login_required
def AddCat():
    form=AddCategoryForm(request.form)
    brand=Brand.query.all()
    if current_user.email == "zaur.gyshv@gmail.com":
        if request.method=="POST":
            New_Cat = Category(CategoryName=form.name.data,brand_id=request.form.get('Brand'))
            db.session.add(New_Cat)
            db.session.commit()
            db.create_all()
            flash(f'THE {form.name.data} ADDED','success')
            return redirect("AddCat")
        return render_template('admin/AddCategory.html', form=form,brand=brand)
    else:
        abort(403)
    return render_template('admin/AddCategory.html')


@app.route('/updateCategory/<int:id>', methods=['GET', 'POST'])
@login_required
def CatUpdate(id):
    form=UpdateCategory(request.form)
    Cat=Category.query.get(id)
    brand=Brand.query.all()
    if current_user.email == "zaur.gyshv@gmail.com":
        if request.method=="POST":
            Cat.CategoryName=form.name.data
            Cat.brand_id=request.form.get('Brand')
            db.session.commit()
            return redirect(url_for('Categories'))
        return render_template('admin/UpdateCat.html',form=form,Category=Cat,brand=brand)
    else:
        abort(403)
    return render_template('admin/UpdateCat.html')

@app.route('/deleteCat/<int:id>', methods=['GET', 'POST'])
def CategoryDelete(id):
    cat=Category.query.get(id)
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for('Categories'))


@app.route('/admin/AllProducts', methods=['GET', 'POST'])
def AllPro():
    Allpro=Products.query.all()
    return render_template('admin/Allproduct.html',pro=Allpro)

@app.route('/deleteProduct/<int:id>', methods=['GET', 'POST'])
def ProductDelete(id):
    pro=Products.query.get(id)
    db.session.delete(pro)
    db.session.commit()
    return redirect(url_for('AllPro'))
    
    


    