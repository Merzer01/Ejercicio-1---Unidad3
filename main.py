from classManejador import manejador
from classMenu import Menu
import os

if __name__ == '__main__':
    os.system('cls')
    m = manejador()
    m.readarchivo()
    band = True
    
    while band:
        menu = Menu()
        opcion = menu.showmenu()
        if opcion == 1:
            print("OPCION 1")
            m.showcarreras()
        elif opcion == 2:
            print("OPCION 2")
            m.buscar_carrera()
        elif opcion == 3:
            m.mostrar()
        elif opcion == 0:
            print("Saliendo...")
            band = False
        else: print("OPCION INCORRECTA")
        os.system('pause')
        os.system('cls')