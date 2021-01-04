from flask import  render_template, session, request, redirect, url_for,flash
from Shop import app, db ,bcrypt



@app.route("/collections")
def collection():
    return render_template('collections/Collection.html')



@app.route("/allproducts")
def Allproducts():
    return render_template('collections/AllProducts.html')


@app.route("/product")
def product():
    return render_template('collections/product.html')

















