import time
import os
import csv

contactos = []

def opciones_menu(p_opcs):
    while True:
        print('Menú contactos\n\t1. Agregar contactos\n\t2. Ver contactos\n\t3. Exportar archivo CSV\n\t4. Salir\n')
        try:
            opc = int(input('Ingrese una opcion: '))
            if opc in p_opcs:
                return opc
            else:
                print('ERROR! debe ingresar una opcion valida, opciones validas (1,2,3,4)!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar un numero entero!')
    

def Agregar_contacto():
    while True:
        nombre_contacto = str(input('Ingrese el nombre el nombre del contacto: '))
        if len(nombre_contacto.strip())  >= 3 and nombre_contacto.isalpha():
            print('Nombre registrado correctamente!')
            time.sleep(1)
            os.system('cls')
            break
        else:
            print('ERROR! debe ingresar un nombre que contenga al menos 3 letras!')
        time.sleep(1)
        os.system('cls')
    
    while True:
        try:
            num_contacto = int(input('Ingrese el número de celular: '))
            if len(str(num_contacto)) == 9 and str(num_contacto)[0]== "9":
                print('Numero de celular registrado!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! el telefono debe comenzar con 9 y tener 9 digitos!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar números enteros!')

    while True:
        # patterns
        contador = 0
        correo = str(input('Ingrese el correo: '))
        for x in correo:
            if x == "@":
                contador = contador + 1
        
        if contador == 1:
            print('Correo registrado!')
            time.sleep(1)
            os.system('cls')
            break
        else:
            print('ERROR! correo no valido, el correo debe contener "@"')
        time.sleep(1)
        os.system('cls')


        # if correo.strip().lower().endswith("@gmail.com") and len(correo.strip()) >=13:
        #  print('Correo registrado!')
        # time.sleep(1)
        # os.system('cls')
        # else:
            # print('Error el correo debe contener 13 caracteres , incluir el @gmail.com !')   
    
    contacto = {
        "nombre":nombre_contacto,
        "telefono":num_contacto,
        "correo":correo
    }

    contactos.append(contacto)


def ver_contactos():
    if len(contactos) >= 1:
        while True:
            print('\tLISTA DE CONTACTOS\n')
            for c in contactos:
                print("\tNombre:",c["nombre"],"\n\tNumero celular:",c["telefono"],"\n\tCorreo:",c["correo"],end="\n")
            try:
                opc_salir = int(input('¿Deseas salir? Ingresa (1:Salir) (0:Redirigir): '))
                if opc_salir in (1,0):
                    if opc_salir == 1:
                        print('Saliendo.')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        print('Redirigiendo.')
                        time.sleep(1)
                        os.system('cls')
                else:
                    print('ERROR! debe ingresar una opcion valida, opciones validas(1 o 0)!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debes ingresar un número entero!')



def exportar_archivo_csv():
    if len(contactos) >= 1:
            nombre_archivo = str(input('Ingrese el nombre del archivo: '))
            try: 
                with open(f"{nombre_archivo}.csv","x",newline="") as archivo:
                    escritor = csv.DictWriter(archivo, ["nombre","telefono","correo"])
                    escritor.writerows(contactos)
                print('ARCHIVO CREADO')
            except:
                print('ERROR! el nombre del archivo ya existe!')
    else:
        print('NO HAY CONTACTOS REGISTRADOS!')
    time.sleep(1)
    os.system('cls')
        
    

def salir():
    for i in range(1,4):
        print('Saliendo de la app de contactos',("."*i))
        time.sleep(1)
        os.system('cls')



# escritor = csv.DictWriter(archivo, ["nombre","telefono","correo"])
        # contactos[0].keys