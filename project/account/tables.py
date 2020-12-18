from flask_table import Table, Col, LinkCol

class userList(Table):
    id = Col('ID')
    name = Col('Name')
    address = Col('Delivery Address')
    email = Col('Email Address')
    phone = Col('Phone No.')
    area = Col('Area Manager')
    access = Col('Access')
    edit = LinkCol('Edit', 'account.editUser', url_kwargs=dict(id='id'))
    delete = LinkCol('Remove', 'account.removeUser', url_kwargs=dict(id='id'))