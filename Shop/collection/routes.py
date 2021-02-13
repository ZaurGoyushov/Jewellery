from flask import  render_template, session, request, redirect, url_for,flash
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import db,app
from Dashboard.models import User
from collection.models import Category,Brand
from Profile.models import Products



@app.route("/product/<int:id>",methods=['GET', 'POST'])
def SingPro(id):
    AllData=Products.query.get(id)
    return render_template('collections/SingleProduct.html',data=AllData)

@app.route("/collections")
def collection():
    
    return render_template('collections/Collection.html')



@app.route("/allproducts",methods=['GET', 'POST'] )
def Allpro():
    brands=Brand.query.all()
    cats=Category.query.all()
    pro=Products.query.all()
    return render_template('collections/AllProducts.html',brands=brands,cats=cats,pro=pro)




















