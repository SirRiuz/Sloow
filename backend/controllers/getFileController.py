
#
#   Este archivo se encarga de retornarme los archivos de video que se mosraran en el frontend
#   y las imagenes de perfil de los usuarios
#

from server import app
from flask import send_from_directory


app.config['VIDEO_POST_DIR'] = 'C:\\Users\\Mateo Jimenez\\Documents\\Loow\\backend\\files\\videos\\'
app.config['IMAGE_PROFILE_DIR'] = 'C:\\Users\\Mateo Jimenez\\Documents\Loow\\backend\\files\imgProfile\\'


@app.route('/video/<videoName>/' , methods=['GET'])
def getVideo (videoName):
    return send_from_directory(app.config['VIDEO_POST_DIR'] , videoName)


@app.route('/img/profile/<imgId>/')
def imageProfile (imgId):
    return send_from_directory(app.config['IMAGE_PROFILE_DIR'] , imgId)
