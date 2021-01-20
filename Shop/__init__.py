from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_product.db'
app.config['SECRET_KEY']='Jewell'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from .Dashboard import routes
from .collections import routes
