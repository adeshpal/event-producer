import sqlobject
from src import conn

class Role(sqlobject.SQLObject):
    _connection = conn
    name = sqlobject.IntCol(default=0)
    description = sqlobject.StringCol(length=30, notNone=True)
    permissions = sqlobject.StringCol(dnotNone=True)

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "permissions": self.permissions,
           
        }
