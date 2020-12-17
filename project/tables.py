from flask_table import Table, Col, LinkCol

class userList(Table):
    id = Col('ID')
    name = Col('Name')
    address = Col('Address')
    email = Col('Email')
    phone = Col('Phone No.')
    area = Col('Area')
    access = Col('Access')
    edit = LinkCol('Edit', 'removeUser', url_kwargs=dict(id='id'))
    delete = LinkCol('Remove', 'removeUser', url_kwargs=dict(id='id'))