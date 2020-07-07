
import peewee

database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class Publicaciones (peewee.Model):

    postId = peewee.IntegerField(default=False , unique=True , primary_key=True)
    userId = peewee.TextField(default=False)
    textMessege = peewee.TextField(default=False)
    videoMode = peewee.TextField(default=False)
    zoneName = peewee.TextField(default=False)

    class Meta (object):
        database = database
        db_name = 'Publicaciones'




Publicaciones.create_table()