from zope.interface import Interface
#from zope.interface import implementer

class ICajero(Interface):
    """
    Declaración de interface ICajero
    El cajero solo puede buscar productos por descripción
    """
    def buscarProductoPorDescripcion(descripcion):
        pass


class ISupervisor(Interface):
    """
    Declaración de interface ISupervisor
    El supervisor puede modificar el precio de un producto de un producto, que busca por código
    """
    def buscarProductoPorCodigo(codigo):
        pass
    def modificarPrecioProducto(codigo, precio):
        pass