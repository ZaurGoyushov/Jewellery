import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Shop import app, db 
from Dashboard import models
from collection.models import Category,Brand





class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(30),  nullable=False)
    Size = db.Column(db.String(80),  nullable=False)
    Color = db.Column(db.String(80),  nullable=False)
    Price = db.Column(db.String(120), nullable=False)
    ProductInfo = db.Column(db.String(120), nullable=False)
    Material = db.Column(db.String(120), nullable=False)
    Stock = db.Column(db.String(60), nullable=False)
    ProductImage_1= db.Column(db.String(120), nullable=False)
    ProductImage_2= db.Column(db.String(120))
    cat_id= db.Column(db.Integer,db.ForeignKey('category.Category_id'), nullable=False)
    brand_id= db.Column(db.Integer,db.ForeignKey('brand.Brand_id'), nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    