from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from project import app, db, bcrypt
from project.forms import loginForm, createUserForm, editUserForm
from project.models import users
from project.tables import userList

@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = loginForm()

    if form.validate_on_submit():
        user = users.query.filter_by(id=form.userID.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Incorrect Details')

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/home")
@login_required
def home():
    return render_template('home.html', title='Home')

@app.route("/displayUsers")
@login_required
def displayUsers():
    table = userList(users.query.all())
    return render_template('user/displayUsers.html', title='Users', table=table)

@app.route("/displayUsers/createUser", methods=['GET', 'POST'])
@login_required
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

        return redirect(url_for('user/displayUsers'))

    return render_template('user/createUser.html', title='Create User', form=form)

@app.route('/displayUsers/editUser/<int:id>', methods=['GET', 'POST'])
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
        return redirect(url_for('user/displayUsers'))
    elif request.method == 'GET':
        form.name.data = user.name
        form.address.data = user.address
        form.email.data = user.email
        form.phone.data = user.phone
        form.area.data = user.area
        form.access.data = user.access
    return render_template('user/editUser.html', title='Edit User',form=form)

@app.route('/displayUsers/removeUser/<int:id>', methods=['GET', 'POST'])
@login_required
def removeUser(id):
    find = db.session.query(users).filter(users.id==id)
    user = find.first()

    if user and user != current_user:
        flash(f'- Removed User ({user.name})')
        db.session.delete(user)
        db.session.commit()
    
    return redirect(url_for('user/displayUsers'))