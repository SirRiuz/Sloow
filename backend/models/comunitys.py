import peewee


database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class comunityManager (peewee.Model):
    id = peewee.IntegerField(unique=True , default=False , primary_key=True)
    #userId = peewee.TextField(default=False)
    comunityMode = peewee.TextField(default='pb')
    title = peewee.TextField(default=False)
    comunityName = peewee.TextField(default=False) #Unico
    descripcion = peewee.TextField(default=False)


    class Meta(object):
        database = database
        db_table = 'comunity'


#comunityManager.create_table()