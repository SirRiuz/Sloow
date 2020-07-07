

from server import app
import utils.geoLocalisation as location
from models.Publicaciones import Publicaciones
from flask import jsonify

videoList = {}

@app.route('/now/')
def publics ():
    myZone = location.getLocationObject()['country']
    videoListItems = getAllPost(myZone)
    if videoListItems:
        return jsonify(videoListItems)

    return "No hay videos disponibles en tu pais '{}' ".format(myZone)


def getAllPost (myZoneLocation):
    query = Publicaciones.select().where(Publicaciones.zoneName == myZoneLocation).execute()
    videoList = []
    for videoItems in query:
        if not videoItems.videoMode == 'pv':
            videoList.append({
                'video':{
                    "User": videoItems.userId, 
                    "VideoFormat": ".mp4", 
                    "messege": videoItems.textMessege, 
                    "video_dir": "{}.mp4".format(videoItems.postId), 
                    "video_id": videoItems.postId, 
                    "video_mode": videoItems.videoMode
                }
            })

    return videoList