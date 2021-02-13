from datetime import datetime
import hashlib
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuarios, Pedidos, Productos, ItemsPedidos

@app.route('/')
def main():

    pedido = Pedidos(Fecha=datetime.now(),
                     Total= 500,
                     Cobrado=False, Observacion='Q este piola',
                     DNIMozo=38459309,
                     Mesa=20)
    db.session.add(pedido)
    db.session.commit()

    """# Creacion Cocinero
    clave = hashlib.md5(bytes("25978634", encoding='utf-8'))
    cocinero = Usuarios(DNI=25978634, Clave=clave.hexdigest(), Tipo="Cocinero")
    db.session.add(cocinero)
    db.session.commit()

    # Creacion Mozo
    clave = hashlib.md5(bytes("38459309", encoding='utf-8'))
    mozo = Usuarios(DNI=38459309, Clave=clave.hexdigest(), Tipo="Mozo")
    db.session.add(mozo)
    db.session.commit()

    # Creacion Pedido 1
    pedido1 = Pedidos(Fecha=datetime.now(), Total=1500, Cobrado=False, Observacion="Diego Milito @@",
                      DNIMozo=38459309, Mesa=22)
    db.session.add(pedido1)
    db.session.commit()

    # Creacion Pedido 2
    pedido2 = Pedidos(Fecha=datetime.now(), Total=440, Cobrado=False, Observacion="Lomo sin aderezos",
                     DNIMozo=38459309, Mesa=1)
    db.session.add(pedido2)
    db.session.commit()

    # Creacion Pedido 3
    pedido3 = Pedidos(Fecha=datetime.now(), Total=370, Cobrado=True, Observacion="", DNIMozo=38459309, Mesa=2)
    db.session.add(pedido3)
    db.session.commit()

    # Crecion Producto 1
    producto1 = Productos(Nombre="Pizza Muzarrella", PrecioUnitario=350)
    db.session.add(producto1)
    db.session.commit()

    # Crecion Producto 2
    producto2 = Productos(Nombre="Gaseosa", PrecioUnitario=90)
    db.session.add(producto2)
    db.session.commit()

    # Crecion Producto 3
    producto3 = Productos(Nombre="Cerveza", PrecioUnitario=120)
    db.session.add(producto3)
    db.session.commit()

    # Crecion Producto 4
    producto4 = Productos(Nombre="Lomo", PrecioUnitario=250)
    db.session.add(producto4)
    db.session.commit()

    # Creacion Item 1
    item1 =  ItemsPedidos(NumPedido=2, NumProducto=1, Precio=1500, Estado="Pendiente")
    db.session.add(item1)
    db.session.commit()

    # Creacion Item 2
    item2 = ItemsPedidos(NumPedido=2, NumProducto=1, Precio=350, Estado="Pendiente")
    db.session.add(item2)
    db.session.commit()

    # Creacion Item 3
    item3 = ItemsPedidos(NumPedido=2, NumProducto=2, Precio=90, Estado="Pendiente")
    db.session.add(item3)
    db.session.commit()

    # Creacion Item 4
    item4 = ItemsPedidos(NumPedido=3, NumProducto=3, Precio=120, Estado="Listo")
    db.session.add(item4)
    db.session.commit()

    # Creacion Item 5
    item5 = ItemsPedidos(NumPedido=3, NumProducto=4, Precio=250, Estado="Listo")
    db.session.add(item5)
    db.session.commit()"""



    return 'asd'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)