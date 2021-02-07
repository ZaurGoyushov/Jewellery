from flask import  render_template, session, request, redirect, url_for,flash
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import db,app





@app.route("/collections")
def collection():
    return render_template('collections/Collection.html')



@app.route("/allproducts")
def Allproducts():
    return render_template('collections/AllProducts.html')


@app.route("/product")
def product():
    return render_template('collections/product.html')

















