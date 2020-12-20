# IMPORTS
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from project import app, db, bcrypt
from project.forms import loginForm, createUserForm, editUserForm, createSupplierForm, editSupplierForm
from project.models import users, suppliers
from project.tables import userList, supplierList

# MAIN ROUTES
@app.route("/home")
@login_required
def home():
    return render_template('home.html', title='Home')

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

# USER ROUTES
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

        return redirect(url_for('displayUsers'))

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
        return redirect(url_for('displayUsers'))
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
    
    return redirect(url_for('displayUsers'))

# SUPPLIER ROUTES
@app.route("/displaySuppliers")
@login_required
def displaySuppliers():
    table = supplierList(suppliers.query.all())
    return render_template('supplier/displaySuppliers.html', title='Suppliers', table=table)

@app.route("/displaySuppliers/createSupplier", methods=['GET', 'POST'])
@login_required
def createSupplier():
    form = createSupplierForm()

    if form.validate_on_submit():
        supplier = suppliers(
            name = form.name.data, 
            address = form.address.data, 
            email1 = form.email1.data, 
            email2 = form.email2.data, 
            email3 = form.email3.data, 
            phone = form.phone.data, 
            type = form.type.data
        )

        db.session.add(supplier)
        db.session.commit()

        flash(f'- Created Supplier ({supplier.name})')

        return redirect(url_for('displaySuppliers'))

    return render_template('supplier/createSupplier.html', title='Create Supplier', form=form)

@app.route('/displaySuppliers/editSupplier/<int:id>', methods=['GET', 'POST'])
@login_required
def editSupplier(id):
    form = editSupplierForm()

    find = db.session.query(suppliers).filter(suppliers.id==id)
    supplier = find.first()

    if form.validate_on_submit():
        supplier.name = form.name.data
        supplier.address = form.address.data
        supplier.email1 = form.email1.data
        supplier.email2 = form.email2.data
        supplier.email3 = form.email3.data
        supplier.phone = form.phone.data
        supplier.type = form.type.data

        db.session.commit()

        flash(f'- Updated Supplier ({supplier.name})')
        return redirect(url_for('displaySuppliers'))
    elif request.method == 'GET':
        form.name.data = supplier.name
        form.address.data = supplier.address
        form.email1.data = supplier.email1
        form.email2.data = supplier.email2
        form.email3.data = supplier.email3
        form.phone.data = supplier.phone
        form.type.data = supplier.type
    return render_template('supplier/editSupplier.html', title='Edit Supplier',form=form)

@app.route('/displaySuppliers/removeSupplier/<int:id>', methods=['GET', 'POST'])
@login_required
def removeSupplier(id):
    find = db.session.query(suppliers).filter(suppliers.id==id)
    supplier = find.first()

    if supplier:
        flash(f'- Removed Supplier ({supplier.name})')
        db.session.delete(supplier)
        db.session.commit()
    
    return redirect(url_for('displaySuppliers'))
