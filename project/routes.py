from flask import render_template, url_for, flash, redirect
from project import app, db, bcrypt
from project.forms import loginForm, createUserForm
from project.models import users, suppliers

@app.route("/", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.storeID.data == 1 and form.password.data == '1':
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)

@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/createUser", methods=['GET', 'POST'])
def createUser():
    form = createUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = users(name=form.name.data, address=form.address.data, email=form.email.data, phoneNo=form.phoneNo.data, area=form.area.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createUser.html', title='Create User', form=form)