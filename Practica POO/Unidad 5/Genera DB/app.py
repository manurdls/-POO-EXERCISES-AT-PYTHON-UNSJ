import hashlib
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuario, Pedido, Producto, ItemPedido


@app.route('/')
def main():


    # Creacion Cocinero
    clave = hashlib.md5(bytes("25978634", encoding='utf-8'))
    cocinero = Usuario(DNI=25978634, Clave=clave.hexdigest(), Tipo="Cocinero")
    db.session.add(cocinero)
    db.session.commit()

    # Creacion Mozo
    clave = hashlib.md5(bytes("38459309", encoding='utf-8'))
    mozo = Usuario(DNI=38459309, Clave=clave.hexdigest(), Tipo="Mozo")
    db.session.add(mozo)
    db.session.commit()

    # Creacion Pedido 1
    pedido1 = Pedido(NumPedido=2, Fecha=datetime.now(), Total=440, Cobrado=False, Observacion="Lomo sin aderezos", DNIMozo=38459309, Mesa=1)
    db.session.add(pedido1)
    db.session.commit()

    # Creacion Pedido 2
    pedido2 = Pedido(Fecha=datetime.now(), Total=370, Cobrado=True, Observacion="", DNIMozo=38459309, Mesa=2)
    db.session.add(pedido2)
    db.session.commit()

    # Crecion Producto 1
    producto1 = Producto(Nombre="Pizza Muzarrella", PrecioUnitario=350)
    db.session.add(producto1)
    db.session.commit()

    # Crecion Producto 2
    producto2 = Producto(Nombre="Gaseosa", PrecioUnitario=90)
    db.session.add(producto2)
    db.session.commit()

    # Crecion Producto 3
    producto3 = Producto(Nombre="Cerveza", PrecioUnitario=120)
    db.session.add(producto3)
    db.session.commit()

    # Crecion Producto 4
    producto4 = Producto(Nombre="Lomo", PrecioUnitario=250)
    db.session.add(producto4)
    db.session.commit()

    # Creacion Item 1
    item1 = ItemPedido(NumItem=2, NumPedido=2, NumProducto=1, Precio=350, Estado="Pendiente")
    db.session.add(item1)
    db.session.commit()

    # Creacion Item 2
    item2 = ItemPedido(NumPedido=2, NumProducto=2, Precio=90, Estado="Pendiente")
    db.session.add(item2)
    db.session.commit()

    # Creacion Item 3
    item3 = ItemPedido(NumPedido=3, NumProducto=3, Precio=120, Estado="Listo")
    db.session.add(item3)
    db.session.commit()

    # Creacion Item 4
    item4 = ItemPedido(NumPedido=3, NumProducto=4, Precio=250, Estado="Listo")
    db.session.add(item4)
    db.session.commit()

    return "Listo"

@app.route('/test')
def test():
    usuario = Usuario.query.filter_by(DNI=38459309).first()
    pedido = Pedido.query.filter_by(Cobrado=True).first()

    return render_template('test.html', usuario=usuario, pedido=pedido)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)