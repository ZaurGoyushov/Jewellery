from flask import  render_template, session, request, redirect, url_for,flash
from Shop import app, db ,bcrypt



@app.route("/collections")
def collection():
    return render_template('collections/Collection.html')



@app.route("/products")
def products():
    return render_template('collections/product.html')


















