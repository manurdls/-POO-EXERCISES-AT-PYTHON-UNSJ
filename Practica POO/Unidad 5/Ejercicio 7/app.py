from datetime import datetime
import hashlib
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuario, Pedido, Producto, ItemPedido


@app.route('/')
def main():
    if 'usuarioDni' in session:
        return redirect(url_for('inicio'))
    else:
        return redirect(url_for('login'))

@app.route('/inicio')
def inicio():
    if 'usuarioDni' in session:
        usuarioDni = session['usuarioDni']
        usuarioTipo = session['usuarioTipo']
        return render_template('inicio.html', tipo=usuarioTipo)
    else:
        return redirect(url_for('main'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['DNI'] or not request.form['password']:
            return render_template('login.html', error="Todos los campos son requeridos")
        else:
            usuario_actual = Usuario.query.filter_by(DNI=request.form['DNI']).first()
            if usuario_actual is None:
                return render_template('login.html', error="El usuario no está registrado")
            else:
                clave = hashlib.md5(bytes(request.form['password'], encoding='utf-8'))
                if usuario_actual.Clave != clave.hexdigest():
                    return render_template('login.html', error="Clave incorrecta")
                else:
                    session['usuarioDni'] = usuario_actual.DNI
                    session['usuarioTipo'] = usuario_actual.Tipo
                    return redirect(url_for('inicio'))
    if request.method == 'GET':
        if 'usuarioDni' in session:
            return redirect(url_for('inicio'))
        else:
            return render_template('login.html', error=None )

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('usuarioDni', None)
    session.pop('usuarioTipo', None)
    return redirect(url_for('main'))

productos_pedidos = []
@app.route('/inicio/registrar-pedido', methods=["GET", "POST"])
def registrarPedido():
    if request.method == 'POST':
        if not request.form['numMesa']:
            return render_template('registrar-pedido.html',
                                   tipo=session['usuarioTipo'],
                                   productos=Producto.query.all(),
                                   productos_pedidos=productos_pedidos,
                                   error="Ingrese el número de la mesa")
        else:
            if not request.form['observacion']:
                observacion = ""
            else:
                observacion = request.form['observacion']
            nuevo_pedido = Pedido(Fecha=datetime.now(),
                                  Cobrado=False, Observacion=observacion,
                                  DNIMozo=session['usuarioDni'],
                                  Mesa=request.form['numMesa'])
            db.session.add(nuevo_pedido)
            db.session.commit()
            total = 0.0
            for i in productos_pedidos:
                producto_actual = Producto.query.filter_by(Nombre=i).first()
                nuevo_item = ItemPedido(NumPedido=nuevo_pedido.NumPedido,
                                        NumProducto=producto_actual.NumProducto,
                                        Precio=producto_actual.PrecioUnitario,
                                        Estado="Pendiente")
                total += nuevo_item.Precio
                db.session.add(nuevo_item)
                db.session.commit()
            nuevo_pedido.Total = total
            db.session.commit()
            return redirect(url_for('inicio'))
    if request.method == 'GET':
        if 'usuarioDni' in session and session['usuarioTipo'] == 'Mozo':
            if not request.args.get("nombre"):
                del productos_pedidos[0:len(productos_pedidos)]
                return render_template('registrar-pedido.html',
                                       tipo=session['usuarioTipo'],
                                       productos=Producto.query.all())
            else:
                productos_pedidos.append(request.args.get("nombre"))
                return render_template('registrar-pedido.html',
                                       tipo=session['usuarioTipo'],
                                       productos=Producto.query.all(),
                                       productos_pedidos=productos_pedidos)
        else:
            return redirect(url_for('main'))

@app.route('/inicio/pedidos-vigentes', methods=["GET"])
def mostrarPedidosVigentes():
    if request.method == "GET":
        if 'usuarioDni' in session and session['usuarioTipo'] == 'Mozo':
            pedidos = Pedido.query.all()
            pedidos_vigentes = []
            fecha_actual = datetime.now()
            for pedido in pedidos:
                fecha = pedido.Fecha
                if fecha.day == fecha_actual.day and fecha.month == fecha_actual.month and fecha.year == fecha_actual.year:
                    if pedido.Cobrado == False:
                        pedidos_vigentes.append(pedido)

            if len(pedidos_vigentes) == 0:
                return render_template('listado-pedidos-vigentes.html',
                                       tipo=session['usuarioTipo'],
                                       mensaje="No hay pedidos vigentes")
            else:
                return render_template('listado-pedidos-vigentes.html',
                                       tipo=session['usuarioTipo'],
                                       pedidos_vigentes=pedidos_vigentes,
                                       productos=Producto.query.all())
        else:
            return redirect(url_for('main'))

@app.route('/inicio/cobrar-pedido', methods=["POST"])
def cobrarPedido():
    try:
        if request.method == "POST":
            if request.form["numPedido"]:
                pedido = Pedido.query.filter_by(NumPedido=request.form["numPedido"]).first()
                return render_template('cobrar-pedido.html',
                                       tipo=session['usuarioTipo'],
                                       pedido=pedido,
                                       productos=Producto.query.all())
    except:
            if request.form["confirmar"]:
                pedido = Pedido.query.filter_by(NumPedido=request.form["confirmar"]).first()
                pedido.Cobrado = True
                db.session.commit()
                return redirect(url_for('mostrarPedidosVigentes'))

@app.route('/inicio/ver-pedidos', methods=["GET", "POST"])
def verPedidos():
    if request.method == "POST":
        item = ItemPedido.query.filter_by(NumItem=request.form["numItem"]).first()
        item.Estado = "Listo"
        db.session.commit()
        return redirect(url_for('verPedidos'))
    if request.method == "GET":
        if 'usuarioDni' in session and session['usuarioTipo'] == 'Cocinero':
            pedidos = Pedido.query.all()
            pedidos_pendientes = []
            fecha_actual = datetime.now()
            for pedido in pedidos:
                fecha = pedido.Fecha
                if fecha.day == fecha_actual.day and fecha.month == fecha_actual.month and fecha.year == fecha_actual.year:
                    band = False
                    for item in pedido.items:
                        if not band:
                            if item.Estado == 'Pendiente':
                                print(item.Estado)
                                band = True
                    if band:
                        pedidos_pendientes.append(pedido)
            if len(pedidos_pendientes) == 0:
                print(len(pedidos_pendientes))
                return render_template('listado-pedidos-pendientes.html',
                                       tipo=session['usuarioTipo'],
                                       mensaje='No hay pedidos pendientes')
            else:
                productos = Producto.query.all()
                return render_template('listado-pedidos-pendientes.html',
                                       tipo=session['usuarioTipo'],
                                       pedidos_pendientes=pedidos_pendientes,
                                       productos=productos)
        else:
            return redirect(url_for('main'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)