import sqlobject
from src import conn
from datetime import datetime

class User(sqlobject.SQLObject):
    _connection = conn
    name = sqlobject.StringCol()
    email = sqlobject.StringCol(length=30, notNone=True)
    info = sqlobject.JSONCol(default = {})
    created_on = sqlobject.DateTimeCol(default=datetime.now(), sqlType='DATETIME')

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "info": self.info,
            "created_on": self.created_on,
        }
