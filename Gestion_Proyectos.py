from datetime import datetime
import json

#Funcion para la lectura de datos del JSON


#Se declara la clase de Proyecto
class Proyecto:

    def __init__(self,id,nombre,descripcion,inicio,vencimiento,estado,empresa,gerente,equipo):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.estado=estado
        self.empresa=empresa
        self.gerente=gerente
        self.equipo=equipo
        self.tareas=[]

    #Se crea una funcion para agregar tareas al proyecto
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)

    #Funcion para mostrar todos los datos del proyecto
    def mostrar(self):
        print('------')
        print('ID: {:<10}'.format(self.id))
        print('Nombre: {:<15}'.format(self.nombre))
        print('Descripcion: {:<15}'.format(self.descripcion))
        print('Inicio: {:<15}'.format(self.inicio.strftime("%d-%m-%Y")))
        print('Vencimiento: {:<15}'.format(self.vencimiento.strftime("%d-%m-%Y")))
        print('Estado: {:<15}'.format(self.estado))
        print('Empresa: {:<15}'.format(self.empresa))
        print('Gerente: {:<10}'.format(self.gerente))
        print('Equipo: {:<10}'.format(", ".join(self.equipo)))
        print('------')

class Tarea:

    def __init__(self,id,nombre,empresa,cliente,descripcion,inicio,vencimiento,estado,porcentaje=""):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimieno=vencimiento
        self.estado=estado
        self.empresa=empresa
        self.cliente=cliente
        self.porcentaje=porcentaje
        self.subtareas=[]

    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)
        

class Subtarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado


def cargar_datos_desde_json(nombre_archivo_txt):
    proyectos=[]
    
    def convertir_fecha(fecha_str):
        return datetime.strptime(fecha_str, "%d-%m-%Y")

    with open(nombre_archivo_txt, "r") as archivo_txt:
        nombre_archivo_json = archivo_txt.readline().strip()

    with open(nombre_archivo_json, "r") as archivo_json:
        datos = json.load(archivo_json)
        for proyecto_data in datos["proyectos"]:
            proyecto = Proyecto(
                proyecto_data["id"],
                proyecto_data["nombre"],
                proyecto_data["descripcion"],
                convertir_fecha(proyecto_data["inicio"]),
                convertir_fecha(proyecto_data["vencimiento"]),
                proyecto_data["estado"],
                proyecto_data["empresa"],
                proyecto_data["gerente"],
                proyecto_data["equipo"]
            )
            
            for tarea_data in proyecto_data["tareas"]:
                tarea = Tarea(
                    tarea_data["id"],
                    tarea_data["nombre"],
                    tarea_data["cliente"],
                    tarea_data["descripcion"],
                    convertir_fecha(tarea_data["inicio"]),
                    convertir_fecha(tarea_data["vencimiento"]),
                    tarea_data["estado"],
                    tarea_data["avance"]
                )
                for subtarea_data in tarea_data.get("subtareas", []):
                    subtarea = Subtarea(
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                        subtarea_data["descripcion"],
                        subtarea_data["estado"]
                    )
                    tarea.agregar_subtarea(subtarea)
                proyecto.agregar_tarea(tarea)
            
            proyectos.append(proyecto)
            
    return proyectos




def buscar_proyectos(proyectos):
    print("Buscar Proyecto por: ")
    
    print("1.- Nombre: ")
    print("2.- Empresa: ")
    print("3.- Gerente: ")
    print("4.- Equipo: ")
    criterio=str(input("Ingrese opcion: "))


    if criterio=="1":
        nombre = str(input("Introduzca el nombre del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if nombre.lower() in proyecto.nombre.lower()]
        if filtrado==[]:
            print("No existen proyectos con ese nombre")
        
    elif criterio=="2":
        empresa = str(input("Introduzca la empresa del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if empresa.lower() in proyecto.empresa.lower()]
        if filtrado==[]:
            print("No existen proyectos de esa empresa")


    elif criterio=="3":
        gerente = str(input("Introduzca nombre del gerente del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if gerente.lower() in proyecto.gerente.lower()]
        if filtrado==[]:
            print("No existen proyectos administrados por ese gerente")
        

    elif criterio=="4":
        equipo = str(input("Introduzca integrantes del equipo del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if equipo.lower() in proyecto.equipo]
        if filtrado==[]:
            print("No existen proyectos administrados por ese equipo")
    

    
    else:
        print("Opcion Invalida")

    
    if filtrado:
        print("Proyectos encontrados: ")
        for proyecto in filtrado:
            print('ID: {:^10} / Nombre: {:^15}  /  Empresa: {:^15}  /  Equipo: {:^10}  /  Gerente: {:^10}'.format(proyecto.id, proyecto.nombre, proyecto.empresa, ", ".join(proyecto.equipo), proyecto.gerente))

        
        seleccion=str(input("\nSeleccione el ID del proyecto que desea operar: "))
        for proyecto in filtrado:
            if seleccion == str(proyecto.id):
                return proyecto

        print("ID invalido")
        return None

#Definimos nuestra funcion principal para gestionar los proyectos
def Gestion_proyecto(proyectitos):
    #Construimos un menu para que el usuario elija la accion a realizar
    print("--------------------")
    print("Gestion del Proyecto ")
    print("Elija la operacion a realizar:")
    print("1.- Modificar. ")
    print("2.- Consultar. ")
    print("3.- Listar. ")
    print("4.- Eliminar. ")

    opcion=str(input("Ingrese opcion: "))
    print()
    

    if opcion=="1":
        #Se busca el proyecto con el que se va a realizar la accion elegida
        proyecto=buscar_proyectos(proyectitos)
        print("Ingrese las modificaciones del proyecto: ")
        proyecto.id=str(input("ID: "))
        proyecto.nombre=str(input("Nombre: "))
        proyecto.descripcion=str(input("Descripcion: "))
        proyecto.inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        proyecto.vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        proyecto.estado=str(input("Estado actual: "))
        proyecto.empresa=str(input("Empresa: "))
        proyecto.gerente=str(input("Gerente: "))
        proyecto.equipo=str(input("Equipo: ")).split(",")
    
    elif opcion=="2":
        proyecto=buscar_proyectos(proyectitos)
        print("Informacion del Proyecto:")
        proyecto.mostrar()

    elif opcion=="3":
        for proyecto in proyectitos:
            proyecto.mostrar()

    elif opcion=="4":
        proyecto=buscar_proyectos(proyectitos)
        option=str(input("Desea borrar el proyecto "+proyecto.nombre+"?: "))
        if option.lower()=="si":
            proyectitos.remove(proyecto)
            print("Proyecto Eliminado")
        else:
            print("Eliminacion cancelada")
        

    print("Desea seguir con la gestion de Proyectos?: ")
    print("1.- Si\n2.-No")
    seguir=(input(">. "))
    
    if seguir=="1":
        print("")
        Gestion_proyecto(proyectitos)
    else: pass


proyectitos=[]
proyectitos=cargar_datos_desde_json("config.txt")


Gestion_proyecto(proyectitos)