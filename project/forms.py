from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, AnyOf
from project.models import users

def choiceQuery():
    return users.query

class loginForm(FlaskForm):
    userID = IntegerField(validators = [DataRequired()])
    password = PasswordField(validators = [DataRequired()])
    remember = BooleanField('Save Info')
    submit = SubmitField('Login')

class userForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    address = StringField('Address')
    email = StringField('Email')
    phone = StringField('Phone No.')
    area = QuerySelectField('Area Manager', query_factory=choiceQuery, allow_blank=True, get_label='name')
    password = StringField('Password', validators = [DataRequired()])
    access = SelectField('Access Level', choices=[('Admin', 'Head Office Admin'), ('Area', 'Area Management'), ('Store', 'Store Management')], validators = [DataRequired()])
    submit = SubmitField('Create')