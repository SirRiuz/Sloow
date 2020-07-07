
import peewee
import random
import base64
import hashlib

database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')
randomKey = ''

class SessionToken (peewee.Model):

    sessionTokenId = peewee.TextField(unique=True , default=hashlib.sha256(base64.encodebytes(str((random.randint(0, 99999) * 10)).encode())).hexdigest())
    userId = peewee.TextField(unique=True)

    class Meta (object):
        database = database
        db_table = 'sessions'


#SessionToken.create(userId='8216312').save()
#SessionToken.create_table()
