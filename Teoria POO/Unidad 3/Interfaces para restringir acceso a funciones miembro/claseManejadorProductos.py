afrom claseProducto import Producto
from interfaces import ICajero, ISupervisor
from zope.interface import implementer

@implementer(ICajero)
@implementer(ISupervisor)
class ManejadorProductos():
    __productos = []

    def __init__(self):
        self.__productos = []

    def agregarProducto(self, producto):
        self.__productos.append(producto)

    def buscarProductoPorDescripcion(self, descripcion):
        """
        Método de la interface ICajero
        """
        i = 0
        bandera = False
        retorno = None
        while not bandera and i<len(self.__productos):
            unProducto = self.__productos[i]
            if unProducto.getDescripcion() == descripcion:
                bandera = True
            else:
                i += 1
        if bandera:
            retorno = self.__productos[i]
        return retorno

    def buscarProductoPorCodigo(self, codigo):
        """
        Método de la interface ISupervisor
        """
        i = 0
        bandera = False
        retorno = None
        while not bandera and i<len(self.__productos):
            unProducto = self.__productos[i]
            if unProducto.getCodigo() == codigo:
                bandera = True
            else:
                i += 1
        if bandera:
            retorno = self.__productos[i]
        return retorno

    def modificarPrecioProducto(self, codigo, precio):
        """
        Método de la interface ISupervisor
        """
        producto = self.buscarProductoPorCodigo(codigo)
        if producto == None:
            print('Producto código {}, no encontrado'.format(codigo))
        else:
            producto.modificarPrecio(precio)