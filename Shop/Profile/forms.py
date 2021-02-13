from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import ValidationError,EqualTo,DataRequired,Email,Length
from flask_wtf import FlaskForm
from Dashboard.models import User



class UpdateAccount(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=25)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    Phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('New Password', 
        validators=[DataRequired(),EqualTo('confirm', message='Passwords must match'),
        
    ])
    confirm = PasswordField('Repeat Password')

    def validate_email(self,email):

        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email already exist") 