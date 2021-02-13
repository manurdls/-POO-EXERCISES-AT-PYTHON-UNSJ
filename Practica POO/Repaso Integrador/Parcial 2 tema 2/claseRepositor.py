from claseEmpleado import Empleado

class Repositor(Empleado):
    __cantProdRepuestos = 0
    __nombreCompania = ""

    def __init__(self,  nombre, apellido, sueldoBasico, antiguedad, turno, cantProdRepuestos, nombreCompania):
        super().__init__(nombre, apellido, sueldoBasico, antiguedad, turno)
        self.__cantProdRepuestos = cantProdRepuestos
        self.__nombreCompania = nombreCompania

    def getCantProdRepuestos(self):
        return self.__cantProdRepuestos
    def getNombreCompania(self):
        return self.__nombreCompania

    def reglaDeNegocio(self):
        porcentaje = 0
        if self.getCantProdRepuestos() > 10 and self.getCantProdRepuestos() <= 50:
            porcentaje = 1
        else:
            if self.getCantProdRepuestos() > 50 and self.getCantProdRepuestos() <=100:
                porcentaje = 1.5
            else:
                if self.getCantProdRepuestos() > 100:
                    porcentaje = 2

        return self.getSueldoBasico()*(porcentaje/100)
