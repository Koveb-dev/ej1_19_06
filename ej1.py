from funciones1 import *


print('Bienvenido a la app de contactos!')
time.sleep(1)
os.system('cls')

opciones = (1,2,3,4)

while True:
    os.system('cls')
    opc = opciones_menu((opciones))

    if opc == 1:
        print('Agregar contacto!')
        time.sleep(1)
        os.system('cls')
        Agregar_contacto()
    elif opc == 2:
        print('Ver contactos')
        time.sleep(1)
        os.system('cls')
        ver_contactos()
    elif opc == 3:
        print('Exportar archivo csv!')
        time.sleep(1)
        os.system('cls')
        exportar_archivo_csv()
    else:
        salir()
        break
