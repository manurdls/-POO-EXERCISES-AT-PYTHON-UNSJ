from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')     #ruta raíz
def usuario():
    return render_template('nuevo_usuario.html')

@app.route('    /bienvenida', methods= ['POST', 'GET'])         #entra por 'POST' cuando reciba un formulario.
                                                                #entra por 'GET' cuando la propia aplicación
                                                                #llama a la función.
                                                                #Gracias a esto yo desde no voy a poder ingresar
                                                                #a esta ruta directamente ingresando esta dirección.
def bienvenida():
    if request.method == 'POST':
        if request.form['nombre'] and request.form['email'] and request.form['password']:   #evalua si se enviaron
                                                                                            #todos los datos
            datosform = request.form    #guardo los datos del formulario en la variable datosform
            return render_template('bienvenida.html', datos=datosform, hora=datetime.now().hour)    #retorna la pagina
                                                                                                    #web bienvenida, y
                                                                                                    #envio como parámetros
                                                                                                    #datos (que son los
                                                                                                    #datos que venían desde
                                                                                                    #el formulario) y la hora.
        else: #si no recibe todos los datos
            return render_template('nuevo_usuario.html')

if __name__ == '__main__':
    app.run(debug=True) #cuando estamos en desarrollo es bueno tener el parametro debug=True porque
                        #para no estar teniendo que reiniciar el servidor cada vez que realizo una modificación
                        #en la aplicación