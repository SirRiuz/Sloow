
from server import app
from flask import(redirect , url_for , request , render_template)
from models.Usuarios import Usuario

@app.route('/account/register/' , methods=['GET' , 'POST'])
def register ():
    idSession = request.cookies.get('user_id')
    if not idSession:

        if request.method == 'POST':
            emai = request.form.get('email')
            password = request.form.get('password')
            confirmPassword = request.form.get('confPassword')
            nickName = request.form.get('nickName')

            print('Metodo post iniciando')


        return render_template('register.html')

    return redirect('/')