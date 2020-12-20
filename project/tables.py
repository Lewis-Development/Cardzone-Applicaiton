from flask_table import Table, Col, LinkCol

class userList(Table):
    id = Col('ID')
    name = Col('Name')
    address = Col('Address')
    email = Col('Email')
    phone = Col('Phone')
    area = Col('Area')
    access = Col('Access')
    edit = LinkCol('Edit', 'editUser', url_kwargs=dict(id='id'))
    delete = LinkCol('Remove', 'removeUser', url_kwargs=dict(id='id'))

class supplierList(Table):
    id = Col('ID')
    name = Col('Name')
    address = Col('Address')
    email1 = Col('Email 1')
    email2 = Col('Email 2')
    email3 = Col('Email 3')
    phone = Col('Phone')
    type = Col('Type')
    edit = LinkCol('Edit', 'editSupplier', url_kwargs=dict(id='id'))
    delete = LinkCol('Remove', 'removeSupplier', url_kwargs=dict(id='id'))