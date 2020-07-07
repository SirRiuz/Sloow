import peewee

database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class joinComunnity (peewee.Model):
    id = peewee.IntegerField(default=0 , unique=True , primary_key=True)
    userId = peewee.TextField(default=False)
    communityId = peewee.TextField(default=False)

    class Meta (object):
        database = database
        db_table = 'joinComunnity'


#joinComunnity.create_table()
