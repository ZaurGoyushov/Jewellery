from Shop import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(180),  nullable=False)
    #profile = db.Column(db.String(180), unique=false, nullable=False, default='profile.jpg')


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(30),  nullable=False)
    Brand = db.Column(db.String(80),  nullable=False)
    Price = db.Column(db.String(120), nullable=False)
    ProductInfo = db.Column(db.String(120), nullable=False)
    
       

    


     