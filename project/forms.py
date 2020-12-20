from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, AnyOf

# MAIN FORMS
class loginForm(FlaskForm):
    userID = IntegerField(validators = [DataRequired()])
    password = PasswordField(validators = [DataRequired()])
    remember = BooleanField('Save Info')
    submit = SubmitField('Login')

# USER FORMS
class createUserForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    address = StringField('Address')
    email = StringField('Email', validators = [DataRequired()])
    phone = StringField('Phone No.')
    area = StringField('Area Manager')
    password = StringField('Password', validators = [DataRequired()])
    access = SelectField('Access Level', choices=[('Admin', 'Head Office Admin'), ('Area', 'Area Management'), ('Store', 'Store Management')], validators = [DataRequired()])
    submit = SubmitField('Create User')

class editUserForm(FlaskForm):
    name = StringField('Name')
    address = StringField('Address')
    email = StringField('Email')
    phone = StringField('Phone No.')
    area = StringField('Area Manager')
    password = StringField('Password', validators = [DataRequired()])
    access = SelectField('Access Level', choices=[('Admin', 'Head Office Admin'), ('Area', 'Area Management'), ('Store', 'Store Management')], validators = [DataRequired()])
    submit = SubmitField('Edit user') 

# SUPPLIER FORMS
class createSupplierForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    address = StringField('Address', validators = [DataRequired()])
    email1 = StringField('Email 1', validators = [DataRequired()])
    email2 = StringField('Email 2')
    email3 = StringField('Email 3')
    phone = StringField('Phone No.', validators = [DataRequired()])
    type = SelectField('Type', choices=[('C', 'Card'), ('P', 'Product')], validators = [DataRequired()])
    submit = SubmitField('Create Supplier') 

class editSupplierForm(FlaskForm):
    name = StringField('Name')
    address = StringField('Address')
    email1 = StringField('Email 1')
    email2 = StringField('Email 2')
    email3 = StringField('Email 3')
    phone = StringField('Phone No.')
    type = SelectField('Type', choices=[('C', 'Card'), ('P', 'Product')])
    submit = SubmitField('Edit Supplier') 