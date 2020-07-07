from models.Baneo import Baneo

def isBaned (userId):
    try:
        Baneo.select().where(Baneo.userId == userId).get()
        return True
    except:
        return False
