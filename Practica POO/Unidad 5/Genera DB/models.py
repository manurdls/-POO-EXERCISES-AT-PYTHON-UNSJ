from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = "Usuarios"
    DNI = db.Column(db.Integer, primary_key=True)
    Clave = db.Column(db.String(120), nullable=False)
    Tipo = db.Column(db.String(120), nullable=False)
    pedidos = db.relationship('Pedido', backref='Usuarios', cascade="all, delete-orphan", lazy='dynamic')

class Pedido(db.Model):
    __tablename__ = "Pedidos"
    NumPedido = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.DateTime, nullable=False)
    Total = db.Column(db.Float)
    Cobrado = db.Column(db.Boolean, nullable=False)
    Observacion = db.Column(db.String(500), nullable=False)
    DNIMozo = db.Column(db.Integer, db.ForeignKey('Usuarios.DNI'))
    Mesa = db.Column(db.Integer, nullable=False)
    items = db.relationship('ItemPedido', backref='Pedidos', cascade="all, delete-orphan", lazy='dynamic')

class Producto(db.Model):
    __tablename__ = "Productos"
    NumProducto = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(120), nullable=False)
    PrecioUnitario = db.Column(db.Float, nullable=False)
    items = db.relationship('ItemPedido', backref='Productos', cascade="all, delete-orphan", lazy='dynamic')

class ItemPedido(db.Model):
    __tablename__ = 'ItemsPedidos'
    NumItem = db.Column(db.Integer, primary_key=True)
    NumPedido = db.Column(db.Integer, db.ForeignKey('Pedidos.NumPedido'))
    NumProducto = db.Column(db.Integer, db.ForeignKey('Productos.NumProducto'))
    Precio = db.Column(db.Float, nullable=False)
    Estado = db.Column(db.String(120), nullable=False)