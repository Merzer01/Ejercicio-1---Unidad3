class carrera:
    __codigo: int
    __nombre: str
    __titulo: str
    __duracion: str
    __tipo: str
    def __init__ (self, cod, nomb, tit, dur, tip):
        self.__codigo = cod
        self.__nombre = nomb
        self.__titulo = tit
        self.__duracion = dur
        self.__tipo = tip
    def __str__(self):
        return ('''
Nombre: {} (Cod: {})
Titulo: {} - ({})
Duracion: {}
        '''.format(self.__nombre, self.__codigo, self.__titulo, self.__tipo, self.__duracion))
    
    def getnombre(self):
        return self.__nombre
    def getduracion(self):
        return self.__duracion
    def getcod(self):
        return self.__codigo