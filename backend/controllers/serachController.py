

from models.Usuarios import Usuario
from server import app
from flask import (Flask ,  render_template  , url_for , request , jsonify , redirect)
from utils.followersManager import getFactoriFollowers
from models.Baneo import Baneo

@app.route('/serach/')
def busquedas():


    if not request.cookies.get('session_manager'):
        return redirect('/')

    if getQueryJson():
        return jsonify(getQueryJson())
    return {
        'error':{
            'messege':'No se han encontrado resultados para esta persona'
        }
    }


def getQueryJson ():
    jsonQueyArray = []
    query = request.args.get('q')

    if  query:
        query = Usuario.select().where(Usuario.nickName % '{}%'.format(query))
        for x in query:
            #print(x.nickName)

            if not isBanned(x.id):
                jsonQueyArray.append({
                    'profile':{
                        'id':x.id,
                        'nombre':x.nombreN,
                        'apellido':x.apellido,
                        'nickName':x.nickName,
                        'seguidores':getFactoriFollowers(x.id),
                    }
                })

        return jsonQueyArray


def isBanned (idUser):
    return Baneo.select().where(Baneo.userId == idUser).execute()
