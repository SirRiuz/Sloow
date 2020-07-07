

from flask import Flask , jsonify , request
from server import app
from models.Publicaciones import Publicaciones
from models.seguidores import Seguidores
from models.Baneo import Baneo
from utils.BanUtils import isBaned


postId = ''
josinJuserProfile = ''

@app.route('/api/v1/get/post/' , methods=['POST'])
def elementPost () -> str:
    global postId
    global josinJuserProfile
    josinJuserProfile = request.form.get('user_id')
    postId = request.form.get('postId')
    videoPropertis = getVideoPropertis(postId)

    if not videoPropertis:
        return {
            'error':{
                'messege':'Esta publicacion no existe',
                'type-error':'post-not-found',
                'code':'38dw20k'
            }
        } , 404

    if videoPropertis['video']['video_mode'] == 'pv':

        #   Si mi id y la id del posteador coinciden
        if josinJuserProfile == videoPropertis['video']['User']:
            return videoPropertis

        # Si soy un seguidor del posteador
        if False:
            return videoPropertis

        return {
            'error':{
                'messege':'Nesecitas ser seguidor de {} para ver este video'.format(videoPropertis['video']['User']),
                'type-error':'video-private',
                'code':'3nw98an'
            }
        }
    
    return videoPropertis


def getVideoPropertis (id : str):
    quetyVideo = Publicaciones.select().where(Publicaciones.postId == id).execute()
    jsonVideoObject = {}
    for videoItem in quetyVideo:
        jsonVideoObject = {
            'video':{
                'User':videoItem.userId,
                'VideoFormat':'.mp4',
                'video_mode':videoItem.videoMode,
                'video_id':videoItem.postId,
                'video_dir':"{}.mp4".format(videoItem.postId),
                'messege':videoItem.textMessege
            }
        }

    return jsonVideoObject
