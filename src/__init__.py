# Database Connection

from sqlobject.mysql import builder
conn = builder()(user='root', password='root@123',
                 host='mysql', db='audit_srv')