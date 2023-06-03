class Menu (object):
    def showmenu(self):
        print("MENU DE OPCIONES")
        print("1 - Carreras por facultad")
        print("2 - Consultar facultad")
        print("3 - Mostrar Datos -> Facultad")
        print("0 - SALIR")
        cond = False
        while not cond:
            op = int(input("Ingrese numero de opcion: "))
            if op in [1,2,3,0]:
                cond = True
        return op