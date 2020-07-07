import peewee

database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class Baneo (peewee.Model):

    banId = peewee.TextField(unique=True , default=True)
    userId = peewee.TextField(unique=True)
    motivo = peewee.TextField()
    timeBan = peewee.TextField()

    class Meta (object):
        database = database
        db_table = 'Baneo'