from flask import render_template, url_for, flash, redirect
from project import app
from project.forms import loginForm
from project.models import access, suppliers

@app.route("/", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.storeID.data == 1 and form.password.data == '1':
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)

def home():
    return render_template('home.html', title='Home')