from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def usuario():
    return render_template('nuevo_usuario.html')

@app.route('/bienvenida', methods= ['POST', 'GET'])
def bienvenida():
    if request.method == 'POST':
        if request.form['nombre'] and request.form['email'] and request.form['password']:
            datosform = request.form
            return render_template('bienvenida.html', datos=datosform, hora=datetime.now().hour)
        else:
            return render_template('nuevo_usuario.html')

if __name__ == '__main__':
    app.run(debug=True)