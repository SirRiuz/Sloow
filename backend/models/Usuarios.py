import peewee
import hashlib
import random


database = peewee.MySQLDatabase('Loow' , user='root' , password='' , port=3306 , host='localhost')


class Usuario (peewee.Model):

    id = peewee.TextField(unique=True , default=hashlib.sha256(str(random.randint(0 , 9999999999)).encode()).hexdigest())
    nombreN = peewee.TextField(default=False)
    apellido = peewee.TextField(default=False)
    correo = peewee.TextField(unique=True , default=False)
    contraseña = peewee.TextField(default=False)
    dateUni = peewee.TextField(default=False)
    sexo = peewee.TextField(default=False)
    nickName = peewee.TextField(unique=True , default=False)
    profileMode = peewee.TextField(default=False)

    class Meta:
        database = database
        db_table = 'Usuarios'


def createDatabase ():
    if not Usuario.table_exists():
        Usuario.create_table()

