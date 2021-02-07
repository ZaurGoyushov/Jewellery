import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Shop import app, db 
from Dashboard import models
from collection.models import Category,Brand





class Products(db.Model):
    products_Product_id = db.Column(db.Integer, primary_key=True)
    products_ProductName = db.Column(db.String(30),  nullable=False)
    products_Brand = db.Column(db.String(80),  nullable=False)
    products_Price = db.Column(db.String(120), nullable=False)
    products_ProductInfo = db.Column(db.String(120), nullable=False)
    products_ProductImage= db.Column(db.String(120), nullable=False)
    cat_id=db.Column(db.Integer,db.ForeignKey('category.Category_id'), nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)