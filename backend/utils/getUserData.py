
from flask import request
from models.Usuarios import  Usuario
from server import app
from utils.followersManager import  getFactoriFollowers

@app.route('/get/profile/<userId>')
def getUserdataById (userId):
    return getJsonData(userId)


def getJsonData (id):
    try:
        responseData = Usuario.select().where(Usuario.id == id).get()
        return {
            'name':'{} {}'.format(responseData.nombreN , responseData.apellido),
            'email':responseData.correo,
            'nickName':responseData.nickName,
            'profileIcon':'',
            'profileID':responseData.id,
            'followersNumber':getFactoriFollowers(responseData.id),
            'profileMode':responseData.profileMode
        }

    except:
        return {
            'error':{
                'messege':'A ocurrido un error al obtener los tados del perfil',
                'type-error':'getUserData-error',
                'code':'j5hv246b4'
            }
        }
