
from models.likeVideo import videoLike


def getLikesNumber (videoId):
    numLike = 0
    query = videoLike.select().where(videoLike.videoId == videoId).execute()
    for itemNumbers in query:
        numLike = numLike + 1
    return numLike


def getLikesID (videoId):
    numLike = []
    query = videoLike.select().where(videoLike.videoId == videoId).execute()
    for itemNumbers in query:
        numLike.append(itemNumbers.userId)
    return numLike