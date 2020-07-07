from models.seguidores import Seguidores


def getFactoriFollowers (myId):
    itemFilter = []
    query = Seguidores.select().where((Seguidores.userB == myId)).execute()
    for item in query:
        itemFilter.append(item)
    return len(itemFilter)
