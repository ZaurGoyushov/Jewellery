from flask import  render_template, session, request, redirect, url_for,flash
from Shop import app, db ,bcrypt



@app.route("/collection")
def collection():
    return render_template('sections/Collection.html')



@app.route("/products")
def products():
    return render_template('sections/product.html')


















