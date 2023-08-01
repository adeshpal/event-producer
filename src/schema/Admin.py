import sqlobject
from src import conn
from datetime import datetime

class Admin(sqlobject.SQLObject):
    """Admin info table"""
    _connection = conn
    name = sqlobject.StringCol()
    role = sqlobject.IntCol(default=0)
    email = sqlobject.StringCol()
    password = sqlobject.StringCol()
    created_on = sqlobject.DateTimeCol(default=datetime.now(), sqlType='DATETIME')

    def get_dict(self):
        """resp dict"""
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "email": self.email,
            "password": self.password,
            "created_on": self.created_on,
        }
Admin.createTable(ifNotExists=True)
