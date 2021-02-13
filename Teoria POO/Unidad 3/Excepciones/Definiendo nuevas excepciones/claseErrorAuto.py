class ErrorAuto(Exception):
    __auto = None
    __mensaje = None
    """Excepcion basica para errores lanzados por los autos"""

    def __init__(self, auto, mensaje = None):
        if mensaje is None:
            mensaje = 'Un error ha ocurrido con el auto %s' % str(auto)
            super(ErrorAuto, self).__init__(mensaje)
        self.__auto = auto
        self.__mensaje = 'ErrorAuto:' + mensaje

    def getAuto(self):
        return self.__auto
    def getMensaje(self):
        return self.__mensaje