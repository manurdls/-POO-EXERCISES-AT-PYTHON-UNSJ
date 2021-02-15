import re

class Email:
    __id = ""
    __domain = ""
    __domainType = ""
    __password = ""

    def __init__(self, email):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
            self.__id = email[ : email.find("@")]
            self.__domain = email[ email.find("@")+1 : email.find(".")]
            self.__domainType = email[ email.find(".")+1 : ]
        else:
            raise TypeError("Formato de mail invalido: el formato debe ser xxxxxxxxx@xxxxx.xxx")

    def __str__(self):
        return self.__id + '@' + self.__domain + '.' + self.__domainType

    def setPassword(self, password):
        self.__password = password



