import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import app, db 
from Profile import models


class Brand(db.Model):
    Brand_id = db.Column(db.Integer, primary_key=True)
    BrandName = db.Column(db.String(30),unique=True,  nullable=False )
    Categories = db.relationship('Category', backref='brand', lazy=True) 
    products = db.relationship('Products', backref='brand', lazy=True)

class Category(db.Model):
    Category_id = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(30), unique=True, nullable=False)
    products = db.relationship('Products', backref='category', lazy=True)
    brand_id=db.Column(db.Integer,db.ForeignKey('brand.Brand_id'), nullable=False)