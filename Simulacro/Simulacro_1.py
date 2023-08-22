import json
import os

def openFile():
    with open("./Simulacro/PaisCiudad.json","r") as file:
        data = json.load(file)
    return data

def saveFile(data):
    with open("./Simulacro/PaisCiudad.json", "w", encoding="utf-8") as file:
        json.dump(data,file, indent=4,)

def message(msg:str) -> None:
    input(f"{msg}\nEnter any key to continue...")

def readInt(msg:str) -> int:
    try:
        return int(input(f"{msg}? "))
    except ValueError:
        message("Error. ValueError not int.")
        return readInt(msg)
    
def readString(msg:str) -> str:
    try:
        return input(f"{msg}? ")
    except ValueError:
        message("Error. ValueError not str")
        return readString(msg)
    
def stringValidate(msg: str) -> str:
    data = readString(msg)
    while(data.strip()==''):
        message("The string is void. Try again.")
        data=readString(msg)
    return data

def rangeValidator(a: int, b: int, msg:str) -> int:
    option = readInt(msg)
    if option>=a and option<=b:
        return option
    else:
        message("Out of range.")
        return rangeValidator(a,b,msg)
    
def listCitys() -> None:
    data = openFile()
    os.system("clear")
    [[print(f"{city['nomCiudad']}") for city in dpto["Ciudades"]] for dpto in data["Departamentos"] ]
    message("")

def listDpto(menu=True) -> None:
    data = openFile()
    [print(f"{dpto['idDep']}. {dpto['nomDepartamento']}") for dpto in data["Departamentos"]]
    # for i in range(len(data["Departamentos"])):
    #     print(f"{i+1}. ID:{data['Departamentos'][i]['idDep']}")

    # for idx,dpto in enumerate(data["Departamentos"]):
    #     print(f"{idx+1}. ID:{dpto['idDep']} - Nombre:{dpto['nomDepartamento']}")

    if menu:
        message("")

def listId() -> list:
    data = openFile()
    idsCitys = []
    idsDptos = [dpto['idDep'] for dpto in data['Departamentos']]
    [idsCitys.extend([city['idCiudad'] for city in dpto['Ciudades']]) for dpto in data["Departamentos"]]
    return idsCitys,idsDptos

def findDepartmentById(id:int) -> int:
    data = openFile()
    dpts = data["Departamentos"]
    i=0
    while id != dpts[i]["idDep"]:
        i+=1
    return i


def addNewCity() -> None:
    data = openFile()
    os.system("clear")
    listDpto(menu=False)
    idCitys,idDptos = listId()
    opDpto = readInt("ID Department")
    while opDpto not in idDptos:
        message("Error. ID invalid.")
        opDpto = readInt("ID Department")
    idxDpt=findDepartmentById(opDpto)
    newID = readInt("ID")
    while newID<0 or newID in idCitys:
        message("Error. Invalid ID.")
        newID = readInt("ID")
    name = stringValidate("Name")
    dptos = data["Departamentos"]
    namesCitys = [city["nomCiudad"] for city in dptos[idxDpt]["Ciudades"]]
    while name in namesCitys:
        message("Error. Invalid Name.")
        name=stringValidate("Name")
    data["Departamentos"][idxDpt]["Ciudades"].append({"idCiudad":newID,"nomCiudad":name.capitalize(),"image":name.lower()+".jpg","coordernadas":{"lat":5,"lon":89}})
    saveFile(data)
    message("Save Succesfuly")

def deleteCity() -> None:
    data = openFile()
    os.system("clear")
    listDpto(menu=False)
    idCitys,idDptos = listId()
    opDpto = readInt("ID Department")
    while opDpto not in idDptos:
        message("Error. ID invalid.")
        opDpto = readInt("ID Department")
    idxDpt=findDepartmentById(opDpto)
    dptos = data["Departamentos"]
    idCitys = [city["idCiudad"] for city in dptos[idxDpt]["Ciudades"]]
    [print(f'{city["idCiudad"]}. {city["nomCiudad"]}') for city in dptos[idxDpt]["Ciudades"]]
    idCity = readInt("ID a elminar")
    while idCity not in idCitys:
        message("Error. Invalid ID.")
        idCity = readInt("Id a eliminar")
    [data['Departamentos'][idxDpt]['Ciudades'].remove(city) for city in dptos[idxDpt]["Ciudades"] if city['idCiudad']==idCity]
    saveFile(data)
    message("Delete succesfuly")

def createDepartment() -> None:
    data = openFile()
    os.system("clear")
    idDptos = [dpto['idDep'] for dpto in data["Departamentos"]]
    nameDptos = [dpto['nomDepartamento'] for dpto in data["Departamentos"]]
    idDpto = readInt("ID department")
    while idDpto in idDptos:
        message("Error. Invalid ID")
        idDpto = readInt("ID Department")
    name = stringValidate("Name")
    while name in nameDptos:
        message("Error. Invalid Name.")
        name = stringValidate("Name")
    newID = readInt("ID City")
    idCitys = listId()
    while newID<0 or newID in idCitys:
        message("Error. Invalid ID.")
        newID = readInt("ID City")
    nameCity = stringValidate("Name City")
    data["Departamentos"].append({"idDep":idDpto,"nomDepartamento":name,"Ciudades":[{"idCiudad":newID,"nomCiudad":nameCity.capitalize(),"image":nameCity.lower()+".jpg","coordernadas":{"lat":5,"lon":89}}]})
    saveFile(data)
    message("Save Succesfuly")

def deleteDepartment() -> None:
    data = openFile()
    os.system("clear")
    listDpto(menu=False)
    idCitys,idDptos = listId()
    opDpto = readInt("ID Department")
    while opDpto not in idDptos:
        message("Error. ID invalid.")
        opDpto = readInt("ID Department")
    idxDpt=findDepartmentById(opDpto)
    data["Departamentos"].pop(idxDpt)
    saveFile(data)
    message("Delete Succesfuly.")

def menu():
    os.system("clear")
    print("{:=^60}".format("MAIN MENU"))
    options = ["Listar todas las ciudades, sin clasificar por departamento.", "Adicionar una nueva ciudad en un departamento existente.", "Eliminar una ciudad de un departamento","Crear un departamento","Eliminar un departamento","Listar todos los Departamentos","Salir"]
    for i, option in enumerate(options):
        print(f"{str(i+1):>6}. {option}")
    option = rangeValidator(1,len(options),"Option")
    if option == len(options):
        return print("{:=^60}".format("PROGRAM FINISH"))
    switch = {1:listCitys, 2:addNewCity, 3:deleteCity, 4:createDepartment, 5:deleteDepartment ,6:listDpto}
    switch[option]()
    menu()

menu()