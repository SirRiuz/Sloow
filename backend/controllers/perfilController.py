
from server import app
from flask import (Flask ,
                   render_template ,
                   redirect ,
                   request ,
                   jsonify)

from models.Usuarios import Usuario
from models.Baneo import Baneo
from utils.deleteFactoriSession import deleteFactoriCookie
from models.seguidores import Seguidores
from utils.followersManager import (getFactoriFollowers , getFactoriFollowers)
from models.Publicaciones import Publicaciones
from utils.getLikeVideo import getLikesNumber
from utils.BanUtils import isBaned
from utils.getUserData import getJsonData

userId = ''
myId = ''

@app.route('/api/v1/profile/' , methods=['POST'])
def profile () -> render_template :
    global myId
    myId = request.form.get('userId')
    nickNameParam = request.form.get('nickName')
    global userId
    try:
        userId = Usuario.select().where(Usuario.nickName == nickNameParam).get().id
    except:
        return {
            'error':{
                'error':'El perfil {} no existe'.format(nickNameParam),
                'code':'13129',
                'type':'profile-no-exits'
            }
        } , 404

    return baneoFactori(userId , nickNameParam)


def baneoFactori (idUser : str , nickName : str) -> str:
    #queryStream = Baneo.select().where(Baneo.userId == idUser).execute()
    if isBaned(idUser):
        return jsonify({
            'error':{
                'code':123,
                'messege':'Esta cuenta a sido suspendida'
            }
        })
    else:
        profileData = profileDataFactori(nickName)
        showProfileVideosById(profileData['profile']['profileID'])
        return accesJoinProfile(profileData)


def profileDataFactori (nickName : str):
    global myId
    query = ''
    query = Usuario.select().where(Usuario.nickName == nickName).get()
    profileSpectMode = 'root'

    if  not myId == query.id:
        profileSpectMode = 'espect'
        return jsonDataProfile(query , profileSpectMode)

    return jsonDataProfile(query , profileSpectMode)


def getVideosProfile (idProfile):
    query = Publicaciones.select().where(Publicaciones.userId == idProfile).execute()
    videoListProfile = []
    for videoItems in query:
        videoListProfile.append(videoItems.id)
    return videoListProfile


def accesJoinProfile (profileData):
    global myId
    #print('#### mMY id ' , myId)
    if myId == profileData['profile']['profileID']:
        return profileData

    if profileData['profile']['profileMode'] == 'pv':

        if isFollower(myId):
            return profileData

        if not myId:
            #redirectProfile = profileData['profile']['nickName']
            return jsonify({"error":{
                'code':323,
                'messege':'Inicia sesion para ver el contenido de este perfil',
                'type-error':'profile-private'
            }})

        return {
            'error':{
                'messege':'Nesecitas seguir a {} para poder ver su contenido'.format(profileData['profile']['nickName']),
                'type-error':'profile-private',
                'code':'863b1'
            }
        }

    return profileData


def showProfileVideosById (profileId):
    profileVideos = Publicaciones.select().where(Publicaciones.userId == profileId).execute()
    videoList = []
    for videosItem in profileVideos:
        videoList.append(videosItem.postId)
    return videoList


def jsonDataProfile (query , profileSpectMode):
    profileData = getJsonData(query.id)
    profileData['profileSpectMode'] = profileSpectMode
    print(profileData)
    return {
            'profile':profileData,
            'videos':getVideoObject(showProfileVideosById(query.id))
    }


def getVideoObject (videoIdList):
    videoObjectList = []
    for videoId in videoIdList:
        query = Publicaciones.select().where(Publicaciones.postId == videoId).execute()
        for videoItems in query:
            videoObjectList.append({
                'video':{
                    'messege':videoItems.textMessege,
                    'videoId':videoItems.postId,
                    'videoLiskeNumber':getLikesNumber(videoItems.postId),
                    'videoMode':videoItems.videoMode,
                    'videoLikesIdList':[],
                    'commentsNumber':0,
                    'commentsIdList':[]
                }
            })

    return videoObjectList


#
#   Este metodo comprueva si estamos siguendo al perfil al que estamos intentando
#   acceder , Si los estamos siguiendo retornara True , en caso contrario retornara
#   False.
#

def isFollower (myid):
    booleanFollowing = False
    query = Seguidores.select().where((Seguidores.userA == myid).bin_and(Seguidores.userB == 'aisdvbaidsavbdu')).execute()
    for items in query:
        booleanFollowing = True

    return booleanFollowing







#############################################################################
#                               FIN DEL CODIGO :D                           #
#############################################################################