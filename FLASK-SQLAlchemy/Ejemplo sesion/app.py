from flask import Flask, render_template, redirect, url_for
from flask import request, make_response, session
import time

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def inicio():

    # Obtiene el tiempo
    tiempo = time.ctime(time.time())

    # Verificamos que la variable username esté registrada en sesion
    if 'usuarioIngresado' in session:

        # Obtengo el nombre del Usuario
        usuarioNombre = session['usuarioIngresado']

        # Retorna el texto con código html
        return 'Has iniciado sesión en el Sitio como ' + usuarioNombre + '<br>' + \
            "<b><a href = '/logout'>Da click acá para salir</a></b>"'</br>' + tiempo

    else:

        # Retorna texto con código html
        return "No has iniciado sesión en el Sitio <br><a href = '/login'><b/>" + \
            "Dá click acá para ingresar</b></a></br>" + tiempo

@app.route('/login', methods=["GET", "POST"])
def login():

    # Obtiene el tiempo
    tiempo = time.ctime(time.time())

    # Verifica el Método
    if request.method == 'POST':

        # Registra la sesión con la cookie
        session['usuarioIngresado'] = request.form['nombre']

        # Redirecciona al inicio
        return redirect(url_for('inicio'))
    else:
        # Crea una variable para colocar la cadena con codigo html a retornar
        sCodigoHtml = tiempo + "</br>"
        sCodigoHtml += '<form action = "" method="post">'     # en action no especifico ninguna pagina, eso quiere decir que
        sCodigoHtml += '<p><label>Nombre</label></p>'       # el formulario se va a enviar a la misma pagina /login
        sCodigoHtml += '<p><input type=text name=nombre ></p>'
        sCodigoHtml += '<p><input type=submit value=Login ></p>'
        sCodigoHtml += '</form>'
        return sCodigoHtml

@app.route('/logout')
def logout():

    # Elimina la variable del vector de Sesión
    session.pop('usuarioIngresado', None)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)