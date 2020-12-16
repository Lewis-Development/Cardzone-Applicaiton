from flask_table import Table, Col, LinkCol

class userList(Table):
    id = Col('ID')
    name = Col('Name')
    address = Col('Address')
    email = Col('Email')
    phoneNo = Col('Phone No.')
    area = Col('Area')
    access = Col('Access')
    edit = LinkCol('Edit', 'editUser', url_kwargs=dict(id='id'))
    delete = LinkCol('Remove', 'removeUser', url_kwargs=dict(id='id'))