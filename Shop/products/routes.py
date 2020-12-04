from flask import  render_template, session, request, redirect, url_for,flash
from Shop import app, db ,bcrypt



@app.route("/cart")
def cart():
    return render_template('sections/cart.html')


















