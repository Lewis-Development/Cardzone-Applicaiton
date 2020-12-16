from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class loginForm(FlaskForm):
    userID = IntegerField('UserID', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Save Info')
    submit = SubmitField('Login')

class createUserForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    address = StringField('Address')
    email = StringField('Email')
    phoneNo = StringField('Phone No.')
    area = SelectField('Area', choices=[('1', 'England'), ('2', 'Scotland'), ('3', 'Wales'), ('4', 'Ireland')], validators = [DataRequired()])
    password = StringField('Password', validators = [DataRequired()])
    access = IntegerField('Access Level', validators = [DataRequired()])
    submit = SubmitField('Create')