from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class loginForm(FlaskForm):
    userID = IntegerField('UserID', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Save Info')
    submit = SubmitField('Login')

class userForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    address = StringField('Address')
    email = StringField('Email')
    phoneNo = StringField('Phone No.')
    area = SelectField('Area', choices=[('GB-ENG', 'England'), ('GB-SCT', 'Scotland'), ('GB-WLS', 'Wales'), ('GB-NIR', 'Ireland')], validators = [DataRequired()])
    password = StringField('Password', validators = [DataRequired()])
    access = IntegerField('Access Level', validators = [DataRequired()])
    submit = SubmitField('Create')