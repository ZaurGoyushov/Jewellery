from wtforms import Form, BooleanField, StringField, PasswordField,SelectField, validators,ValidationError
from flask_wtf import FlaskForm
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from collection.models import Brand


class AddBrandForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=3, max=25)])
    def validate_Name (self,BrandName):
        if Brand.query.filter_by(BrandName = name.data):
            raise ValidationError ("This Brand already exist")  

    

class AddCategoryForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    Brand = SelectField('Brand', [validators.Length(min=4, max=25)])