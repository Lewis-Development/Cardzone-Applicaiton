from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from project import db, bcrypt
from project.account.forms import loginForm, createUserForm, editUserForm
from project.models import users
from project.account.tables import userList

account = Blueprint('account', __name__)

@account.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = loginForm()

    if form.validate_on_submit():
        user = users.query.filter_by(id=form.userID.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Incorrect Details')

    return render_template('login.html', title='Login', form=form)

@account.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('account.login'))

@account.route("/userManagement")
@login_required
def userManagement():
    table = userList(users.query.all())
    return render_template('userManagement.html', title='Users', table=table)

@account.route("/createUser", methods=['GET', 'POST'])
def createUser():
    form = createUserForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = users(
            name = form.name.data, 
            address = form.address.data, 
            email = form.email.data, 
            phone = form.phone.data, 
            area = form.area.data, 
            password = hashed_password, 
            access = form.access.data
        )

        db.session.add(user)
        db.session.commit()

        flash(f'- Created User ({user.name})')
        return redirect(url_for('account.userManagement'))

    return render_template('createUser.html', title='Create User', form=form)

@account.route('/editUser/<int:id>', methods=['GET', 'POST'])
@login_required
def editUser(id):
    form = editUserForm()

    find = db.session.query(users).filter(users.id==id)
    user = find.first()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user.name = form.name.data
        user.address = form.address.data
        user.email = form.email.data
        user.phone = form.phone.data
        user.area = form.area.data
        user.password = hashed_password
        user.access = form.access.data

        db.session.commit()

        flash(f'- Updated User ({user.name})')
        return redirect(url_for('account.userManagement'))
    elif request.method == 'GET':
        form.name.data = user.name
        form.address.data = user.address
        form.email.data = user.email
        form.phone.data = user.phone
        form.area.data = user.area
        form.access.data = user.access
    return render_template('editUser.html', title='Edit User',form=form)

@account.route('/removeUser/<int:id>', methods=['GET', 'POST'])
@login_required
def removeUser(id):
    find = db.session.query(users).filter(users.id==id)
    user = find.first()

    if user and user != current_user:
        flash(f'- Removed User ({user.name})')

        db.session.delete(user)
        db.session.commit()
    
    return redirect(url_for('account.userManagement'))