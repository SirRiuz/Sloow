

from flask import (request , make_response , redirect)


def deleteFactoriCookie ():
    make = make_response(redirect('/'))
    make.set_cookie('session_manager' , '' , expires=0)	
    make.set_cookie('user_id' , '' , expires=0)
    return make

