from flask import Flask,blueprints
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_uploads import IMAGES ,UploadSet,configure_uploads,patch_request_class
import os
#pip install -U Werkzeug==0.16.0

filedir= os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_product.db'
app.config['SECRET_KEY']='Jewell'
app.config['UPLOADED_PHOTOS_DEST']=os.path.join(filedir,'static/photo')
app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png', 'jpg', 'jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
photos=UploadSet('photos',IMAGES)
configure_uploads(app,photos)
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category='info'





from .Dashboard import routes
from .collection import routes
from .auth import routes
from .Profile import routes
