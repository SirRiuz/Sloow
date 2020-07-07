

from server import app
from flask import (Flask , request , render_template , redirect , url_for)
import os
import hashlib
import random
from models.Publicaciones import Publicaciones
#from utils.geoLocalisation import getLocationObject

@app.route('/new/' , methods=['GET' , 'POST'])
def postManaget ():

    if not request.cookies.get('user_id'):
        return redirect('/')

    if request.method == 'POST':
        file = request.files['ourFile']
        if file.filename =='':
            return 'Deves enviar un video como requisito para hacer un post'
        print(file.filename)
        saveFileInFormath(file , file.filename)
        return redirect(url_for('postManaget'))
    return render_template('upload.html')


def saveFileInFormath (file , fileName):
    file.save(os.path.join(app.config['UPLOAD_FOLDER'] , ranameFactoryFile() + '.mp4'))


def ranameFactoryFile ():
    id = random.randint(0,99999999) * 10
    keyId = hashlib.sha256(str(random.randint(0,9999)).encode()).hexdigest()
    messege = request.form.get('text-messege')
    myId = request.cookies.get('user_id')
    #print('Befor ' + id)
    #zoneName=getLocationObject()['country']
    Publicaciones.create(id=random.randint(0,10) ,postId=id , userId=myId ,textMessege=messege , videoMode='pb' , zoneName='').save()
    #socketIo.emit('newPost' , 'Esto es un nuevo post' , broadcast=True)
    #return id + fileFormat
    #print('After ' + id)
    return str(id)

def generateRandomId () -> str:
    return hashlib.sha256(str(random.randint(0,9999)).encode()).hexdigest()


