

from server import app
from utils.deleteFactoriSession import deleteFactoriCookie


@app.route('/user/close-session')
def logaut ():
    return deleteFactoriCookie()