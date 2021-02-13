from wtforms import Form, BooleanField, StringField, PasswordField,SelectField
from wtforms.validators import ValidationError,EqualTo,DataRequired,Email,Length
from flask_wtf import FlaskForm
import os,sys
from os.path import dirname,abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
from collection.models import Brand,Category


class AddBrandForm(Form):
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=25)])
    def validate_name(self,name):
        brand=Brand.query.filter_by(BrandName = name.data).first()
        if brand:
            raise ValidationError("This Brand already exist")  

    

class AddCategoryForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=25)])
    Brand = SelectField('Brand', validators=[DataRequired(), Length(min=3, max=25)])
    def validate_name (self,name):
        cat=Category.query.filter_by(CategoryName = name.data).first()
        if cat:
            raise ValidationError ("This Category already exist")