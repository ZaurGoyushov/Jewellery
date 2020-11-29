from flask import render_template, session, request, redirect, url_for

from Shop import app, db

@app.route("/")
def home():
    return ('home page')


@app.route("/register")
def register():
    return render_template('admin/register.html', title = "Register user")