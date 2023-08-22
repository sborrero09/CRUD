import json
import os
# llamamos el json y lo leemos en la variable
with open('PetShopping.json','r') as petDatos:
    data=json.load(petDatos)
#Valida Int y no permite valores menores a cero utilidad en precios
def validarPrecio(msj):
    try:
      id=int(input(msj))
      while True:
        if id=='' or id<=0: #Exige al ususario que ingrese un dato numerico mayor a 1
          print('intentelo de nuevo\n')
          id=int(input(msj))
          continue #evita el return u hace que se repita la condicion hasta que sea falsa
        return id
    except Exception:
        print('ingrese un dato correcto correcta')
#Valida Int y no permite caracteres diferentes
def validarMenu(msj):
    while True:
        try:
            op=int(input(msj))
            if op=='': 
                print('Inegrese alguna opcion')
                input('enter...\n')
                continue
            return op
        except Exception:
            print('solo se aceptan datos numericos')
#validad str no permite datos vacios ni datos con numero dentro solo letras   
def addType(msj):
        data=input(msj)
        while data.split()=='':
            os.system('cls')
            print('Ingrese algun TIPO\n')
            data=input(msj)
        while data.isalpha()==False or data.isdigit():
          os.system('cls')
          data=input(msj)
        return data     
#muestra las mascostas
def showPets():
    os.system('cls')
    print("{:^9} {:^10} {:^10} {:^9} {:^9}".format('Tipo      |','Raza           |','Talla      |','Precio |','servicios   |'))
    for index,pet in enumerate(data['pets'],start=1) :
        servicios=', '.join(pet["servicios"])
        print()
        print("{:1} {:<9} {:<1} {:<14} {:<1} {:<10} {:<1} {:<6} {:<1} {:<12}".format(index, pet["tipo"],'|',pet["raza"],'|',pet["talla"],'|',pet["precio"],'|',servicios))
    input('\npresione enter o cualquier tecla para volver al menu...\n')
#add datos a una lista dentro de un diccionario
def addservices(msj):
    servicios=[]
    nexx=True
    while nexx:
        note=addType(msj)
        servicios.append(note)
        op=validarMenu('ingrese 0 para salir o cualquiero otro numero para agg nuevo servicio\n')
        if op==0:
            nexx=False
    return servicios
#crea un dicionario con datos dentro de una lista
def addPet():
    os.system('cls')
    tipo=addType('Ingrese el TIPO de mascota (ave,mamifero,insecto etc...)\n')
    raza=addType('Ingrese la RAZA de la mascota\n')
    talla=addType('Ingrese la TALLA de la mascota(pequeno, mediano, grande)\n')
    precio=validarPrecio('ingrese el PRECIO de la mascota\n')
    servicios=addservices('ingrese el servicio para la mascota y luego presione enter para guardar\n')
    data['pets'].append({
        "tipo":tipo,
        "raza":raza,
        "talla":talla,
        "precio":precio,
        "servicios":servicios
    })
    with open('PetShopping.json','w') as destino:
        json.dump(data,destino,indent=4)
#Busca y muestra los datos de la mascotas escogidas
def viewSearch():
   type=addType('Ingrese el tipo de mascota que desea mostrar\n')
   print("{:^9} {:^10} {:^10} {:^9} {:^9}".format('Tipo      |','Raza           |','Talla      |','Precio |','servicios   |'))
   volver=0
   for index,pet in enumerate(data['pets'], start=1):
       nexx=True
       cont=0
       while nexx:
           if pet["tipo"].lower() == type.lower():
               servicios=', '.join(pet["servicios"])
               print("{:1} {:<9} {:<1} {:<14} {:<1} {:<10} {:<1} {:<6} {:<1} {:<12}".format(index, pet["tipo"],'|',pet["raza"],'|',pet["talla"],'|',pet["precio"],'|',servicios))
               cont+=1
           if cont >0:
               nexx=False
           else:
               volver+=1
               nexx=False
           if len(data['pets'])==volver:
              os.system('cls')
              print('El TIPO DE mascota no pertenece a ningun resgistro')
              input('enter...')
              return viewSearch()
   input('\nenter...')               
