from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# Crea el objeto Flask
app = Flask(__name__)

# Establesco los parametros de configuración desde config.py
app.config.from_pyfile('config.py')

# Importo el objeto SQLAlchemy
from models import db

# Importo los modelos de las clases que se enlazan con la base de datos
from models import Usuarios

# Semilla para encriptamiento
semilla = bcrypt.gensalt()


# Defnie la ruta principal
@app.route('/')
def main():
    nuevo_usuario = Usuarios(nombre='Manuel', correo='manurossidls@gmail.com', password='asdfwkejfjksadfw')
    db.session.add(nuevo_usuario)
    db.session.commit()
    if 'nombre' in session:
        return render_template('inicio.html')
    else:
        return render_template('ingresar.html')

# Define la ruta index
@app.route('/inicio')
def inicio():
    if 'nombre' in session:
        return render_template('inicio.html')
    else:
        return render_template('ingresar.html')

# Define la ruta de registro
@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    if request.method == "GET":
        # Acceso no concedido

        # Verifica que haya sesion
        if 'nombre' in session:
            return render_template('inicio.html')
        else:
            return render_template('ingresar.html')
    else:
        # Obtengo los datos del request
        nombre = request.form['nmNombreRegistro']
        correo = request.form['nmCorreoRegistro']
        password = request.form['nmPasswordRegistro']
        # Encripto el password
        password_encode = password.encode("utf-8")
        password_encriptado = bcrypt.hashpw(password_encode, semilla)
        # Creo un objeto de tipo Usuarios
        nuevo_usuario = Usuarios(nombre=nombre, correo=correo, password=password_encriptado)
        # Agrego ese objeto a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Registro la sesion
        session['nombre'] = nombre
        session['correo'] = correo

        # Redirijo a index
        return redirect(url_for('inicio'))

# Define la ruta para ingresar
@app.route('/ingresar', methods=["GET", "POST"])
def ingresar():
    if request.method == "GET":
        # Acceso no concedido

        # Verifica que haya sesion
        if 'nombre' in session:
            return render_template('inicio.html')
        else:
            return render_template('ingresar.html')
    else:
        # Obtengo los datos del objeto request
        correo = request.form['nmCorreoLogin']
        password = request.form['nmPasswordLogin']
        password_encode = password.encode("utf-8")

        # Busco el correo en la base de datos
        usuario = Usuarios.query.filter_by(correo=correo).first()

        if usuario is None:
            # No encotro el correo

            # Mensaje Flash
            flash("El Correo no existe", "alert-warning")

            # Redirige a Ingresar
            return render_template('ingresar.html')
        else:
            # Encontro el correo

            # Obtengo el password encripatdo encode del usuario que obtuve de la base de datos
            password_encriptado_encode = usuario.password

            # Verifico si el password ingresado por el usuario es igual al password que hay en la base de datos
            if bcrypt.checkpw(password_encode, password_encriptado_encode):
                # Si la contraseña es correcta

                # Registra la sesion
                session['nombre'] = usuario.nombre
                session['correo'] = usuario.correo

                # Redirijo al inicio
                return redirect(url_for('inicio'))
            else:
                # Si la contraseña es incorrecta

                # Mensaje Flash
                flash("El password no es correcto", "alert-warning")

                # Redirige a Ingresar
                return render_template('ingresar.html')

# Define la ruta de salida
@app.route('/salir')
def salir():
    # Limpio las sesiones
    session.clear()

    # Redirijo a Ingresar
    return redirect(url_for('ingresar'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)