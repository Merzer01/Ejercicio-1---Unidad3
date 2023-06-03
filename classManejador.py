from classFacultad import facultad
from classCarrera import carrera
import csv

class manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    
    def readarchivo (self):
        with open ('Facultades.csv', 'r', encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')

            for row in lector:
                if len(row) == 5:
                    d1 = int(row[0]) #codigo de la facultad
                    d2 = str(row[1]) #nombre
                    d3 = str(row[2]) #direccion
                    d4 = str(row[3]) #localidad
                    d5 = str(row[4]) #numero de telefono
                    f = facultad(d1, d2, d3, d4, d5)
                    self.__lista.append(f)
                    cod = row[0]
                else:
                    d1 = int(row[0]) #codigo de la facultad
                    d6 = int(row[1])    #codigo de la carrera
                    d7 = str(row[2])    #nombre
                    d8 = str(row[3])    #titulo
                    d9 = str(row[4])    #semestres
                    d10 = str(row[5])   #grado
                    self.__lista[d1-1].setcarrera(d6, d7, d8, d9, d10)
    
    def showcarreras(self): #item 1
        cod = int(input("Ingrese codigo de la facultad a buscar: "))
        band = False
        i = 0
        while not band:
            if cod == self.__lista[i].getcod():
                print('''
Nombre: {}
Listado de carreras:                 
                '''.format(self.__lista[i].getnombre()))
                self.__lista[i].listado()
                band = True
            else: i += 1
    
    def buscar_carrera(self):   #item 2
        car = str(input("Ingrese nombre de la carrera: "))
        i = 0
        band = False
        while not band:
            dato = []
            if self.__lista[i].busca_carrera(car, dato):
                band = True
            else: i += 1
        
        if i < len(self.__lista):
            print('''
Codigo: {} - {}
Nombre: {}
Localidad: {}            
            '''.format(self.__lista[i].getcod(), dato[0], self.__lista[i].getnombre(), self.__lista[i].getlocalidad()))
    
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            self.__lista[i].listado()