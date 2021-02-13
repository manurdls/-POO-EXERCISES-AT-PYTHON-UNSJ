import requests

class Provincia(object):
    __nombre = None
    __capital = None
    __cantHabitantes = None
    __cantDP = None
    __temperatura = None
    __sensacionTermica = None
    __humedad = None

    def __init__(self, nombre, capital, cantHabitantes, cantDP):
        self.__nombre = self.requerido(nombre, 'Nombre es un dato requerido')
        self.__capital = self.requerido(capital, 'Capital es un dato requerido')
        self.__cantHabitantes = self.requerido(cantHabitantes, 'Cantidad de habitantes es un dato requerido')
        self.__cantDP = self.requerido(cantDP, 'Cantidad de departamentos/partidos es un dato requerido')
        self.setWeatherData()

    def __str__(self):
        return 'Nombre: {}\nCapital: {}\nCantidad de habitantes: {}\n' \
               'Cantidad de departamentos/partidos: {}\nTemperatura: {}\n' \
               'Sensación térmica: {}\nHumedad: {}\n'.format(self.getNombre(),
                                                             self.getCapital(),
                                                             self.getCantHabitantes(),
                                                             self.getCantDP(),
                                                             self.getTemperatura(),
                                                             self.getSensacionTermica(),
                                                             self.getHumedad())

    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getCantHabitantes(self):
        return self.__cantHabitantes
    def getCantDP(self):
        return self.__cantDP
    def getTemperatura(self):
        return self.__temperatura
    def getSensacionTermica(self):
        return self.__sensacionTermica
    def getHumedad(self):
        return self.__humedad
    def setWeatherData(self):
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q='+str(self.__capital)+'&units=metric&appid=6702d6d8e0b5e8155ef073fd71167814'
        r = requests.get(complete_url)
        json = r.json()
        try:
            if json['message'] == 'city not found':
                pass
        except:
            for i in json:
                if i == 'main':
                    self.__temperatura = str(json[i]['temp'])
                    self.__sensacionTermica = str(json[i]['feels_like'])
                    humedad = str(json[i]['humidity'])+'%'
                    self.__humedad = humedad
        else:
            raise ValueError('La ciudad ingresada no se encuentra en la base de datos del clima')

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def __lt__(self, siguiente):
        return self.getNombre() < siguiente.getNombre()

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                cantHabitantes=self.__cantHabitantes,
                cantDP=self.__cantDP
            )
        )
        return d