import peewee

database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class Seguidores(peewee.Model):

    id = peewee.TextField(unique=True , default=False)
    userA = peewee.TextField(default=False)
    userB = peewee.TextField(default=False)

    class Meta (object):
        database = database
        db_table = 'Seguidores'