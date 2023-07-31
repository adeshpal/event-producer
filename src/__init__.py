# Database Connection

from sqlobject.mysql import builder
conn = builder()(user='root', password='root@123',
                 host='localhost', db='audit_srv')