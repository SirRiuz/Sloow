import peewee

database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class videoLike (peewee.Model):

    userId = peewee.TextField(default=False)
    videoId = peewee.TextField(default=False)

    class Meta (object):
        database = database
        db_table = 'likeVideo'
