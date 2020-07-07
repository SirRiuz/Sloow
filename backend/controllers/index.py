
from server import app
from models.Usuarios import Usuario
import models.Usuarios as dadaUsuario
import models.seguidores
from models.Publicaciones import Publicaciones
from flask import request , redirect , make_response
from models.seguidores import Seguidores
from models.Publicaciones import Publicaciones
from flask import jsonify , render_template
from models.Baneo import Baneo
from utils.BanUtils import isBaned
from utils.getLikeVideo import getLikesNumber , getLikesID
import random
from utils.getUserData import  getJsonData

@app.route('/api/v1/videos/' , methods=['POST'])
def index () -> str :
    return jsonify(ordenateVideo(postVideoById()))

def loadListFollowers ():
    myId = request.form.get('userId')
    query = Seguidores.select().where((Seguidores.userB == myId)).execute()
    MyFollowing = Seguidores.select().where((Seguidores.userA == myId)).execute()

    followersNumber = 0
    listFollowerId = []
    myFollowingFlisr = []
    for itemFollowersId in query:
        listFollowerId.append(itemFollowersId.userA)
        followersNumber = followersNumber + 1

    for itemFollowing in MyFollowing:
        myFollowingFlisr.append(itemFollowing.userB)

    return {
        'Followers':listFollowerId,
        'Following':myFollowingFlisr,
        'Number_follower' : followersNumber
    }

def postVideoById():
    diveoArray = []
    myUserId = request.form.get('myUserId')
    for usersIdItems in loadListFollowers()['Following']:
        query = Publicaciones.select().where((Publicaciones.userId == usersIdItems).bin_or(Publicaciones.userId == myUserId)).execute()
        for itemVideoClopt in query:
            if not isBaned(itemVideoClopt.userId):
                diveoArray.append({
                    'video':{
                        'VideoFormat':'.mp4',
                        'videoId':itemVideoClopt.postId,
                        'postUrl':'http://127.0.0.1:5000/post/sdfbskfnsk',
                        'videoDir':"http://127.0.0.1:5000/video/{}.mp4/".format(itemVideoClopt.postId),
                        'messege':itemVideoClopt.textMessege,
                        'videoMode' : itemVideoClopt.videoMode,
                        'videoLikes':getLikesNumber(itemVideoClopt.postId),
                        'videoLikesIds':getLikesID(itemVideoClopt.postId),
                        'position':positioningNumber(0/10,0/10,0/10,getLikesNumber(itemVideoClopt.postId)/10,0/10,0/10,0/10),
                        'posteador':getJsonData(itemVideoClopt.userId)
                    }
                })

    return diveoArray

def ordenateVideo (videoList):
    videoArray = sorted(videoList, key=lambda x: x['video']['position'] , reverse=True)
    return videoArray


def positioningNumber(*args) -> float:
    positionNumber = 0.0
    for item in args:
        #print(float(item))
        positionNumber = float(item) + positionNumber

    #print('Punto de possicionamiento es -> ' , positionNumber)

    return positionNumber/2
