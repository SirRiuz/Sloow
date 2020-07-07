
from server import app
from flask import (request , render_template , make_response , redirect , jsonify)
from models.Usuarios import Usuario
from utils.BanUtils import isBaned
import datetime
from models.sessionToken import SessionToken


@app.route('/api/v1/login/' , methods=['POST'])
def login () -> render_template:
    if request.method == 'POST':
        return loginManager(request.form.get('email') , request.form.get('password'))


def loginManager (email : str , password : str):
    try:
        query = Usuario.select().where((Usuario.correo == email).bin_and(Usuario.contraseña==password)).get()
        if query:
            if not isBaned(query.id):
                return {
                    'session':{
                        'id':query.id,
                        'nickName':query.nickName,
                        'userName':'{} {}'.format(query.nombreN , query.apellido),
                        'profileMode':query.profileMode,
                        'email':query.correo,
                        'profileImage':'profile image'
                    }
                }
            else:
                return {
                    'error':{
                        'type-error':'ban_acount',
                        'messege':'Tu cuenta a sido suspendida'
                    }
                }

    except:
        return {
            'error':{
                'type-error':'login-error',
                'messege':'No se a podido iniciar sesion , porque el correo o la contraseña son incorrectos'
            }
        }

def createTokenSession ():
    sessionKey = SessionToken.create(userId='xxsdsi').save().get()
    print(sessionKey['sessionTokenId'])
