from classCarrera import carrera

class facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carrera = []
    def __init__(self, cod, nomb, direc, loc, tel):
        self.__codigo = cod
        self.__nombre = nomb
        self.__direccion = direc
        self.__localidad = loc
        self.__telefono = tel
        self.__carrera = []
    def __str__(self):
        return ('''
---------------------------------------------        
{} (Cod: {})
Direccion: {} ({})
Telefono: {}
---------------------------------------------
        '''.format(self.__nombre, self.__codigo, self.__direccion, self.__localidad, self.__telefono))

    def __del__(self):
        print("Borrando carreras de la facultad {} ({})".format(self.__nombre, self.__codigo))
        del self.__carrera

    def setcarrera(self, c, n, t, d, tp):
        c = carrera(c, n, t, d, tp)
        self.__carrera.append(c)
    
    def getcod(self):
        return self.__codigo
    def getnombre(self):
        return self.__nombre
    def getlocalidad(self):
        return self.__localidad
    
    def listado(self):
        for i in range(len(self.__carrera)):
            print(self.__carrera[i])
    
    def busca_carrera(self, c, dato):
        i = 0
        band = False

        while i < len(self.__carrera) and not band:
            if c == self.__carrera[i].getnombre():
                dato.append(self.__carrera[i].getcod())
                band = True
            else: i += 1
        return band