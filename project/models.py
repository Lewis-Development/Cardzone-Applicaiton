from project import db, login_manager
from flask_login import UserMixin

# users(id, name, address, email, phoneNo, area[areasID], password, access)
# areas(id, name, manager[usersID])
# suppliers(id, name, field, address, email1, email2, email3, phoneNo)

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(80))
    email = db.Column(db.String(50))
    phoneNo = db.Column(db.String(15))
    area = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(60), nullable=False, default='password')
    access = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f"users('{self.id}', '{self.name}', '{self.address}', '{self.email}', '{self.phoneNo}', '{self.area}', '{self.password}', '{self.access}')"