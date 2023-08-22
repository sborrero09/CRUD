import json
import os
import time

def validar_opcion(numero):
    while True:
        try:
            num = int(numero)
            if 0 <num< 7: return num
            else:
                print("Ingrese Un número Valido (1 a 6)...")
                numero = input("Introduce El Número Nuevamente:  ").strip()
        except ValueError: print("Ingresa Un Dato Válido ..."); numero=input("Introduce El Número Nuevamente:  ").strip()

def cargar_datos():
    try:
        with open('departamentos.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        with open('departamentos.json', 'w', encoding='utf-8') as archivo:
            json.dump({"departamentos": []}, archivo)
        return {"departamentos": []}
listado = cargar_datos()

def guardar_datos(departamentos):
    with open('departamentos.json', 'w') as archivo:
        json.dump(departamentos, archivo, indent=4)

#!  ---------------> FUNCION NUMERO 1   <---------------
def listar_todas_las_ciudades():
    if listado['departamentos'] != []:
    #? verificamos si existe algun valor llamado dep en el json
        idx = 0
        ciudades_presentes = False
        #? mientras no encuentre ciudades y no se acabe la lista de departamentos ejecuta
        while not ciudades_presentes and idx < len(listado['departamentos']):
            #? volvemos boleano la lista, asi podemos saber si existe alguna ciudad, valida
            ciudades_presentes = bool(listado['departamentos'][idx]['ciudades'])
            idx += 1
        if ciudades_presentes:
            os.system('cls')
            #print("━"*44+"\n"+"┃{:^42}┃".format("LISTA DE LAS CIUDADES"))
            print("\n"+"{:^42}".format("LISTA DE LAS CIUDADES"))
            print("━"*63+"\n"+"{:^15} {:^15} {:^15} {:^15}".format("Nombre", "latitud", "longitud", "Imagen")+"\n"+"-"*63)
            for departamento in listado['departamentos']:
                for n, ciudad in enumerate(departamento['ciudades'], start=1):
                    #print("┃ {:<1}.{:^39}┃".format(n, ciudad['nomCiudad']))
                    print("{:<1}.{:15}|{:^15}|{:^15}|{:^15}".format(n, ciudad['nomCiudad'],"30","50",ciudad['imagen']))
            print("-"*63)
            print('\n')
            time.sleep(4)
        else: print("\n\nNo Hay Ciudades Para Mostrar...\n\n"); time.sleep(4)
    else: print("\n\nNo se ha almacenado Ninguna Ciudad En La Base De Datos\n\n"); time.sleep(4)

#!  ---------------> FUNCION NUMERO 2   <---------------
def crear_ciudad_en_departamento():
    if listado['departamentos'] != []:
        listar_departamentos()
        indice = int(input("Número Del Departamento Donde Quiere Crear La Ciudad: "))-1
        if 0 <= indice <= len(listado['departamentos']): 
            city = input("Ingrese El Nombre De La Ciudad A Agregar:  ")
            picture = input("Ingrese La Imagen De La ciudad:  ")
            latitude = input("Ingrese La Latitud De La Ciudad:  ")
            longitude = input("Ingrese La Longitud De La Ciudad:  ")
            departament = listado['departamentos'][indice]
            ciudades = departament['ciudades']
            
            nueva_ciudad = {"idCiudad": len(ciudades)+1,"nomCiudad": city,"imagen": picture,
            "coordenadas": {"lat":latitude, "lon":longitude}}
            
            ciudades.append(nueva_ciudad)
            guardar_datos(listado)
        else: print("Indice Del Departamento Inválido")
    else: print("\n\n\tAsegúrese De Crear Un Departamento\n\tantes de añadir una ciudad\n\n"); time.sleep(4)

#!  ---------------> FUNCION NUMERO 3   <---------------
def eliminar_ciudad_en_departamento():
    if listado['departamentos'] != []:
        idx = 0; ciudades_presentes = False
        while not ciudades_presentes and idx < len(listado['departamentos']):
            ciudades_presentes = bool(listado['departamentos'][idx]['ciudades']); idx += 1
        if ciudades_presentes:
            listar_departamentos()
            indice = int(input("Número Del Departamento Donde Quiere Eliminar La Ciudad: "))-1
            if 0 <= indice < len(listado['departamentos']):
                print("━"*44+"\n"+"┃{:^42}┃".format("CIUDADES DE "+listado['departamentos'][indice]['nomDepartamento']))
                for n, departamento in enumerate(listado['departamentos'][indice]['ciudades'], start=1):
                    print("┃ {:<1}.{:^39}┃".format(n, departamento['nomCiudad']))
                print("━"*44,"\n")
                indice2 = int(input("\n\nNúmero De la Ciudad a Eliminar: "))-1
                if 0 <= indice < len(listado['departamentos'][indice]['ciudades']):
                    ciudad_eliminada = listado['departamentos'][indice]['ciudades'].pop(indice2)
                    print(f"El departamento '{ciudad_eliminada['nomCiudad']}' ha sido eliminado."); guardar_datos(listado)
                else: print("Índice de la ciudad Inválido")
            else: print("Índice del Departamento Inválido")
        else: print("\n\n\tAsegúrese De Añadir Una Ciudad A\n\tla Base De Dato Antes De Eliminarla\n\n"); time.sleep(4)
    else: print("\n\n\tNo Existen Departamentos, Cree Uno\n\tantes de eliminar una ciudad\n\n"); time.sleep(4)

#!  ---------------> FUNCION NUMERO 4   <---------------
def crear_departamento():
    if listado['departamentos'] != []:
        indice = len(listado['departamentos'])+1
    else: indice = 1
    name = input("Ingrese El Nombre Del Departamento A Agregar:  ")
    añadir_departamento = {'idDepartamento': indice,'nomDepartamento': name,'ciudades': []}

    listado['departamentos'].append(añadir_departamento)
    guardar_datos(listado)

#!  ---------------> FUNCION NUMERO 5   <---------------
def eliminar_departamento():
    if 'departamentos' in listado:
        listar_departamentos()
        indice = int(input("Ingrese El Número Del Departamento A Eliminar:  ")) - 1
        if 0 <= indice <= len(listado['departamentos']):
            dep_eliminado = listado['departamentos'].pop(indice)
            print(f"El Departamento {dep_eliminado} Fué Eliminado Correctamente.")
        else:
            print("Indice Del Departamento Inválido")
    else: print("\n\n\tAsegúrese De Añadir Un Departamento A\n\tla Base De Dato Antes De Eliminarlo\n\n"); time.sleep(4)

#!  ---------------> FUNCION NUMERO 6   <---------------
def listar_departamentos():
    if listado['departamentos'] != []:
    #if 'departamentos'[] in listado: 
        os.system('cls')
        print("━"*44+"\n"+"┃{:^42}┃".format("LISTA DE LOS DEPARTAMENTOS")+"\n"+"━"*44)
        for n, departamento in enumerate(listado['departamentos'], start=1):
            print("┃ {:<1}.{:^39}┃".format(n, departamento['nomDepartamento']))
            print("━"*44)
        print('\n')
        time.sleep(4)
    else: print("\n\nNo Hay Departamentos Para Mostrar...\n\n"); time.sleep(4)

def menu():
    ciclo = True
    while ciclo:
        print("="*10," MODÚLO GESTOR DE CIUDADES ","="*10,"\n")
        print("\t1. Listar Todas Las Ciudades")
        print("\t2. Crear Una Ciudad En un Departamento")
        print("\t3. Eliminar Una Ciudad De un Departamento")
        print("\t4. Crear un Departamento")
        print("\t5. Eliminar Un Departamento")
        print("\t6. Listar Todos los Departamentos")
        print("\n","="*48)
        opcion = validar_opcion((input('\nIngrese Una opción --->  ')))
        switch = {
                1: listar_todas_las_ciudades,
                2: crear_ciudad_en_departamento,
                3: eliminar_ciudad_en_departamento,
                4: crear_departamento,
                5: eliminar_departamento,
                6: listar_departamentos
                }
        switch[opcion]()
menu()