#actualiza datos dentro de una lista contenida en un diccionario dicpadre:listaPadre:dicionarioh:listah
def updateList(indicador):
    os.system('cls')
    indicador-=1
    print('SERVICIOS:')
    for i in range(len(data['pets'][indicador]['servicios'])):
        print(i+1,data['pets'][indicador]['servicios'][i])
    date=validarMenu('ingrese 1 para actualizar servicio o 2 para agg servicio y 0 para salir\n')
    nexx=True
    while nexx:
      if date == 1:
          for i in range(len(data['pets'][indicador]['servicios'])):
              os.system('cls')
              print(data['pets'][indicador]['servicios'])
              nexx=True
              while nexx:
                print('para MODIFICAR:',data['pets'][indicador]['servicios'][i])
                mod=validarMenu(' digite 1 de lo contrario 0\n')
                if mod==1:
                    data['pets'][indicador]['servicios'][i]=addType('ingrese nuevo Servicio')
                    nexx=False
                elif mod==0:
                    nexx=False
                else:
                    break
      elif date == 2:
          os.system('cls')
          servicio=addType('Ingrese nuevo servicio')
          data['pets'][indicador]['servicios'].append(servicio)
          nexx=False
      elif date==0:
          return
      else:
          nexx=False
#Busca y actualiza
def update():
    showPets()
    indicador=validarMenu('Ingrese el indicie o numero de la mascota que desea ACTUALIZAR\n')
    for index, pet in enumerate(data["pets"],start=1):
        if indicador==index:
            servicios=', '.join(pet["servicios"])
            nexx=True
            while nexx: 
              os.system('cls')
              print("{:1} {:<9} {:<1} {:<14} {:<1} {:<10} {:<1} {:<6} {:<1} {:<12}".format(index, pet["tipo"],'|',pet["raza"],'|',pet["talla"],'|',pet["precio"],'|',servicios)) 
              print(' '*16,'MENU')
              print(' '*11,'1.Actualizar RAZA\n\
              2.Actualizar precio\n\
              3.Actualizar servicios\n\
              4.salir')
              op=validarMenu("Ingrese la opcion para el anterior menu\n")
              if op==1:
                  pet['raza']=addType('Ingrese nuevo RAZA:\n')
              elif op==2:
                  pet['precio']=validarPrecio('Ingrese nuevo PRECIO\n')
              elif op==3:
                  validar=updateList(indicador)
              elif op==4:
                  return
    with open('PetShopping.json','w') as destino:
        json.dump(data,destino,indent=4)
#Eliminar datos 
def delete():
    showPets()
    op=validarMenu('Ingrese el indicie o numero de la mascota que desea ELIMINAR\n')
    cont=0
    os.system('cls')
    for index, pet in enumerate(data['pets'],start=1):
       nexx=True
       aux=0
       while nexx:   
          if op == index:
              data['pets'].pop(index-1)
              servicios=', '.join(pet["servicios"])
              cont+=1
              aux+=1
              print('MASCOTA ELIMINADA:')
              input("{:1} {:<9} {:<1} {:<14} {:<1} {:<10} {:<1} {:<6} {:<1} {:<12}".format(index, pet["tipo"],'|',pet["raza"],'|',pet["talla"],'|',pet["precio"],'|',servicios))
              nexx=False
          if aux<=0:
              nexx=False
          with open('PetShopping.json','w') as destino:
              json.dump(data,destino,indent=4)
    if cont<=0:
        return print('EL indice ingresado no pertenece a niguna mascota :()')

def menu():
    nexx=True
    conf=True
    while nexx:
        os.system('cls')
        print(' '*16,'MENU \n')
        print("\t1.Mostrar todas las mascotas\n\
        2.Crear nueva mascota\n\
        3.Mostrar datos de la mascota especifica\n\
        4.Actualizar datos de la mascota\n\
        5.Eliminar mascota\n\
        6. salir")
        op=validarMenu('Ingrese una opcion del anterior menu\n')
        if op==6:
            nexx=False
            return print('THE END.')
        elif op<1 or op>6:
            print('Opcion invalida escoja una del 1 al 6')
            input('ente...')
            conf=False
        if conf ==True:
          switch={1:showPets,2:addPet,3:viewSearch,4:update,5:delete}
          switch[op]()

menu()