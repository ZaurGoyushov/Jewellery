import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Shop import app, db 
from Profile.models import Products

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180),  nullable=False)
    products = db.relationship('Products', backref='user', lazy=True)
    






 




    
    
    
            
     
    