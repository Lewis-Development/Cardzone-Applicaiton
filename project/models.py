from project import db

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(80))
    email = db.Column(db.String(50))
    phoneNo = db.Column(db.String(15))
    area = db.Column(db.Integer)
    password = db.Column(db.String(60), nullable=False, default='password')

    def __repr__(self):
        return f"users('{self.id}', '{self.password}')"

class suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    field = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(80))
    email1 = db.Column(db.String(50), nullable=False)
    email2 = db.Column(db.String(50))
    email3 = db.Column(db.String(50))
    phoneNo = db.Column(db.String(15))
    contactName = db.Column(db.String(30))

    def __repr__(self):
        return f"suppliers('{self.id}', '{self.name}')"