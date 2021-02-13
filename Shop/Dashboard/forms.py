from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import ValidationError,EqualTo,DataRequired,Email,Length
from Dashboard.models import User
from collection.models import Brand,Category


class UpdateUser(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=25)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    Phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('New Password', 
        validators=[DataRequired(),EqualTo('confirm', message='Passwords must match'),
        
    ])
    confirm = PasswordField('Repeat Password')


class UpdateBrand(Form):
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=25)])
    def validate_name(self,name):
        brand=Brand.query.filter_by(BrandName = name.data).first()
        if brand:
            raise ValidationError("This Brand already exist")  

    

class UpdateCategory(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=25)])
    def validate_name (self,name):
        cat=Category.query.filter_by(CategoryName = name.data).first()
        if cat:
            raise ValidationError ("This Category already exist")
    


