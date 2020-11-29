from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_product.db'
app.config['SECRET_KEY']='Jewell'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
from .Dashboard import routes

