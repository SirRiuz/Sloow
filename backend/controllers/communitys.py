

from server import app
from models.comunitys import comunityManager
from flask import (redirect , request , redirect)
from models.joinComunity import  joinComunnity

comunityDataFactory = ''

@app.route('/co/<communityName>/')
def communitysSystem (communityName):
    #joinComunnity.create(id=123 , userId='kasjdakjsdva' , communityId=324243).save()
    global comunityDataFactory
    myId = request.cookies.get('user_id')
    comunityDataFactory = getDataComunityFactory(communityName)
    #comunityManager.create(id=8213863 , comunityMode='pv' , title='memes para todos' , comunityName='memes' , descripcion='Comunidad sobre videos de memes').save()


    if comunityDataFactory:

        getComunityMembers(comunityDataFactory['comunityData']['id'])

        if comunityDataFactory['comunityData']['mode'] == 'pv':
            if not request.cookies.get('user_id'):
                return redirect('/account/login/?next=/community/{}/'.format(communityName))

            if isJoinCommunity(myId , comunityDataFactory['comunityData']['id']):
                pass
            else:
                return 'Esta comunidad es privada , nesecitas una invitacion del administrador para poder ingresar ...'

        return comunityDataFactory

    return 'Esta comunidad no existe ...'


def getDataComunityFactory (nickName : str) :
    comunityDataObject = {}
    query = comunityManager.select().where(comunityManager.comunityName == nickName).execute()
    for items in query:
        #print(items.id)
        comunityDataObject = {
            'comunityData':{
                'id':items.id,
                'mode':items.comunityMode,
                'title':items.title,
                'nickName':items.comunityName,
                'description' : items.descripcion,
                'members':[]
            }
        }

    return comunityDataObject


def isJoinCommunity (userId , communityId) -> bool:
    return joinComunnity.select().where((joinComunnity.userId == userId).bin_and(joinComunnity.communityId == communityId)).execute()
    #boolMaster = False
    #return ''

def getComunityMembers (cominityId):
    query = joinComunnity.select(joinComunnity.communityId == '324243').execute()
    for itemFactory in query:
        print(itemFactory)