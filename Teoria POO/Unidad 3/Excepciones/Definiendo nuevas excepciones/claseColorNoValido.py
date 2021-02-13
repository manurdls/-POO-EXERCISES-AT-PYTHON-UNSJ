from claseErrorAuto import ErrorAuto

class ColorNoValido(ErrorAuto):
    """Lanzado cuando el atributo color de un auto no tiene un valor valido"""
    def __init__(self, auto, mensaje):
        super().__init__(auto, mensaje = 'ColorNoValido: ' + mensaje)