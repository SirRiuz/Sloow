

from flask import redirect
from server import app

@app.errorhandler(404)
def errorNotFound (e):
    return {
        'error':{
            'type-error':'error_not_found',
            'messege':'El servidor no a encontrado la ganina ...'
        }
    },404

@app.errorhandler(405)
def errorInternal (e):
    return {
        'error':{
            'type-error':'client-error',
            'messege':'A ocurrido un error con el cliente ...',
            'code':'mehtod-error'
        }
    },405
