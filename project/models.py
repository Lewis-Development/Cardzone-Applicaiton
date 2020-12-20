from project import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(80))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    area = db.Column(db.String(30))
    password = db.Column(db.String(60), nullable=False, default='password')
    access = db.Column(db.String(60), nullable=False)
    orders = db.relationship('orders', backref='author', lazy=True)

    def __repr__(self):
        return f"users('{self.id}', '{self.name}', '{self.address}', '{self.email}', '{self.phone}', '{self.area}', '{self.password}', '{self.access}')"

class suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(80))
    email1 = db.Column(db.String(50))
    email2 = db.Column(db.String(50))
    email3 = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    type = db.Column(db.String(10))
    orders = db.relationship('orders', backref='supplier', lazy=True)

class orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    supplier = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False))